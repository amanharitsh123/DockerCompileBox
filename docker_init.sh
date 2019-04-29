set -x
# remove any previous container
sudo docker rm `sudo docker inspect --format="{{.Id}}" securo`
# Build Docker Image

#var="192.168.200.1"
#echo ${var%.*}
#
#192.168.200

path_of_file=`realpath "$0"`
path_of_file=${path_of_file%/*}


sudo docker build --tag=securo .
# Running Docker container with output folder mounted
sudo docker run --name=securo -d -v $path_of_file/output:/output securo
# Remove Docker Container
# sudo docker rm `sudo docker inspect --format="{{.Id}}" securo` 
