# specifiy the image's OS
FROM ubuntu:20.04
MAINTAINER Wissem Inoubli (inoubliwissem@gmail.com)
# install the required softwares (JDK, openssh, wget)

RUN apt-get update -y && apt-get install vim -y && apt-get install wget -y && apt-get install ssh -y && apt-get install openjdk-8-jdk -y && apt-get install sudo -y && apt-get install pip -y

# create a new user and add it as sudoer
RUN useradd -m kafka && echo "kafka:supergroup" | chpasswd && adduser kafka sudo && echo "kafka     ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && cd /usr/bin/ &&  ln -s python3 python
# set the workspace
WORKDIR /home/kafka



# switech to the created user

USER kafka

# download kafka and extract it


RUN wget -q https://dlcdn.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz && tar zxvf kafka_2.13-3.0.0.tgz && rm kafka_2.13-3.0.0.tgz


RUN mv kafka_2.13-3.0.0 kafka

COPY start.sh /home/kafka/
COPY kafkaAdmin.py /home/kafka/

#open the used ports
EXPOSE 9092 22
RUN pip install kafka-python

# start kafka and zookeeper 's services 
#ENTRYPOINT ["/home/kafka/start.sh"]
 
