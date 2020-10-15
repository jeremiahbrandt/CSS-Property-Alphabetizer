FILE_NAME = "style.css"

def writeToFile():
    for selector in selectors:
        newFile.write(selector)

def removeNewLinesBetweenSelectors():
    for i in range(len(selectors) - 1):
        orginalSelector = selectors[i]
        newLineCount=0
        for character in orginalSelector:
            if character == "\n":
                newLineCount += 1
            else:
                break

        selectors[i] = orginalSelector[newLineCount:]
        selectors[i] = selectors[i][:selectors[i].rfind(";")] + ";\n}"
        if i > 0:
            selectors[i] = "\n\n" + selectors[i]

def sortSelector(selector):
    propertiesStringStart = selector.find("{")+1
    propertiesStringEnd = selector.find("}")
    cssPropertiesString = selector[propertiesStringStart:propertiesStringEnd]
    cssPropertiesArray = cssPropertiesString.split(";")
    cssPropertiesArray.sort()
    cssPropertiesArray.pop(0)

    for i in range(len(cssPropertiesArray)):
        cssPropertiesArray[i] = cssPropertiesArray[i] + ";"

    newCssProperties = " ".join(map(str, cssPropertiesArray))
    selector = selector[:propertiesStringStart] + newCssProperties + selector[propertiesStringEnd:]
    return selector

orignalFile = open(FILE_NAME, "r")
newFile = open("newFile.css", "w+")

originalContents = orignalFile.read()
selectors = originalContents.split("}")

removeNewLinesBetweenSelectors()

for i in range(len(selectors)):
    selectors[i] = sortSelector(selectors[i])

writeToFile()
