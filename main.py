import os
import json

with open("data/importantData.json", "r") as f:
    data = json.load(f)
    downDir = data["downDir"]
    gotoDir = data["gotoDir"]

downDir = "C:/Users/PC/Downloads/"
gotoDir = "C:/Users/PC/Desktop/Downloads/"
customExtensions = {}

with open("data/extensions.json", "r") as f:
    extensions = json.load(f)

with open("data/customExtensions.json", "r") as f:
    customExtensions = json.load(f)

os.chdir(downDir)

for key in extensions.keys():
    if not os.path.exists(gotoDir + key + "/"):
        os.makedirs(gotoDir + key + "/")

for key in customExtensions.keys():
    if not os.path.exists(gotoDir + key + "/"):
        os.makedirs(gotoDir + key + "/")
if not os.path.exists(gotoDir + "Unknown/"):
    os.makedirs(gotoDir + "Unknown/")

def organize():
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