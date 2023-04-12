wget https://mirrors.cloud.tencent.com/virtualbox/6.1.18/Oracle_VM_VirtualBox_Extension_Pack-6.1.18.vbox-extpackwget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
echo "deb [arch=amd64] https://mirrors.cloud.tencent.com/virtualbox/apt/ focal contrib" >> virtualbox.list
sudo mv virtualbox.list /etc/apt/sources.list.d/virtualbox.list
sudo apt update
sudo apt install virtualbox-6.1 -y
wget https://mirrors.cloud.tencent.com/ubuntu-releases/20.04/ubuntu-20.04.2-live-server-amd64.iso