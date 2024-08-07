#! /bin/bash
sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo yum install git -y
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo git clone https://github.com/rmsghost/projetct_stackobservability.git /home/app/projetct_stackobservability
sudo docker-compose -f /home/app/projetct_stackobservability/compose.yaml up -d --build
sudo cp /home/app/projetct_stackobservability/daemon.json /etc/docker/daemon.json
sudo systemctl start docker