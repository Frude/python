# -*- coding:UTF-8 -*-
# import pika
# # 导入库
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# # 设置一个新连接，连接到本地的 RabbitMQ 服务端。
# channel = connection.channel()
# # 注册到 books 队列
# channel.queue_declare(queue='books')
# channel.basic_publish(exchange='', routing_key='books', body='Whats up')
# # 发送消息 body
# connection.close()
# #

import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='books')


def callback(ch, method, properties, body):
    print body

channel.basic_consume(callback, queue='books', no_ack=True)
# 注册回调函数，当有消息取出时，程序调用 callback 函数，其中 body 就是取出的消息。
channel.start_consuming()