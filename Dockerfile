FROM python:3.6-slim
ENV LANG=en_US.UTF-8

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt && \
	rm -rf /tmp/*
#RUN apt-get update && apt-get install -y  --no-install-recommends vi &&  rm -rf /var/lib/apt/lists/* && apt-get clean
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
COPY . /app

EXPOSE 8080

#COPY config /root/.kube/config

CMD python app.py