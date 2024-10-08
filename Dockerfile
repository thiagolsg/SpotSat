FROM python:3.10.4-slim-buster

WORKDIR /app

COPY . .

#RUN apt-get -y install libpq-dev gcc && pip install psycopg2
RUN pip install -r requirements.txt
#RUN python etl_amostras.py
 
EXPOSE 8080

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0","--port", "8080","--reload"]