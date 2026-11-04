# fix_the_stats.py (fixed)
# Count failed logins and the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Fix 1:defined the the traker variable outside the loop to prevent it from resetting on every iteration.(semanticerror)
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
    count += 1
# Fix 2 (semantic): moved the print statement out of the loop block so it only runs once at the end.
# Fix 3 (semantic):replaced floor division // whith standard division / to get decimal output.
print(f"Average session: {total / count} minutes")

# Fix 4 (semantic):adjusted upper bound of the sequence to include number 4.
for level in range(1, 5):
    print(f"Level {level}")