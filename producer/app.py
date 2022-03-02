import pika
from fastapi import FastAPI, HTTPException, Body
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to RabbitMQ-FastAPI"}


@app.post("/hello/{message}")
async def post_message(message: str = Body(..., example="Hello World!")):
    try:
        connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq-0.rabbitmq-headless.keda.svc.cluster.local", port=5672, 
        credentials=pika.PlainCredentials("user", "PASSWORD")))
            
        channel = connection.channel()
        #channel.exchange_declare(exchange='logs', exchange_type='direct')

        #severity = ['hello', 'message', 'error']
        #messages = ['Hafizur', 'message', 'error']

        channel.queue_declare(queue='hello')

        channel.basic_publish(exchange='', routing_key='hello', body=message)

        await connection.close()

        return "Successfully sended message do queue"

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Error when trying to send message to queue",
        )
        


