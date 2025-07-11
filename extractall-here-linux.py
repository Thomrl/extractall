import os, sys, rarfile

curdir = os.getcwd()
print("Chosen folder "+curdir+"\n")

for file in os.listdir():
    if not file.endswith("py"):
        os.chdir("./"+file)
        for file in os.listdir():
            if file.endswith(".rar"):
                print(file)
        os.chdir("..")

goOrNot = input("\nThe files listed above were found, do you wish to unpack them?\nPress Y and enter to continue\n").lower()

if goOrNot == "y":
    print("Super! Let's go!")
    if not os.path.exists("_output"):
        os.mkdir("_output")
        print("_output folder has been created")
    else:
        print("\"_output\" folder already exists!")
    for file in os.listdir():
        if not file == "extractall-here-linux.py":
            if not file == "_output":
                print("Going to folder: "+file)
                os.chdir("./"+file)
                for file in os.listdir():
                    if file.endswith(".rar"):
                        print(file+" found. Please dont close while extracting")
                        rar = rarfile.RarFile(file)
                        rar.extractall('../_output')
                        #rarfile(file).extractall("../_output")
                        print("extracting "+file+" done!")    
                os.chdir("..")
    print("All DONE!")
    print("You should be able to find the unpacked item(s) in the _output folder")
                                   
input("Finished! Press enter to close me.")                   
