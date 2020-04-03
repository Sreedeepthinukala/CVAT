Open a terminal window.

Type(you can copy paste all the commands) commands below into the terminal window to install docker. More instructions can be found here.



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


Replace the original docker compose yml file with <a href="https://github.com/Sreedeepthinukala/CVAT/blob/master/docker-compose.yml">docker-compose-yml</a></p>

Under Volumes near device, give the path of the images folder. If you are using the yolo v3 model specified here, git clone https://github.com/AntonMu/TrainYourOwnYOLO. Images should be in 3.DATA->Source_images_Training images and also the same images should be in 3.DATA->Source_images_Training images->vott-csv-export.

In the cvat folder, add <a href="https://github.com/Sreedeepthinukala/CVAT/blob/master/docker-compose.override.yml">docker-override.yml</a></p> 


Build docker images by default. It will take some time to download public docker image ubuntu:16.04 and install all necessary ubuntu packages to run CVAT server.

docker-compose build

Run docker containers. It will take some time to download public docker images like postgres:10.3-alpine, redis:4.0.5-alpine and create containers.

docker-compose up -d

You can register a user but by default it will not have rights even to view list of tasks. Thus you should create a superuser. A superuser can use an admin panel to assign correct groups to the user. Please use the command below:

docker exec -it cvat bash -ic 'python3 ~/manage.py createsuperuser'

Google Chrome is the only browser which is supported by CVAT. Go to localhost:8080. Type your login/password for the superuser on the login page and press the Login button.

Go to http://localhost:8080/api/swagger/. Under server, click GET server/share, click try it out. Place the images path there and execute. 200 ,eans ran successfully.

To see if the images are shared successfully, follow this( create new task-> connected file share -> root).

Once all the images are ready, go to TrainYourOwnYOLO_master add <a href="https://github.com/Sreedeepthinukala/CVAT/blob/master/xml_to_csv.py">xmltocsv.py</a></p> and <a href="https://github.com/Sreedeepthinukala/CVAT/blob/master/cvat_automation.py">automation.py</a></p> in the 1.Image_annotation folder.

Download <a href="https://github.com/Sreedeepthinukala/CVAT/blob/master/job.sh">automation.sh(job.sh is the file name)</a></p> and run ./job.sh in the terminal.(Note: you have to update the virtual environment name. job.sh has my environment name)

Note: If you give less than 90 images and run it, it would throw and error "KeyError: 'val_loss'". So please make sure to give more than 90 images. More images for training would increase accuracy.








