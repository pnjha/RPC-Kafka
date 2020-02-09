import os
import sys
import json
import pickle
import threading as th
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from Server import Server as Server

def produce_topic(topic_name,receiver_id,value,kafka_id):
    producer = KafkaProducer(retries=5,bootstrap_servers=kafka_id,key_serializer=lambda m: json.dumps(m).encode('utf-8'),value_serializer=lambda m: json.dumps(m).encode('utf-8'))
    producer.send(topic_name,key=receiver_id,value=value)
    producer.flush()
    print(value)

def consume_topic(function_name,server_id):
    consumer = KafkaConsumer(function_name,group_id=server_id,bootstrap_servers=server_id,key_deserializer=lambda m: json.loads(m.decode('utf-8')),value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    server_impl_obj = Server()
    for message in consumer:
        if message.key == server_id:
            client_id = message.value["id"]
            request = message.value["param_value"]
            function = getattr(server_impl_obj,function_name)
            val = function(**request)
            reply = {}
            reply['response_value'] = val
            produce_topic(function_name,client_id,reply,server_id)

def main(server_id,server_IP,server_port):
    
    temp_funtions_list = dir(Server)
    functions_list = []
    for item in temp_funtions_list:
        if "__" not in item:
            functions_list.append(item)
    reply = {}
    reply["functions_list"] = functions_list
    produce_topic("functions_list","default",reply,server_id)

    for function_name in functions_list:            
        th.Thread(target=consume_topic, args=(function_name,server_id)).start()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ("Invalid argument format\n Correct usage:python3 [filename][IP Address][Port Number]")
        exit()
    server_IP = str(sys.argv[1])
    server_port = str(sys.argv[2])
    server_id = server_IP+":"+server_port
    main(server_id,server_IP,server_port)