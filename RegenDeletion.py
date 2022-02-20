import os
import subprocess

initFile = "PATH";
#Has to be a type of string, so we would encode it later in order to check if it is a running task.
yourApp = "yourapp";
#Getting list of processes.
s = subprocess.check_output("tasklist", shell=True)
#Cheking if the process isn't in the processes list.
if yourApp.encode() not in s:

    if os.path.exists(initFile):
            os.remove(initFile)
            print("File has been Removed!")
    else:
        print(FileNotFoundError)
else:
    print("Running!")
