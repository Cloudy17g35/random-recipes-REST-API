FROM python:3.8

WORKDIR /api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY . .

RUN chmod +x run.sh

CMD ["./run.sh"]