docker run -d --hostname my-rabbit --name my-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3
echo "Use 'docker start my-rabbit' to start service"
