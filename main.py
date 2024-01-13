from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from MessageForm import MessageForm
from CheckSpam import transform_text, predict

app = FastAPI()

@app.get("/")
async def read_root():
    return JSONResponse(content=jsonable_encoder({"Message": "Yeah you are in the root"}), status_code=200)

@app.post("/api/v1/getResult/")
async def getResult(item: MessageForm):

    try:
        transformed_sms = transform_text(item.message)
        result = predict(transformed_sms)
    except:
        return JSONResponse(content=jsonable_encoder({"Message": "Something went wrong :("}), status_code=400)


    return JSONResponse(content=jsonable_encoder({"Message": result}), status_code=200)