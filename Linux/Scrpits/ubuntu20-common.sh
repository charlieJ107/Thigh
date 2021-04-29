sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
wget https://raw.githubusercontent.com/charlieJ107/Thigh/main/Linux/config/ubuntu20.list -o /etc/apt/sources.list
sudo apt upgrade -y
sudo apt install git vim htop build-essential default-jdk default-jre curl openssh-server python3-dev python3-pip -y
pip3 config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple