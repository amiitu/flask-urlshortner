FROM ubuntu:16.04
RUN apt-get -y update
RUN apt-get -y install libffi-dev python3-pip libmysqlclient-dev
RUN mkdir /demoapp
WORKDIR /demoapp
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ADD . /demoapp
ENV LC_ALL=C.UTF-8 
ENV LANG=C.UTF-8
#RUN flask db init
RUN flask db upgrade
EXPOSE 8001
ENTRYPOINT ["python3"] 
CMD ["run.py"]