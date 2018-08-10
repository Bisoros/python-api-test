import pika

class RpcServer():
    host = 'localhost'
    func = None

    def on_request(self, ch, method, props, body):

        print(" [.] Received: %s" % body)
        response = self.func(body)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id = \
                                                             props.correlation_id),
                         body=str(response))
        ch.basic_ack(delivery_tag = method.delivery_tag)

    def __init__(self, queue, func):
        self.func = func
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))

        channel = connection.channel()

        channel.queue_declare(queue=queue)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(self.on_request, queue=queue)

        print(" [x] Awaiting RPC requests")
        channel.start_consuming()

if __name__ == '__main__':
    rpc = RpcServer('numbers', lambda x : 'respone')
