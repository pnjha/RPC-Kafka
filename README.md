<strong>To run zookepper</strong><br>
bin/zookeeper-server-start.sh config/zookeeper.properties<br>

<strong>To run Kafka</strong><br>
bin/kafka-server-start.sh config/server.properties<br>

<strong>To run server</strong><br>
python3 [filename][server IP][server port]

<strong>To run script</strong><br>
python3 script.py [client IP][client port][server ip][server port]

<strong>To run client</strong><br>
python3 client.py

<strong>Commands at Client's end</strong><br>
get_items_list -> to get list of all items along with the quantity present<br>
buy -> to buy a particular item
help -> to get list of commands