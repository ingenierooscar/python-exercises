from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir(
    '.') if isfile(join('.', f))]
print(files_list)
