# Parse and filter by log level
error_count=0
with open("application.log", "r") as f:
    for line in f:
        parts = line.strip().split(maxsplit=4)
        date, time, level, service, message = parts
        if level == "ERROR":
            error_count+=1
            print(f"[{date} {time}] {message}")
    print(error_count)

# doing single rule based detection
threshold=6

