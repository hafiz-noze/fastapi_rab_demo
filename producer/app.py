import pika
from fastapi import FastAPI, HTTPException, Body
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to RabbitMQ-FastAPI"}


@app.get("/hello/{message}")
def post_message(message: str):

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="rabbitmq", port=5672, 
    credentials=pika.PlainCredentials("user", "PASSWORD")))
        
    channel = connection.channel()


    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=message)

    connection.close()

    return {"Successfully sended {} do queue".format(message)}
        


