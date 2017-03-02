This is a project to creating a docker container on a raspberry pi. The goal is to create a Flask application in a docker container which can then be called from outside the raspberrypi to get the temperature value.

This is based heavily on [bmwshop's sensehat](https://github.com/bmwshop/sensehat) project where he made it as small as possible. I created the basic Flask program and more or less took his Dockerfile and added pip and Flask.

To use, 

docker build -t sense .

docker run --privileged -dp 5000:5000 sense

And then open a browser to the address of the docker container.
