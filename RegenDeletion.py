#The main intention of the script is the ability to remove a file, that can regenerate itself. Later you can put it in the task manager.



import os
import subprocess

#I have made it flexible, so you can easily change the path to the file and app name.
initFile = "PATH";
#Has to be type string, so we would encode it later in order to check if it is a running task.
yourApp = "yourapp";
#Getting list of processes.
s = subprocess.check_output("tasklist", shell=True)
#Cheking if the process isn't in the processes list.
if yourApp.encode() not in s:
#Removing a file.
    if os.path.exists(initFile):
            os.remove(initFile)
            print("File has been Removed!")
# Throwing an error if there is no file in the path.
    else:
        print(FileNotFoundError)
else:
    print("Running!")

