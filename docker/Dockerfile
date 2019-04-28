############################################################
# Dockerfile to build sandbox for executing user code
# Based on Ubuntu
############################################################

FROM ubuntu
# MAINTAINER ASAD MEMON, OSMAN ALI

# Update the repository sources list
# RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install apt-utils -y
RUN apt-get upgrade -y

#Install all the languages/compilers we are supporting.
RUN apt-get install -y gcc
RUN apt-get install -y g++
# RUN apt-get install -y php5-cli
# RUN apt-get install -y ruby
RUN apt-get install -y python
# RUN apt-get install -y curl
# RUN mkdir -p /opt/rust && \
#     curl https://sh.rustup.rs -sSf | HOME=/opt/rust sh -s -- --no-modify-path -y && \
#     chmod -R 777 /opt/rust

# RUN apt-get install -y sudo
# RUN apt-get install -y bc
RUN mkdir /input
RUN mkdir /output
WORKDIR /input
COPY ./input /input
RUN bash -i
# RUN python *.py > /output/out.txt
CMD python *.py >/output/ans.txt
# RUN echo "mysql ALL = NOPASSWD: /usr/sbin/service mysql start" | cat >> /etc/sudoers

