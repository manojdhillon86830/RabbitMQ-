
import pika, time

# Establish a connection with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare a durable queue
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

# Define a callback function
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.')) 
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge message


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)


channel.start_consuming()  

