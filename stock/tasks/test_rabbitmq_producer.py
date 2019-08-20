import pika

rabbitmq_host = '192.168.88.200'
rabbitmq_port = 32782
rabbitmq_vhost = 'stock_host'
rabbitmq_user = 'stock_user'
rabbitmq_pass = 'stock_pass'
credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host, rabbitmq_port, rabbitmq_vhost, credentials))
channel = connection.channel()
channel.exchange_declare(exchange='hello-world',
                         exchange_type='direct',
                         durable=True,
                         auto_delete=False,)
channel.queue_declare(queue='balance')
msg_props = pika.BasicProperties()
msg_props.content_type = 'text/plain'
for i in range(1000000):
    channel.basic_publish(exchange='hello-world',
                      routing_key = 'balance',
                      body='Heloo' + str(i),
                      properties = msg_props)
connection.close()
