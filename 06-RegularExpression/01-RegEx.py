import re

email = input("Enter email id :")
match = re.match('[^A-Z][\w.]+@+[\w.]+', email)
if match:
    print("Pattern Match")
else:
    print("Pattern do not match")

print(match.group())
