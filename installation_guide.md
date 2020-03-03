Open a terminal window. If you don't know how to open a terminal window on Ubuntu.

Type commands below into the terminal window to install docker. More instructions can be found here.



sudo apt-get update
sudo apt-get install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io


Log out and log back in (or reboot) so that your group membership is re-evaluated. You can type groups command in a terminal window after that and check if docker group is in its output.


Install docker-compose (1.19.0 or newer). Compose is a tool for defining and running multi-container docker applications.

sudo apt-get install -y python3-pip
sudo python3 -m pip install docker-compose
Clone CVAT source code from the GitHub repository.

sudo apt-get install -y git
git clone https://github.com/opencv/cvat
cd cvat
replace the original docker compose yml file with <a href="https://github.com/Sreedeepthinukala/CVAT/blob/master/docker-compose.yml">docker-compose-yml</a></p>. Under Volumes near device, give the path of the images folder.

Add <a href="https://github.com/Sreedeepthinukala/CVAT/blob/master/docker-compose.override.yml">docker-override.yml</a></p>


Build docker images by default. It will take some time to download public docker image ubuntu:16.04 and install all necessary ubuntu packages to run CVAT server.

docker-compose build


