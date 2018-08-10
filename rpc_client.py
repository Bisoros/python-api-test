import pika
import uuid

class RpcClient(object):
    host = 'localhost'
    queue = 'rpc_queue'

    def __init__(self, queue):
        self.queue = queue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, data):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue,
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(data))
        while self.response is None:
            self.connection.process_data_events()
        return self.response

if __name__ == '__main__':
    fibonacci_rpc = RpcClient('rpc_queue')

    var = "30" #input("Enter an integer: ")
    print(" [x] Requesting fib(" + var +")")
    response = fibonacci_rpc.call(int(var))
    print(" [.] Got %r" % response)

    '''
    # how it will work:
    rpc = RpcClient('queue name')
    return rpc.call(the_json)
    '''
