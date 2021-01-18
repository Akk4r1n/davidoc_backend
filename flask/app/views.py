from app import app
import os
from os import walk

@app.route("/")
def index():
    return "Hello from Flask in a container!"

@app.route("/login")
def login():
    return "Trying to login huh"

@app.route("/documentations")
def get_documentations():
    # TODO: get path from config
    documentationPath = "/Documentation"
    scanned_folder = scan_folder_recursively({}, documentationPath)
    return scanned_folder

def scan_folder_recursively(myDictionary, path):
    # use the walk function from the os-module to get the path and the names of all files and folders seperated in that folder
    for dirpath, dirnames, filenames in walk(path):
        # get the folder name from the dirpath variable
        folderName = os.path.basename(os.path.normpath(dirpath))

        # append the foldername to the dictionary
        myDictionary["Foldername"] = folderName
        myDictionary["Files"] = get_files(path)

        folderList = []
        # go through each folder recursively
        for directory in dirnames:
            newDictionary = {}
            folderList.append(scan_folder_recursively(newDictionary, path + f"/{directory}"))
        
        # append the list of folders after iterating through each one recursively
        myDictionary["Folders"] = folderList

        # return the dictionary
        return myDictionary

def get_files(path):
    for dirpath, dirnames, filenames in walk(path):
        fileList = []
        for fileItem in filenames:
            fileDict = {}
            fileDict["Filename"] = "'" + fileItem + "'"
            fileDict["Path"] = "'" + dirpath + f"/{fileItem}" + "'"
            fileList.append(fileDict)
        return fileList
