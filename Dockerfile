FROM python:2.7.12
#FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY cert.pem /etc/pki/tls/cert.pem

COPY KafkaProducer.py . 

CMD ["python","KafkaProducer.py"]
