#!/bin/bash
cd kafka
bin/zookeeper-server-start.sh config/zookeeper.properties &> /dev/null &
bin/kafka-server-start.sh config/server.properties &> /dev/null &
#sudo service ssh start
