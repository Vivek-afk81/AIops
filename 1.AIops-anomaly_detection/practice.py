from sklearn.ensemble import IsolationForest


response_time=[
    120, 125, 118, 130, 122,
    127, 124, 121, 129, 126,
    123, 128, 125, 122, 131,
    700, 127, 119, 650, 124
]

response_time=[[i] for i in response_time]

model=IsolationForest(
    contamination=0.1,
    random_state=42
)

model.fit(response_time)

labels=model.predict(response_time)

print(labels)

for time, label in zip(response_time, labels):
    if label == -1:
        print(time[0], "ms -> Anomaly")
    else:
        print(time[0], "ms -> Normal")