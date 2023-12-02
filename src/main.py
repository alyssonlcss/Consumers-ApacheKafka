from consumer_manager import ConsumerManager

def main():
    topics = ['seu_topico']
    group_id1 = 'grupo_consumidor_1'
    group_id2 = 'grupo_consumidor_2'
    num_messages = 1

    manager1 = ConsumerManager(group_id1, topics, num_messages)
    manager2 = ConsumerManager(group_id2, topics, num_messages)

    try:
        manager1.start_consumer()
        manager2.start_consumer()

        manager1.join_consumer()
        manager2.join_consumer()

    except KeyboardInterrupt:
        pass
    finally:
        manager1.close_consumer()
        manager2.close_consumer()

if __name__ == "__main__":
    main()
