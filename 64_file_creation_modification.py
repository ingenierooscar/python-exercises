import datetime
import os

# Path to the file
path = r"abc.java"

stat = os.stat(path)
c_timestamp = stat.st_birthtime
c_time = datetime.datetime.fromtimestamp(c_timestamp)
print(c_time)
