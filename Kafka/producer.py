import json
import time
from confluent_kafka import Producer

KAFKA_BROKER="localhost:9092"

TOPIC="server_metrics"

producer=Producer({
    "bootstrap.servers":KAFKA_BROKER
})

messages=[
    {"server_id": "server01", "cpu_usage": 82, "memory_usage": 65},
    {"server_id": "server02", "cpu_usage": 45, "memory_usage": 62},
    {"server_id": "server03", "cpu_usage": 91, "memory_usage": 70},
    {"server_id": "server04", "cpu_usage": 60, "memory_usage": 55},
    {"server_id": "server05", "cpu_usage": 78, "memory_usage": 61},
    {"server_id": "server06", "cpu_usage": 88, "memory_usage": 68},
    {"server_id": "server07", "cpu_usage": 52, "memory_usage": 58},
    {"server_id": "server08", "cpu_usage": 95, "memory_usage": 72},
    {"server_id": "server09", "cpu_usage": 67, "memory_usage": 64},
    {"server_id": "server10", "cpu_usage": 49, "memory_usage": 60},
]

for message in messages:
    producer.produce(
        TOPIC,
        value=json.dumps(message).encode("utf-8")
    )
    print(f"Sent:{message}")

    producer.poll(0)
    time.sleep(0.5)

producer.flush()
print("All messages sent successfully.")