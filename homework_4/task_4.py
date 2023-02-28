import re

name = ["FirstItem", "FriendsList", "MyTuple"]
name = str(name)
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name)
