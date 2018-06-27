import pika
import csv

    


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello', durable=False)

with open ('demo.csv')as csvfile:
    data = csv.reader(csvfile)
    for row in data:  
        channel.basic_publish(exchange='',
         routing_key= 'hello', 
         body=str(row))
                        
print(" [x] Sending a Greeting!'")
connection.close()
