import re

def readInput():
    inputFile = open("input/input16.txt", "r")
    thingsArr = []
    dictArr = []
    for line in inputFile:
        inputDict = {}
        currentLine = line.split()
        thingOne = str(currentLine[2].split(":")[0])
        numThingOne = int(currentLine[3].split(",")[0])
        thingTwo = str(currentLine[4].split(":")[0])
        numThingTwo = int(currentLine[5].split(",")[0])
        thingThree = str(currentLine[6].split(":")[0])
        numThingThree = int(currentLine[7])
        sueNum = int(currentLine[1].split(":")[0])
        inputDict[thingOne]  = numThingOne
        inputDict[thingTwo]  = numThingTwo
        inputDict[thingThree] = numThingThree
        if thingOne not in thingsArr:
            thingsArr.append(thingOne)
        dictArr.append(inputDict)

    for thing in thingsArr:
        for stuff in dictArr:
            if thing not in stuff.keys():
                stuff[thing] = 999

    matchDict = {"children":3, "cats":7, "samoyeds":2, "pomeranians":3, "akitas":0, "vizslas":0, "goldfish":5, "trees":3, "cars":2, "perfumes":1}
    return dictArr, thingsArr, matchDict

def part_1(dictArr, thingsArr, matchDict):
    matchesFlag = False
    matchArr = []
    for term in dictArr:
            for thingName in thingsArr:
                if term[thingName] == matchDict[thingName] or term[thingName] == 999:
                    matchesFlag = True
                else:
                    matchesFlag = False
                    break
            if matchesFlag == True:
                matchArr.append(dictArr.index(term)+1)
    return matchArr

def part_2(dictArr, thingsArr, matchDict):
    matchesFlag = False
    matchArr = []
    for term in dictArr:
            for thingName in thingsArr:
                if thingName == "cats" or thingName == "trees":
                    if term[thingName] > matchDict[thingName] or term[thingName] == 999:
                        matchesFlag = True
                    else:
                        matchesFlag = False
                        break
                elif thingName == "pomeranians" or thingName == "goldfish":
                    if term[thingName] < matchDict[thingName] or term[thingName] == 999:
                        matchesFlag = True
                    else:
                        matchesFlag = False
                        break
                else:
                    if term[thingName] == matchDict[thingName] or term[thingName] == 999:
                        matchesFlag = True
                    else:
                        matchesFlag = False
                        break

            if matchesFlag == True:
                matchArr.append(dictArr.index(term)+1)

    return matchArr

def main():
    dictArr, thingsArr, matchDict = readInput()
    print(part_1(dictArr, thingsArr, matchDict))
    print(part_2(dictArr, thingsArr, matchDict))

main()
