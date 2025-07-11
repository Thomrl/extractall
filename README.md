# Extractall
This scripts goes through the sub folders of the chosen folder and checks for .rar files, and then extracts the content to a folder called "\_output" which it will make by itself.

# How to use (new)
Simply run the script in the folder containing the folders with rar files in them.
```
Main folder
  folder
    .rar
    .r00
    .r01
  folder2
    .rar
    .r00
    .r01
  extractall.py
```
This means we put it in the folder where folder and folder2 is, so the script can go through those folders, check for rar files and start unpacking them.



# How to use (old)
Use "Run" (shortcut: windows key + R) and write: extractall "filepath". e.g: extractall "c:\user\Thomrl\received files\Cake"

You need to have installed the modules pyunpack and patool.
