import json
from confluent_kafka import Consumer


KAFKA_BROKER = "localhost:9092"
TOPIC = "server_metrics"


# Create Kafka consumer
consumer = Consumer({
    "bootstrap.servers": KAFKA_BROKER,
    "group.id": "aiops-monitor",
    "auto.offset.reset": "earliest"
})


# Subscribe to the topic
consumer.subscribe([TOPIC])


print("Consumer started...")
print("Listening for server metrics...\n")


try:
    while True:

        # Wait for a message
        message = consumer.poll(1.0)

        if message is None:
            continue

        if message.error():
            print(f"Consumer error: {message.error()}")
            continue

        # Convert JSON bytes → Python dictionary
        data = json.loads(message.value().decode("utf-8"))

        server_id = data["server_id"]
        cpu = data["cpu_usage"]
        memory = data["memory_usage"]

        print(
            f"Message received: {server_id} | "
            f"CPU: {cpu}% | Memory: {memory}%"
        )

        # AIOps anomaly rule
        if cpu > 80:
            print(f"ALERT: High CPU detected on {server_id}")
        else:
            print("Normal")
        print()
finally:
    consumer.close()