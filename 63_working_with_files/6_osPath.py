import os
# listdir() is used to list all files and folders inside the current folder
# endswith() is used to get all files ending with a particular filetype
# URL : https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

files = [f for f in os.listdir() if f.endswith('.txt')]

print(files)