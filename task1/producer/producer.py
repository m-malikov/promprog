import pika
import random
import time
import logging
import sys

conn_params = pika.ConnectionParameters('rabbitmq', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='numbers')

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(asctime)s - %(message)s")

while True:
    number = random.randint(1, 10)
    logging.info("Sending number {}".format(number))

    channel.basic_publish(
        exchange='', routing_key='numbers', body=str(number))

    delay = random.randint(1, 10)

    time.sleep(delay)


connection.close()
