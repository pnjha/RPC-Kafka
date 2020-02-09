from connection_manager import *
server_Ip = 127.0.0.1
server_port = 5000
client_Ip = 127.0.0.1
client_port = 8132
def buy(**args):
	request = {}
	request['type'] = 'buy'
	request['param_value'] = args
	send_to_server(request,client_IP,client_port,server_IP,server_port)
	reply = receive_from_server(client_IP,client_port,server_IP,server_port)
	return reply['response_value']
def get_items_list(**args):
	request = {}
	request['type'] = 'get_items_list'
	request['param_value'] = args
	send_to_server(request,client_IP,client_port,server_IP,server_port)
	reply = receive_from_server(client_IP,client_port,server_IP,server_port)
	return reply['response_value']
def products(**args):
	request = {}
	request['type'] = 'products'
	request['param_value'] = args
	send_to_server(request,client_IP,client_port,server_IP,server_port)
	reply = receive_from_server(client_IP,client_port,server_IP,server_port)
	return reply['response_value']