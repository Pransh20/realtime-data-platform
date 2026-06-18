from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

products = [
    "Laptop",
    "Phone",
    "Tablet",
    "Headphones"
]

while True:

    event = {
        "user_id": random.randint(1, 1000),
        "product": random.choice(products),
        "amount": random.randint(100, 5000)
    }

    producer.send("orders", event)

    print(event)

    time.sleep(1)
