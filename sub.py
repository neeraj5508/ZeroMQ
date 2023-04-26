import zmq

class Subscriber:
    def __init__(self, channels):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)

        for channel in channels:
            self.socket.connect(channel)

    def subscribe(self, channel):
        self.socket.setsockopt_string(zmq.SUBSCRIBE, channel)

    def receive(self):
        message = self.socket.recv_string()
        channel, message = message.split(' ', 1)
        return channel, message

if __name__ == '__main__':
    channels = ["tcp://localhost:5555"]
    subscriber = Subscriber(channels)
    subscriber.subscribe("channel1")
    subscriber.subscribe("channel2")

    while True:
        channel, message = subscriber.receive()
        print(f"Received: {channel}: {message}")
