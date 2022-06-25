from tkinter import *
import json
from tkinter import filedialog
from organizer import addNewFolder, organize

root = Tk()
root.title("Downloads Organizer")

downDir = ""
gotoDir = ""

with open("data/dirs.json", "r") as f:
        tmp = json.load(f)

l1 = Label(root, text="Downloads directory: " + tmp["downDir"])
l1.grid(row=0, column=0)

def selectDownDir():
    global downDir
    downDir = filedialog.askdirectory(initialdir="C:/", title="Select downloads directory")
    
    with open("data/dirs.json", "r") as f:
        data = json.load(f)
    data["downDir"] = downDir
    with open("data/dirs.json", "w") as f:
        json.dump(data, f, indent=4)

    l1.config(text="Downloads directory: " + downDir)

downDirB = Button(root, text="Select", command=selectDownDir)
downDirB.grid(row=0, column=1)

l2 = Label(root, text="Goto directory: " + tmp["gotoDir"])
l2.grid(row=1, column=0)

def selectGotoDir():
    global gotoDir
    gotoDir = filedialog.askdirectory(initialdir="C:/", title="Select downloads directory")

    with open("data/dirs.json", "r") as f:
        data = json.load(f)
    data["gotoDir"] = gotoDir
    with open("data/dirs.json", "w") as f:
        json.dump(data, f, indent=4)

    l2.config(text="Goto directory: " + gotoDir)

gotoDirB = Button(root, text="Select", command=selectGotoDir)
gotoDirB.grid(row=1, column=1)

extCnt = 1
def openNewFolderWindow():
    top = Toplevel()
    top.title("Add a new folder")

    extes = []

    def deleteExtE(num):
        # TODO: add deletion for the extension entries
        ...

    def addExtension():
        global extCnt
        
        e = Entry(top)
        e.grid(row=extCnt, column=0)

        db = Button(top, text="Delete", command=deleteExtE)
        db.grid(row=extCnt, column=1)
        
        extes.append((e, db))
        extCnt += 1

    tl = Label(top, text="Folder Name: ").grid(row=0, column=0)

    nameE = Entry(top)
    nameE.grid(row=0, column=1)

    extB = Button(top, text="Add Extension", command=addExtension).grid(row=0, column=2)

    # TODO: Finish the adding folder system 👌

# TODO: Add a way so that users can see the custom folders that they added

addNew = Button(root, text="Add a new folder!", command=openNewFolderWindow)
addNew.grid(row=2, column=0)

orgBut = Button(root, text="Organize!", command=lambda: organize(downDir, gotoDir))
orgBut.grid(row=2, column=1)

mainloop()