from sklearn.ensemble import IsolationForest
from collections import Counter

##read logs

with open('logs.txt','r',encoding='utf-8') as file:
    logs=file.readlines()

#count total errors
errors_in_log=0

for log in logs:
    if 'ERROR' in log:
        errors_in_log+=1
print(f"Total number of errors : {errors_in_log}")

# Count errors by minute
errors_by_minute = Counter()

for log in logs:
    parts=log.split()

    if len(parts)>=6:
        level=parts[2]
        minute=parts[1][:5]

        if level=="ERROR":
            errors_by_minute[minute]+=1

print("\nErrors by minute:")

for minute, count in errors_by_minute.items():
    print(minute, "->", count)


# Rule-based anomaly detection
threshold = 6

print("\nAnomalies:")

for minute, count in errors_by_minute.items():
    if count > threshold:
        print("Anomaly:", minute, "had", count, "errors")  
