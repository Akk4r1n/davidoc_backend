import os
from os import walk
from flask import send_file
from flask import send_from_directory
from . import app

@app.route("/")
def index():
    return """
    <h1>Hello from Flask in a container!</h1>
    <h2>This is the backend for DaviDoc!</h2>
    <br>
    <h2>List of existing endpoints:</h2>
    <hr>
    <ul>
      <li>/doc - returns the folder structure for the documentation</li>
      <li>/doc/path - returns the content of a file with the given path</li>
    </ul>
    """

"""
Get the folder structure for the entire documentation
"""
@app.route("/doc")
def get_documentation():
    # TODO: get path from config
    # This is the path from inside the container
    documentationPath = "/documentation"
    scanned_folder = scan_folder_recursively({}, documentationPath)
    return scanned_folder

"""
Get the file content for the given path
"""
@app.route("/doc/<path:subpath>")
def get_file_dynamically(subpath):
    print(subpath)
    try:
        # return send_file(f"/documentation/{subpath}.md")
        return send_from_directory("/documentation/", f"{subpath}.md", as_attachment=True)
    except Exception as exception:
        return str(exception)

"""
Scan the directory recursively for all folders and files
"""
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

"""
Get all files in the given directory
"""
def get_files(path):
    for dirpath, dirnames, filenames in walk(path):
        fileList = []
        for fileItem in filenames:
            fileDict = {}
            fileDict["Filename"] = fileItem
            fileDict["Path"] = dirpath + f"/{fileItem}"
            fileList.append(fileDict)
        return fileList
