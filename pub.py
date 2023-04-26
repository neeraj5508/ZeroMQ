import zmq
import time

class Publisher:
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)

    def publish(self, channel, message):
        self.socket.send_string(f"{channel} {message}")

if __name__ == '__main__':
    publisher = Publisher()
    publisher.socket.bind("tcp://*:5555")

    while True:
        message = "Hello, World!"
        publisher.publish("channel1", message)
        publisher.publish("channel2", message)
        time.sleep(1)
