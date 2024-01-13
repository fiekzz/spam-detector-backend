# 
FROM python:3.11.5-slim-bullseye

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./main.py /code/main.py
COPY ./CheckSpam.py /code/CheckSpam.py
COPY ./MessageForm.py /code/MessageForm.py
COPY ./model.pkl /code/model.pkl
COPY ./vectorizer.pkl /code/vectorizer.pkl

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]