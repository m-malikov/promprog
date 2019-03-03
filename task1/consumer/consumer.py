import pika
import logging
import sys

conn_params = pika.ConnectionParameters('rabbitmq', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='numbers')

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(asctime)s - %(message)s")


def callback(ch, method, properties, body):
    logging.info("Recieved number {}".format(body.decode("utf-8")))


channel.basic_consume(callback, queue='numbers', no_ack=True)

while True:
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    except Exception:
        channel.stop_consuming()
        logging.exception("Exception occured")
