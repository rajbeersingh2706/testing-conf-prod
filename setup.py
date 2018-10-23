import sys
from setuptools import setup

setup(name="testing-conf-producer",
      version="0.0.1",
      maintainer="RAJBEER",
      description="Kafka Producer",
      platforms=["any"],
      #packages=["", ""],
      entry_points={
          "console_scripts": [
            "kafka_produer = KafkaProducer:main"
          ]
      }
)
