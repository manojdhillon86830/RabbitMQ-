

#---------------------SEND MESSAGE TO FIRST RECEIVER WHO IS FREE. IF FIRST RECEIVER IS NOT RUNNING SEND MESSAGE TO SECOND IF SECOND IS ALSO BUSY SEND IT TO THIRD--------------------------------#


import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
message = ' '.join(sys.argv[1:]) or "Hello World"

channel.basic_publish(exchange='', routing_key='task_queue', body=message, properties=pika.BasicProperties(delivery_mode=2))

print(" [x] Successfully Sent! %r" % message)
connection.close()

# differnce compare to hello-world
        #  durable=True
        # properties=pika.BasicProperties(delivery_mode=2)