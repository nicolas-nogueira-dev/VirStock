import os
from os.path import join

def getFilespath(folderPath):
    files = os.listdir(folderPath)
    filesDict = {}
    for file in files:
        indexFilesDict = len(filesDict) + 1
        temp = {"fileName":str(file),"fileSize":os.path.getsize(folderPath+"/"+file)}
        filesDict[str(indexFilesDict)] = temp
    return filesDict

def formateSize(size):
    if size < 1000:
        return f"{size} kb"
    if size >= 1000 and size < 1000000 :
        size = round(size / 1000, 2)
        return f"{size} mb"
    if size >= 1000000:
        size = round(size / 1000000000, 2)
        return f"{size} gb"

def saveFile(app,file,fileName):
    file.save(join(app.config['UPLOAD_FOLDER'], fileName))
