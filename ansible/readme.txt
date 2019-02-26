docker build -t gh/ansible .
docker run -it -d --rm --name ansible -v $(pwd):/home/ubuntu/ansible gh/ansible
docker exec -it ansible bash
