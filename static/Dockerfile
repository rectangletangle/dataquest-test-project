
FROM ubuntu:14.04

RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y python python2.7-dev python-pip

COPY ./ /home/
RUN mkdir -p /home/public/static/

RUN pip install -r /home/requirements.txt

RUN cp -R $(python /home/getstatic.py) /home/public/

EXPOSE 8000

WORKDIR /home/public/

# Serve static files
# Using this in lieu of a production grade static content server.
CMD python /home/srv.py 8000
