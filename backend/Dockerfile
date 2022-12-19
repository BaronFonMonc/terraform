# start by pulling the python image
#FROM python:3.8-alpine
FROM python:3.7

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
RUN apt update
RUN apt-get install -y default-libmysqlclient-dev
RUN pip3 install mysqlclient

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["main.py" ]