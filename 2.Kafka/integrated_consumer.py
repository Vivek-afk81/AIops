from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "server_metrics",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="aiops-integrated",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)

anomaly_count = 0
messages_processed = 0
total_messages = 10

print("Waiting for messages...\n")

for message in consumer:

    data = message.value

    server = data["server_id"]
    cpu = data["cpu_usage"]

    print(f"Message received: {server} | CPU: {cpu}%")

    if cpu > 80:
        anomaly_count += 1
        print("ALERT: High CPU detected")
    else:
        print("Normal")

    messages_processed += 1

    if messages_processed == total_messages:
        break

consumer.close()

print(f"\nTotal anomalies detected: {anomaly_count}")