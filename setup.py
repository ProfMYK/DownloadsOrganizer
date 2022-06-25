import os
import json
from venv import create
from colorama import Fore
from organizer import createFolders
import colorama
colorama.init(autoreset=True)

customFolders = {} # {"FolderName/": ["extName1", "extName2"]}
downDir = ""
gotoDir = ""

downDir = input("What is your downloads directory: ")
while not os.path.exists(downDir):
    print(Fore.RED + "Folder not found!" + Fore.RESET)
    print("Please enter your downloads folder correctly!")
    downDir = input("What is your downloads directory: ")

gotoDir = input("Whay is the directory that you want the files to go: ")
while not os.path.exists(gotoDir):
    print(Fore.RED + "Folder not found!" + Fore.RESET)
    print("Please enter the folder correctly!")
    gotoDir = input("Whay is the directory that you want the files to go: ")

data = {"downDir": downDir, "gotoDir": gotoDir}
with open("data/dirs.json", "w") as f:
    f.write(json.dumps(data, indent=4))

data = {}
run = input("Do you want to add custom folders for spesific file extensions(Y/N): ")
while run.upper() == "Y":
    folderName = input("What is the name of the folder: ")
    exts = []
    ext = input("Add an extension name (press enter to quit): ")
    exts.append(ext)
    while ext != "":
        ext = input("Add an extension name (press enter to quit): ")
        exts.append(ext)
    del exts[-1]
    data[folderName] = exts
    print(f"Added the folder {folderName}.")
    run = input("Do you want to continue adding custom folders for spesific file extensions(Y/N): ")


with open("data/customExtensions.json", "w") as f:
    f.write(json.dumps(data, indent=4))