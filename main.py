from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from MessageForm import MessageForm
from CheckSpam import transform_text, predict
import logging
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return JSONResponse(content=jsonable_encoder({"Message": "Yeah you are in the root"}), status_code=200)

@app.post("/api/v1/getResult/")
async def getResult(item: MessageForm):

    try:
        transformed_sms = transform_text(item.message)
        result = predict(transformed_sms)
    except Exception as e:
        logger.error(e)
        return JSONResponse(content=jsonable_encoder({"Message": "Something went wrong :("}), status_code=400)


    return JSONResponse(content=jsonable_encoder({"Message": result}), status_code=200)