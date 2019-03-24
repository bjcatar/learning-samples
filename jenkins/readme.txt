
### https://github.com/jenkinsci/docker

# Run Jenkins, mapped to local vol to keep data
docker run --name jenkins --rm -d -v $(pwd)/jenkins_home:/var/jenkins_home -p 8082:8080 -p 50000:50000 jenkins/jenkins:lts

# Build my own Jenkins
docker build -t gh/jenkins .

# Create local directory for later use as volume
mkdir jenkins_home

# Set numbers of executors
cat > executors.groovy <<EOF
import jenkins.model.*
Jenkins.instance.setNumExecutors(5)
EOF

# Configure logging
cat > jenkins_home/log.properties <<EOF
handlers=java.util.logging.ConsoleHandler
jenkins.level=FINEST
java.util.logging.ConsoleHandler.level=FINEST
EOF

# Run My Jenkins
docker run --name jenkins --rm -d --env JAVA_OPTS="-Djava.util.logging.config.file=/var/jenkins_home/log.properties" -v $(pwd)/jenkins_home:/var/jenkins_home -p 8082:8080 -p 50000:50000 gh/jenkins

# Get initial admin password
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
