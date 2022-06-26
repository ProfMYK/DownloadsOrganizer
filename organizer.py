import os
import json

extensions = {}
extensions["Images"] = ["jpg", "jpeg", "jpe", "jif", "jfif", "jfi", "png", "gif", "webp", "tiff", "tif", "psd", "raw", "arw", "cr2", "nrw", "k25", "bmp", "dib", "heif", "heic", "ind", "indd", "indt", "jp2", "j2k", "jpf", "jpx", "jpm", "mj2", "svg", "svgz", "ai"]
extensions["Videos"] = ["webm", "mkv", "flv", "vob", "ogv",  "drc", "gifv", "mng", "avi", "MTS", "M2TS", "TS", "mov", "qt", "wmv", "yuv", "rm", "rmvb", "viv", "asf", "amv", "mp4", "m4v", "mpg", "mp2", "mpeg", "mpe", "mpv", "m2v", "m4v", "svi", "mxf", "roq", "nsv", "flv", "f4v", "f4p", "f4a", "f4b"]
extensions["Audios"] = ["3gp", "aa", "aac", "aax", "act", "aiff", "alac", "amr", "ape", "au", "awb", "dss", "dvf", "flac", "gsm", "iklax", "ivs", "m4a", "m4b", "m4p", "mmf", "mp3", "mpc", "msv", "nmf", "ogg", "oga", "mogg", "opus", "ra", "rm", "raw", "rf64", "sin", "tta", "voc", "vox", "wav", "wv", "webm", "8svx", "cda"]
extensions["Text"] = ["doc", "docx", "odt", "pdf", "rtf", "tex", "txt", "wpd"]
extensions["Data"] = ["csv", "dat", "db", "dbf", "log", "mdb", "sav", "sql", "tar", "xml"]
extensions["OS"] = ["bin", "dmg", "iso", "toast", "vcd"]
extensions["Zip"] = ["7z", "arj", "deb", "pkg", "rar", "rpm", "tar.gz", "z", "zip"]
extensions["Executables"] = ["exe"]

def addNewFolder(name: str, exts: list):
    with open("data/customExtensions.json", "r") as f:
        data = json.load(f)
    data[name] = exts
    with open("data/customExtensions.json", "w") as f:
        f.write(json.dumps(data, indent=4))

def createFolders(gotoDir: str):
    with open("data/customExtensions.json", "r") as f:
        customExtensions = json.load(f)

    for key in extensions.keys():
        if not os.path.exists(gotoDir + key + "/"):
            os.makedirs(gotoDir + key + "/")
            
    if not os.path.exists(gotoDir + "Unknown/"):
        os.makedirs(gotoDir + "Unknown/")

    for key in customExtensions.keys():
        if not os.path.exists(gotoDir + key + "/"):
            os.makedirs(gotoDir + key + "/")
            

def createData():
    os.makedirs("data")
    with open("data/customExtensions.json", "w") as f:
        f.write("{}\n")
    data = {"downDir": "", "gotoDir": ""}
    with open("data/dirs.json", "w") as f:
        json.dump(data, f, indent=4)

def organize(downDir: str, gotoDir: str):
    with open("data/customExtensions.json", "r") as f:
        customExtensions = json.load(f)

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