from tkinter import *
import json
from tkinter import filedialog
from tkinter import messagebox
from organizer import addNewFolder, organize, createData
import os

if not os.path.exists("data"):
    createData()

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
    data["downDir"] = downDir + "/"
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
    data["gotoDir"] = gotoDir + "/"
    with open("data/dirs.json", "w") as f:
        json.dump(data, f, indent=4)

    l2.config(text="Goto directory: " + gotoDir)

gotoDirB = Button(root, text="Select", command=selectGotoDir)
gotoDirB.grid(row=1, column=1)

extCnt = 1
def openNewFolderWindow():
    global extCnt
    extCnt = 1

    top = Toplevel()
    top.title("Add a new folder")

    extes = []

    def deleteExtE():
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

    def done():
        if extes == []:
            messagebox.showerror("No extensions", "Please provide some extensions.")
            return
        elif nameE.get() == "":
            messagebox.showerror("No name", "Please provide a folder name.")
            return
        else:
            exts = []
            for exte in extes:
                if exte[0].get() == "":
                    messagebox.showerror("No name", "Please provide extensions names.")
                    return
                exts.append(exte[0].get())
            
            addNewFolder(nameE.get(), exts)
            top.destroy()

    l = Label(top, text="").grid(column=0, row=99)
    doneB = Button(top, text="Add", command=done).grid(row=100, column=2)

# TODO: Add a way so that users can see the custom folders that they added
# TODO: Implement Custom folder edit thing 😥

addNew = Button(root, text="Add a new folder!", command=openNewFolderWindow)
addNew.grid(row=2, column=0)

def org():
    with open("data/dirs.json", "r") as f:
        tmp = json.load(f)
    down = tmp["downDir"]
    goto = tmp["gotoDir"]

    organize(down, goto)

folderCnt = 0
def foldersCommand():
    folders = {}
    foldersNew = {}
    with open("data/customExtensions.json", "r") as f:
        folders = json.load(f)
    
    if len(folders) == 0:
        messagebox.showerror("Not Found", "No custom folders were found!")
        return

    global folderCnt
    top = Toplevel()
    top.title("Custom Folders")

    for folder in folders.keys():
        l = Label(top, text="Folder Name: ").grid(row=folderCnt, column=0)

        name = Entry(top)
        name.insert(0, folder)
        name.grid(row=folderCnt, column=1)

        deleteFolder = Button(top, text="Delete Folder").grid(row=folderCnt, column=2)

        folderCnt += 1

        for ext in folders[folder]:
            l1 = Label(top, text="Ext Name: ").grid(row=folderCnt, column=0)

            extName = Entry(top)
            extName.insert(0, ext)
            extName.grid(row=folderCnt, column=1)

            deleteExt = Button(top, text="Delete").grid(row=folderCnt, column=2)
            folderCnt += 1

        l = Label(top, text="").grid(columnspan=3, column=0, row=folderCnt)

        folderCnt += 1

    upBut = Button(top, text="Update").grid(row=folderCnt, column=2)

    # TODO: Implement deletion for everything 😫

orgBut = Button(root, text="Organize!", command=org)
orgBut.grid(row=3, column=0)

foldBut = Button(root, text="Custom Folders", command=foldersCommand)
foldBut.grid(row=2, column=1)

mainloop()