import pandas as pd
import matplotlib.pyplot as plt


# Sample dataset
data = {
    "Timestamp": [
        "10:00", "10:01", "10:02", "10:03", "10:04",
        "10:05", "10:06", "10:07", "10:08", "10:09",
        "10:10", "10:11", "10:12", "10:13", "10:14",
        "10:15", "10:16", "10:17", "10:18", "10:19"
    ],
    "CPU": [
        45, 52, 48, 55, 50,
        95, 47, 53, 49, 51,
        56, 54, 97, 52, 48,
        50, 57, 55, 92, 46
    ],
    "Memory": [
        60, 62, 61, 64, 63,
        65, 62, 60, 61, 63,
        64, 62, 66, 61, 60,
        62, 64, 63, 65, 61
    ],
    "Response_Time": [
        180, 190, 175, 200, 185,
        420, 180, 195, 182, 188,
        190, 185, 450, 195, 180,
        190, 185, 188, 430, 182
    ]
}


df=pd.DataFrame(data)
#basic statistics
print("Basic Statistics")
print(df[["CPU","Memory","Response_Time"]].describe())

#Threshold based detection

CPU_THRESHOLD=80

df["STATUS"]=df["CPU"].apply(
    lambda x: "Anomaly" if x>80 else "Normal"
)

#find anomalies
anomalies=df[df["STATUS"]=="Anomaly"]

print("Total records",len(df))
print("Anomalies detected:", len(anomalies))

print("\nAnomalous Records:")
print(
    anomalies[
        ["Timestamp", "CPU", "Memory", "Response_Time", "STATUS"]
    ]
)

#ploting

plt.figure(figsize=(10,5))

plt.plot(
    df["Timestamp"],df["CPU"],
    marker="o",
    label="CPU Usage"
)

plt.scatter(
    anomalies["Timestamp"],anomalies["CPU"],
    marker="x",
    s=100,
    label="Anomaly"

)

# Threshold line
plt.axhline(
    y=CPU_THRESHOLD,
    linestyle="--",
    label="Threshold"
)

plt.xlabel("Timestamp")
plt.ylabel("CPU Usage (%)")
plt.title("AIOps CPU Anomaly Detection")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()