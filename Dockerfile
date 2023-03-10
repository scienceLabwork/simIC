#Create a ubuntu base image with python 3 installed.
FROM python:3.8

FROM --platform=linux/amd64 ubuntu:22.04

#Set the working directory
WORKDIR /

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
# RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
# RUN /usr/local/bin/python -m pip install --upgrade pip

# TO GET OUTPUT IN DOCKER --progress=plain
# RUN python --version 

#Expose the required port
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]