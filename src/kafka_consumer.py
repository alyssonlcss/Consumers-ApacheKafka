from confluent_kafka import Consumer, KafkaException

class KafkaConsumer:
    def __init__(self, group_id, topics, bootstrap_servers, auto_offset_reset):
        self.group_id = group_id
        self.topics = topics
        self.bootstrap_servers = bootstrap_servers
        self.auto_offset_reset = auto_offset_reset
        self.consumer = self.create_consumer()

    def create_consumer(self):
        config = {
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': self.group_id,
            'auto.offset.reset': self.auto_offset_reset
        }
        consumer = Consumer(config)
        consumer.subscribe(self.topics)
        return consumer

    def consume_messages(self, num_messages):
        for _ in range(num_messages):
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    print(f"Erro: {msg.error()}")
                    break
            print(f"Consumer: {self.group_id}, Topic: {msg.topic()}, "
                  f"Partition: {msg.partition()}, Offset: {msg.offset()}, "
                  f"Value: {msg.value().decode('utf-8')}")

    def close_consumer(self):
        self.consumer.close()
