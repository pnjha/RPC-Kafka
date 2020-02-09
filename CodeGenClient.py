from connection_manager import *
server_IP = '127.0.0.1'
server_port = str(9092)
client_IP = '127.0.0.1'
client_port = str(5000)
def buy(**args):
	request = {}
	request['type'] = 'buy'
	request['param_value'] = args
	client_id = client_IP+':'+client_port
	server_id = server_IP+':'+server_port
	request['id'] = client_id
	produce_topic('buy',server_id,request,server_id)
	reply = consume_topic('buy',client_id,server_id)
	return reply['response_value']
def get_items_list(**args):
	request = {}
	request['type'] = 'get_items_list'
	request['param_value'] = args
	client_id = client_IP+':'+client_port
	server_id = server_IP+':'+server_port
	request['id'] = client_id
	produce_topic('get_items_list',server_id,request,server_id)
	reply = consume_topic('get_items_list',client_id,server_id)
	return reply['response_value']