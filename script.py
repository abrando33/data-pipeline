import requests
import time
from kafka import KafkaProducer 

producer = KafkaProducer(bootstrap_servers='localhost:29092')

producer.send('nginx2',b'"17/May/2015:08:05:32 +0000", "remote_ip": "93.180.71.3", "remote_user": "-", "request": "GET /downloads/product_1 HTTP/1.1", "response": 304, "bytes": 0, "referrer": "-", "agent": "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"')
producer.flush()
