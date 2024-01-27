# mio-sdp-repo


# To run the image on the respbarry follow these steps:
 1. Follow the instructions for the docker installation on Raspberry https://docs.docker.com/engine/install/raspberry-pi-os/
 2. Use this command to run the image: docker run -it --rm -v /usr:/usr -e LD_LIBRARY_PATH=/usr/lib --device /dev/vchiq debian:stretch /usr/bin/vcgencmd flask-mio