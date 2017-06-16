#! python3.5
import os, shutil, sys
from pyunpack import Archive

path = sys.argv[1]

os.chdir(path)
curdir = os.getcwd()
print("Chosen folder "+curdir)
os.mkdir("_output")
print("_output folder has been created")

for file in os.listdir():
    print("Going to folder: "+file)
    os.chdir(".\\"+file)
    for file in os.listdir():
        if file.endswith(".rar"):
            print(file+" found. Please dont close while extracting")
            Archive(file).extractall("..\\_output")
            print("extracting "+file+" done!")    
    os.chdir("..")

print("All DONE!")
