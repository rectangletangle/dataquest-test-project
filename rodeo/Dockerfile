
FROM ubuntu:14.04

RUN apt-get update && apt-get -y upgrade

# `python2.7-dev` installs the C-Python header files for rodeo's dependencies
RUN apt-get install -y python python2.7-dev python-pip

COPY ./ /home/

RUN mkdir /home/data/

RUN pip install -r /home/requirements.txt

EXPOSE 5000

# Run rodeo
CMD python /home/app.py
