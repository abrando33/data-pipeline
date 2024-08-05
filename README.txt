The following is an overview of my data pipeline project

The pipeline consists of five docker containers: Kafka, Zookeeper, Elasticsearch, Kibana and Logstash.

There is a sixth container, init-kafka that creates the desired topics and then exits.

I created several topics to test out my pipeline because I wanted to pull JSON from the nginx logs file as well as a remote API.

I did this to demonstrate the routing in logstash from two kafka topics to two ES indices.

To initially build containers from the images in the docker-compose.yml run: docker compose build --no-cache

To start the containers run docker compose up

To monitor the containers, check the status on docker desktop and monitor logs

To stop the containers run docker compose down

I have provided two python producers that both send JSON objects to their respective kafka topic

One script, NewsScript.py, pulls news stories from an API and sends the logs to the 'news' kafka topic.
Logstash is subscribed to the kafka topic but for these documents no filtering is applied in logstash. 
From logstash, the articles are sent to the 'news' index in ElasticSearch.

The second script, nginxlogs.py, reads the logs from the filepath, sends the JSON to a kafka topic. Logstash is subscribed to the 'nginx2' topic.
Filtering is applied to these logs in logstash and from there they are sent to ElasticSearch. I have defined a short mapping for this index in ES in order
to assign a geo-point field type to the geoip field produced by the logstash filter. I did this to build a map visualization in Kibana as part of the dashboard.

I have added two screenshots as well that show the resulting nginx logs document structure in ES as well as a sample dashboard I constructed using an index pattern for that index.

