FROM ubuntu:16.04
RUN apt-get -y update
RUN apt-get -y install libffi-dev python3-pip libmysqlclient-dev
RUN mkdir /demoapp
WORKDIR /demoapp
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ADD . /demoapp
EXPOSE 8001
ENTRYPOINT ["python3"] 
CMD ["short.py"]
