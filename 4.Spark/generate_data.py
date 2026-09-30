import csv

raw_records = [
    ["tx_id", "user_id", "age", "signup_date", "purchase_amount", "country", "status"],
    [101, "USR_101", 25, "2026-01-10", 150.00, "IN", "COMPLETED"],
    [102, "USR_102", "", "2026-01-11", 85.50, "US", "COMPLETED"],        # Missing age
    [103, "USR_103", 40, "2026-01-12", -30.00, "IN", "FAILED"],          # Negative amount & failed
    [104, "USR_104", 19, "bad_timestamp", 310.00, "UK", "COMPLETED"],    # Corrupted date string
    [105, "USR_105", "", "2026-01-14", 1200.00, "IN", "COMPLETED"],      # Missing age & high spender
    [106, "USR_106", 52, "2026-01-15", 0.00, "US", "CANCELLED"],        # 0 amount & cancelled
    [107, "USR_107", 31, "2026-01-16", 240.00, "US", "COMPLETED"],
    [108, "USR_108", 22, "2026-01-17", 450.00, "IN", "COMPLETED"],
    [109, "USR_109", 60, "2026-01-18", 99.00, "UK", "COMPLETED"]
]

# Opens "raw_orders.csv" in write mode ("w") using a context manager ('with') to ensure the file automatically closes when done.
# newline="" prevents extra blank lines between rows on Windows, and encoding="utf-8" safely handles special characters.
with open("raw_orders.csv", "w", newline="", encoding="utf-8") as f:

    # Creates a CSV writer object that will format and send data to the opened file object 'f'.
    writer = csv.writer(f)
    writer.writerows(raw_records)

print("Created 'raw_orders.csv' with realistic dirty records.")
