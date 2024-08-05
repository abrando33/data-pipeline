import requests
from kafka import KafkaProducer
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_API_URL = 'https://newsapi.org/v2/everything'
KAFKA_BROKER = 'localhost:29092'
KAFKA_TOPIC = 'news'
COUNTRY = 'us' 

def get_news(api_key, technology):
    params = {
        'q': technology,
        'apiKey': api_key
        
    }
    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code == 200:
        return response.json()['articles']
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return []

def send_to_kafka(producer, topic, news_articles):
    for article in news_articles:
        producer.send(topic, value=article)
        print(f"Sent to Kafka: {article['title']}")

def main():
   
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    while True:
        news_articles = get_news(NEWS_API_KEY, COUNTRY)

        send_to_kafka(producer, KAFKA_TOPIC, news_articles)
        time.sleep(5)

if __name__ == '__main__':
    main()
