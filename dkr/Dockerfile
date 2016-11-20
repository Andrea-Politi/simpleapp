FROM ubuntu:16.04


# Install required packages 

RUN apt-get update && apt-get install -y \
	git \
	sudo \
	python \
	python-dev \
	build-essential \
	python-setuptools \
	python-mysqldb \
	nginx \
	curl \
  && rm -rf /var/lib/apt/lists/*

# install pip
RUN curl -sS https://bootstrap.pypa.io/get-pip.py|python
ADD requirements.txt .
RUN pip install -r requirements.txt

# add the code
ADD sampleapp/ /sample_app
COPY nginx.conf /etc/nginx/sites-available/default

# set env variables
WORKDIR /sample_app
RUN ln -s /usr/lib/python2.7 /sample_app/lib

# start uwsgi and nginx
CMD sh starts.sh
