from kafka import KafkaProducer

KAFKA_TOPIC = 'demo'
#producer = KafkaProducer(bootstrap_servers=KAFKA_BROKERS)

producer = KafkaProducer(bootstrap_servers = 'pkc-e8xq4.us-central1.gcp.confluent.cloud:9092',
                         sasl_plain_username ='BLPGYC252ZPQX6VH',
                         sasl_plain_password='vsHuX1ttck4WwKFvSM/IPdnjRPJ1zyTJ5978edsCHKU5A7bhYG1SQEHZsR5pmgzs',
                         #ssl_endpoint_identification_algorithm='https',
                         sasl_mechanism='PLAIN',
                         request_timeout_ms=2000,
                         retry_backoff_ms=500,
                         security_protocol='SASL_SSL',
			 ssl_cafile ='/etc/pki/tls/cert.pem',
                         api_version=(0,10,0),
			 api_version_auto_timeout_ms=0	
                        )

messages = [b'hello kafka 1', b'I am sending 2', b'3 test messages',b'4the message from kafaka1','5th message ']

# Send the messages
for m in messages:
    producer.send(KAFKA_TOPIC, m)

producer.flush()
print("message setn successfully")
