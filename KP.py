from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092',key_serializer=lambda m: json.dumps(m).encode('utf-8'),value_serializer=lambda m: json.dumps(m).encode('utf-8'))
producer.send('my_topic',key="hello",value={'id': '1','msg':'hello'})
producer.flush()