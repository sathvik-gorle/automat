import os
import shutil
import time

# adds a certain amount of folders to computer with a path

number = 0
folders = input("Enter the amount of folders you want to add: ")
folders = int(folders)
path = input("Enter the path to make folders in: ")
result = True

while(result):
    number = number + 1
    if (number <= folders):
        os.makedirs(path+"/folder"+str(number))
        startTime = time.time() 
    else:
        result = False