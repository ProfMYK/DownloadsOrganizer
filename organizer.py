import os
import json

customExtensions = {}

with open("data/extensions.json", "r") as f:
    extensions = json.load(f)

with open("data/customExtensions.json", "r") as f:
    customExtensions = json.load(f)

def addNewFolder(name: str, exts: list):
    with open("data/customExtensions.json", "r") as f:
        data = json.load(f)
    data[name] = exts
    with open("data/customExtensions.json", "w") as f:
        f.write(json.dumps(data, indent=4))

def createFolders(gotoDir: str):
    for key in extensions.keys():
        if not os.path.exists(gotoDir + key + "/"):
            os.makedirs(gotoDir + key + "/")

    for key in customExtensions.keys():
        if not os.path.exists(gotoDir + key + "/"):
            os.makedirs(gotoDir + key + "/")
    if not os.path.exists(gotoDir + "Unknown/"):
        os.makedirs(gotoDir + "Unknown/")

    # TODO: Create the data folder and the files inside of it

def organize(downDir: str, gotoDir: str):
    createFolders(gotoDir)
    os.chdir(downDir)
    files = os.listdir()
    for f in files:
        placed = False
        for key in extensions.keys():
            for ext in extensions[key]:
                if f.endswith("." + ext):
                    os.rename(downDir + f, gotoDir + key + "/" + f)
                    placed = True

        for key in customExtensions.keys():
            for ext in customExtensions[key]:
                if f.endswith("." + ext):
                    os.rename(downDir + f, gotoDir + key + "/" + f)
                    placed = True

        if not placed:
            os.rename(downDir + f, gotoDir + "Unknown/" + f)