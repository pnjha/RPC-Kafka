from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('my_topic',group_id='my_group',bootstrap_servers='127.0.0.1:9092',key_deserializer=lambda m: json.loads(m.decode('utf-8')),value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
	print("here: ",message)
	d = message.value
	print(d)
    