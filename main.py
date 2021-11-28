import os
#operating system
print(os.system("date"))
#shows the date
#os.mkdir("New Folder")
#makes a new folder on system
print(os.getcwd())
#finded the current working directory(where the user ios currently working)
print(os.path.exists('/Users/myrathakker/Desktop/Coding/C-100'))
#We are checking the path in the system to see if it exists(true) or not(false)
print(os.path.splitext("/Users/myrathakker/Desktop/Coding/C-99/main.py"))
#spliting the path from the root till the name of the file and the other part is the extension part