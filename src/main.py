from consumer_manager import ConsumerManager
from configs import config_loader


def main(): 
    # Carregar configurações do arquivo appsettings.json
    config = config_loader.load_config('appsettings.json')

    # Obter configurações específicas para Kafka
    kafka_config = config.get('kafka_config', {})
    topics = config.get('topics', [])
    bootstrap_servers = kafka_config.get('bootstrap_servers', 'default_bootstrap_servers')
    auto_offset_reset = kafka_config.get('auto_offset_reset', 'default_auto_offset_reset')
    num_messages = 1

    # Obter group_ids do arquivo de configuração
    group_id1 = config.get('group_ids', {}).get('group_id1', 'default_group_id1')
    group_id2 = config.get('group_ids', {}).get('group_id2', 'default_group_id2')


    manager1 = ConsumerManager(group_id1, topics, bootstrap_servers , auto_offset_reset, num_messages)
    manager2 = ConsumerManager(group_id2, topics, bootstrap_servers, auto_offset_reset, num_messages)

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
