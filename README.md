# Kafka server  on Docker.

Following this steps you can build and use the image to create a kafka  containers.


## Creating the container

To run and create a container execute the next command:

     $ docker run -it --name <container-name> -p 9092:9092  --hostname <your-hostname> kafka

Change **container-name** by your favorite name and set **your-hostname** with by your ip or name machine. You can use **localhost** as your-hostname

When you run the container, at the entrypoint you use the docker-entrypoint.sh shell that creates and starts the hadoop environment.

You should get the following prompt:

     kafka@localhost:~$ 
