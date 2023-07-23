# 5
itemSplit="#%#"
lineSplit="##%##"

# 5a
def saveData(fileName: str, fileData: list):
    file = open(fileName, "w")
    file.write(itemSplit.join(str(item) for item in fileData) + lineSplit
               + itemSplit.join(type(item).__name__ for item in fileData))

    return


# 5b
def loadData(fileName: str):
    try:
        file = open(fileName, "r")
    except:
        print("error, no file found")

        pass
    try:
        lists = file.read().split(lineSplit)
        valuesList = lists[0].split(itemSplit)
        typesList = lists[1].split(itemSplit)

        fileData = []

        for index, value in enumerate(valuesList):
            if typesList[index] == "int":
                fileData.append(int(value))
            elif typesList[index] == "float":
                fileData.append(float(value))
            elif typesList[index] == "bool":
                fileData.append(value == "True")
            else:
                fileData.append(value)

        return fileData
    except:
        print("error: wrong file format")

        pass
