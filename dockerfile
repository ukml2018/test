from alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip 
	
WORKDIR /app
COPY . /app

RUN apk add gcc && \
    rm -rf /var/lib/apt/lists/*
	
RUN apk add libffi-dev

RUN apk add linux-headers

RUN apk add libc-dev

RUN apk --update add mysql-client

RUN apk add --no-cache mariadb-dev

RUN apk add --no-cache libzmq zeromq-dev openssl-dev build-base  g++

RUN pip3 --no-cache-dir install -r requirements_docker.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["connect_mysql.py"]

