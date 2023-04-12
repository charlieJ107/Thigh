sudo apt update
sudo apt install git vim htop build-essential default-jdk default-jre curl openssh-server -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh --mirror Aliyun
dockerd-rootless-setuptool.sh install