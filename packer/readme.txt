https://hub.docker.com/r/hashicorp/packer
https://www.packer.io/intro/getting-started/build-image.html

# validate template
# packer validate example.json
docker run -i -t -v $(pwd):/go/src/app hashicorp/packer:light validate /go/src/app/example.json

docker run -i -t -v $(pwd):/go/src/app hashicorp/packer:light build -var-file=/go/src/app/variables.json /go/src/app/example.json 
