import os 
from datetime import datetime
arr = os.listdir()
print(arr)
for i in arr:
	created=os.stat(i).st_ctime
	print(i, "=" , datetime.fromtimestamp(created))

