import sys
import datetime

print(str(sys.argv))
now = datetime.datetime.now()

after = sys.argv[1].split(":")
before = sys.argv[2].split(":")

for i in range(len(after)):
    if after[i].startswith("0"):
        after[i] = after[i][1]

for i in range(len(before)):
    if before[i].startswith("0"):
        before[i] = before[i][1]


before_date = now.replace(hour=int(before[0]), minute=int(before[1]), second=int(before[2]), microsecond=999999)
after_date = now.replace(hour=int(after[0]), minute=int(after[1]), second=int(after[2]), microsecond=0)

if after_date <= now <= before_date:
    print("true")
else:
    print("false")

