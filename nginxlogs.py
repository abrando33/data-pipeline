import json
import time
from confluent_kafka import Producer

kafka_conf = {
    'bootstrap.servers': 'localhost:29092',  
    'client.id': 'json-producer'
}

producer = Producer(kafka_conf)

def delivery_report(err, msg):
    """ Delivery report callback called once for each message produced """
    if err is not None:
        print(f"Delivery failed for message {msg.key()}: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


json_file_path = 'C:/Users/alecm/Projects/nginx.log'
kafka_topic = 'nginx2'

def send_json_logs_to_kafka(file_path, topic):
    with open(file_path, 'r') as json_file:
        for line in json_file:
            try:
                log_entry = json.loads(line.strip())  
                log_entry_str = json.dumps(log_entry)  
                producer.produce(topic, value=log_entry_str, callback=delivery_report)
                producer.poll(0)  
                
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON line: {line.strip()}\nError: {e}")

    producer.flush()  

if __name__ == "__main__":
    send_json_logs_to_kafka(json_file_path, kafka_topic)
