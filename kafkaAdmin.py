from kafka.admin import KafkaAdminClient, NewTopic
import sys
from kafka import KafkaProducer
from kafka import KafkaConsumer
def createTopic(TopicId, Adminclient):
   topic_list = []
   topic_list.append(NewTopic(name=TopicId, num_partitions=1, replication_factor=1))
   Adminclient.create_topics(new_topics=topic_list, validate_only=False)
def createAdmin(client, server):
   admin_client = KafkaAdminClient(bootstrap_servers=server, client_id=client)
   return admin_client
def deleteTopic(topicId,adminclient):
   adminclient.delete_topics(topicId)
def listTopic(adminclient):
   return adminclient.list_topics()
def push(topic,msg):
   producer = KafkaProducer(bootstrap_servers='localhost:9092')
   producer.send(topic, bytes(msg, encoding='utf-8'))
def get(topic):
   consumer = KafkaConsumer(topic)
   for message in consumer:
      print (message)
if __name__ == '__main__':
   #print (sys.argv)
   server=None
   server = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test1')
   if len(sys.argv) < 3:
      print(" the arguments (3 arguments) should be entered as the following struture: [server, operation(create,delete, list), topicID (in case of delete- or create, and all for list ]")
   else:
      server2=(sys.argv[1],'client')
      if sys.argv[2]=="create":
         createTopic(sys.argv[3],server)
      elif sys.argv[2]=="delete":
         deleteTopic(sys.argv[3],server)
      elif sys.argv[2]=="list":
         print(listTopic(server))
      elif sys.argv[2]=="push":
         push(sys.argv[3], sys.argv[4])
      elif sys.argv[2]=="get":
         get(sys.argv[3])
      else:
         print("Please use these arguments: [server, operation(create,delete, list), topicID (in case of delete- or create, and all for list ]")

