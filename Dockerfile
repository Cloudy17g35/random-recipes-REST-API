FROM python:3.8

WORKDIR /api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
ENV AWS_ACCESS_KEY_ID your_acces_key_id
ENV AWS_SECRET_ACCESS_KEY your_secret_acces_key
COPY . .

RUN chmod +x run.sh

RUN ./run.sh

CMD ["uvicorn", "server:app", "--host" , "0.0.0.0", "--port", "8080"]