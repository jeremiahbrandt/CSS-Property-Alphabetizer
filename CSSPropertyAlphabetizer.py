import sys
import os

FILE=""
try:
    FILE = sys.argv[1]
except IndexError:
    print("Correct usage: py " + os.path.basename(sys.argv[0]) + " \"FILE.css\"")
    print("Example: CSSPropertyAlphabetizer.py style.css")
    quit(1)

# Read original fle contents
originalString = open(FILE, "r").read()

# Remove new line characters
originalString = originalString.replace("\n", "")

# Store selectors in List
selectors = originalString.split("}")
selectors.pop()
for i in range(len(selectors)):
    selectors[i] = selectors[i] + "}\n\n"

# Sort properties w/in each selector
for i in range(len(selectors)):
    selector = selectors[i]
    startI = selector.find("{") + 1
    endI = selector.find("}")
    propertiesStr = selector[startI:endI]
    propertiesList = propertiesStr.split(";")
    propertiesList.pop()
    # Add new line character and semicolon to every property
    for j in range(len(propertiesList)):
        propertiesList[j] = "\n" + propertiesList[j] + ";"
    # Sort properties
    propertiesList.sort()
    # Add new line character after last property
#    propertiesList[-1] = propertiesList[-1] + "\n"
    # Replace original selector w/ sorted selector
    selectors[i] = selectors[i][:startI] + "".join(map(str, propertiesList)) + selectors[i][endI:]

# Write to new CSS file
outputFile = open(f"alphabetized-{FILE}", "w+")
for selector in selectors:
    outputFile.write(selector)
