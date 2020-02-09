import sys, traceback
import socket
import pickle
import os
import random
import copy
import pandas as pd
import re
import copy
import threading as th
from CodeGenClient import *

def main():

	while True:
		cmd = str(input("Enter your command: ")).lower()
		cmd_param = re.split("\s",cmd)
		cmd_name = cmd_param[0]
		
		if cmd_name == "get_items_list":
			result = get_items_list()
			try:
				if result == -1:
					print("Invalid arguments")
					continue
			except:
				continue		
			for item, value in result.items():
				print(item," : ",value)

		elif cmd_name == "buy":
			result = buy(product_name = cmd_param[1])
			if result==0:
				print("Item Unavailable")
			if result == -1:
				print("Invalid arguments")

		elif cmd_name == "help":
			print("Command list\n1.get_items_list\n2.buy [product_name]")

		else:
			print("Invalid Command")
		
			
if __name__ == '__main__':
	main()