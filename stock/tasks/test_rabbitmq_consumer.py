import pika


rabbitmq_host = '192.168.88.200'
rabbitmq_port = 32782
rabbitmq_vhost = 'stock_host'
rabbitmq_user = 'stock_user'
rabbitmq_pass = 'stock_pass'

credential = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host, rabbitmq_port, rabbitmq_vhost, credential))
channel = connection.channel()
channel.queue_declare(queue='balance')


def callback(ch, method, properties, body):
    print("接收到任务%s" % body)
    #ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume("balance",callback)

print("等待xin任务..")
channel.start_consuming()