import sys
import pickle
import os
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError

def get_function_body(function_name):
	return "\ndef "+ function_name +"(**args):\n\trequest = {}\n\trequest['type'] = "+ "'" + function_name + "'" +"\n\trequest['param_value'] = args\n\tclient_id = client_IP+':'+client_port\n\tserver_id = server_IP+':'+server_port\n\trequest['id'] = client_id\n\tproduce_topic("+"'"+function_name+"'"+",server_id,request,server_id)\n\treply = consume_topic("+"'"+function_name+"'"+",client_id,server_id)\n\treturn reply['response_value']"

def create_interface(server_IP,server_port,client_IP,client_port,function_list):
	f = open("CodeGenClient.py", "w")	
	f.write("from connection_manager import *\nserver_IP = "+"'"+server_IP+"'"+"\nserver_port = str("+server_port+")")
	f.write("\nclient_IP = "+"'"+client_IP+"'"+"\nclient_port = str("+client_port+")")
	for item in function_list:
		function_body = get_function_body(item)
		f.write(function_body)
	f.close()

def consume_topic(function_name,key,client_id,server_id):
    consumer = KafkaConsumer(function_name,group_id=client_id,bootstrap_servers=server_id,key_deserializer=lambda m: json.loads(m.decode('utf-8')),value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    for message in consumer:
    	if message.key == key:
            return message.value["functions_list"]

def code_generator(client_IP,client_port,server_IP,server_port):
	server_id = server_IP+":"+server_port
	client_id = client_IP+":"+client_port
	functions_list = consume_topic("functions_list","default",client_id,server_id)
	create_interface(server_IP,server_port,client_IP,client_port,functions_list)

if __name__ == '__main__':

	if len(sys.argv) != 5:
		print("Invalid Input Format\n python3 [FileName][Client IP][Client Port][Server IP][Server Port]")
		exit()
	client_IP = str(sys.argv[1])
	client_port = str(sys.argv[2])
	server_IP = str(sys.argv[3])
	server_port = str(sys.argv[4])
	code_generator(client_IP,client_port,server_IP,server_port)
