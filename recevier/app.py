import pika
from fastapi import FastAPI, HTTPException, Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to RabbitMQ-FastAPI"}


@app.get("/message")
async def post_message():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
            )
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', exchange_type='direct')
        result = channel.queue_declare(exclusive=True, queue="")
        queue_name = result.method.queue
        channel.queue_bind(exchange='logs', queue=queue_name, routing_key='hello')

        def callback(ch, method, properties, body):
            print(" [x] %r:%r" % (method.routing_key, body))
        channel.basic_consume(on_message_callback=callback, queue=queue_name, auto_ack=True)
        await channel.start_consuming()

        return {"message": "Message received"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        

@app.get("/error")
async def post_message():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
            )
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', exchange_type='direct')
        result = channel.queue_declare(exclusive=True, queue="")
        queue_name = result.method.queue
        channel.queue_bind(exchange='logs', queue=queue_name, routing_key='error')

        def callback(ch, method, properties, body):
            print(" [x] %r:%r" % (method.routing_key, body))
        channel.basic_consume(on_message_callback=callback, queue=queue_name, auto_ack=True)
        await channel.start_consuming()

        return {"message": "Message received"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/hello")
async def post_message():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
            )
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', exchange_type='direct')
        result = channel.queue_declare(exclusive=True, queue="")
        queue_name = result.method.queue
        channel.queue_bind(exchange='logs', queue=queue_name, routing_key='hello')

        def callback(ch, method, properties, body):
            print(" [x] %r:%r" % (method.routing_key, body))
        channel.basic_consume(on_message_callback=callback, queue=queue_name, auto_ack=True)
        await channel.start_consuming()

        return {"message": "Message received"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
