import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=False)
print('[*] Waiting for messages. to exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" %body)
    print (" [x] Done")
    

channel.basic_consume(callback, queue='hello', no_ack=True)


channel.start_consuming()