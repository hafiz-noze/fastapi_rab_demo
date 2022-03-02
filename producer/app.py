import pika
from fastapi import FastAPI, HTTPException, Body
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to RabbitMQ-FastAPI"}


@app.post("/hello")
async def post_message(message: str = Body(...)):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
            )
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', exchange_type='direct')

        severity = ['hello', 'message', 'error']
        messages = ['Hafizur', 'message', 'error']

        for i in range(10):
            randomNum = random.randint(0, len(severity)-1)
            message = random.choice(messages)
            routing_key = severity[randomNum]
            channel.basic_publish(exchange='logs', routing_key=routing_key, body=message)
            print(" [x] Sent %r:%r" % (routing_key, message))

        channel.exchange_delete(exchange='logs', if_unused=False)

        await connection.close()

        return "Successfully sended message do queue"

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Error when trying to send message to queue",
        )
        


