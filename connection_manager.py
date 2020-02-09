import sys, traceback
import pickle
import os
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError

def produce_topic(topic_name,receiver_id,value,kafka_id):
    producer = KafkaProducer(retries=50,bootstrap_servers=kafka_id,key_serializer=lambda m: json.dumps(m).encode('utf-8'),value_serializer=lambda m: json.dumps(m).encode('utf-8'))
    producer.send(topic_name,key=receiver_id,value=value)
    producer.flush()

def consume_topic(function_name,client_id,server_id):
    consumer = KafkaConsumer(function_name,group_id=client_id,bootstrap_servers=server_id,key_deserializer=lambda m: json.loads(m.decode('utf-8')),value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    for message in consumer:
        if message.key == client_id:
            return message.value 