# remove any previous container
sudo docker rm `sudo docker inspect --format="{{.Id}}" securo`
# Build Docker Image

sudo docker build --tag=securo .
# Running Docker container with output folder mounted
sudo docker run --name=securo -d -v /home/amanharitsh/Desktop/minor2/securo/output:/output securo
# Remove Docker Container
# sudo docker rm `sudo docker inspect --format="{{.Id}}" securo` 
