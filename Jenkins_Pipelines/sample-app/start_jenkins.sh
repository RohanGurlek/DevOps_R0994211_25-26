#!/bin/bash

docker run -d --rm -u root -p 8080:8080 -v jenkins-data:/var/jenkins_home -v $(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home --name jenkins_server jenkins/jenkins:lts

#get jenkins admin pass
docker exec -it jenkins_server /bin/bash
#as root inside container
cat /var/jenkins_home/secrets/initialAdminPassword
exit
echo "password above is your login for Jenkins"