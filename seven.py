import shutil
import os

# 7
def copyDirectory(sourcePath: str, destinationPath: str, fileTypes=[]):
    if os.path.exists(destinationPath):
        shutil.rmtree(destinationPath)

    if os.path.exists(sourcePath):
        if os.path.isdir(sourcePath):
            os.mkdir(destinationPath)
            dirContent = os.listdir(sourcePath)

            for fileName in dirContent:
                copyDirectory(sourcePath + "\\" + fileName, destinationPath + "\\" + fileName,
                              fileTypes)
        elif os.path.splitext(sourcePath)[1][1:] in fileTypes or not fileTypes:
            shutil.copy(sourcePath, destinationPath)
    else:
        print("error: bad path - " + sourcePath)
        pass
