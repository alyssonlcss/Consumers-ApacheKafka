import threading
from kafka_consumer import KafkaConsumer

class ConsumerManager:
    def __init__(self, group_id, topics, bootstrap_servers, auto_offset_reset, num_messages):
        self.group_id = group_id
        self.topics = topics
        self.bootstrap_servers = bootstrap_servers
        self.auto_offset_reset = auto_offset_reset
        self.num_messages = num_messages
        self.consumer = KafkaConsumer(self.group_id, self.topics, self.bootstrap_servers, self.auto_offset_reset)
        self.thread = threading.Thread(target=self.consume_in_thread)

    def consume_in_thread(self):
        try:
            while True:
                self.consumer.consume_messages(self.num_messages)
        except KeyboardInterrupt:
            pass

    def start_consumer(self):
        self.thread.start()

    def join_consumer(self):
        self.thread.join()

    def close_consumer(self):
        self.consumer.close_consumer()
