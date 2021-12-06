def read_input():
    with open("input/input11.txt") as input_file:
        for line in input_file:
            input_str = line.rstrip()
    return input_str

def recursiveCheck(string, numReplace, index):
    if string[index] == "z":
        numReplace += 1
        index -= 1
        return recursiveCheck(string, numReplace, index)
    return numReplace

def incrementPwd(string):
    index = len(string) - 1
    numReplace = recursiveCheck(string, 0, index)
    if string[index] != "z":
        string = string[:index] + chr(ord(string[index])+1) + string[index+1:]
    for i in range(0, numReplace):
        string = string[:index-i] + "a" + string[index+1-i:]
        string = string[:index-i-1] + chr(ord(string[index-i-1])+1) + string[index-i:]
    return string

def checkOne(string):
    listString = list(string)
    tripList = [i+j+k for i,j,k in zip(string, string[1:], string[2:])]
    for i in range(0, len(tripList)):
        if ord(tripList[i][0]) == ord(tripList[i][1]) - 1 and ord(tripList[i][1]) == ord(tripList[i][2]) - 1:
            return True
    return False

def checkTwo(string):
    noNos = ["i", "o", "l"]
    listString = list(string)
    for char in listString:
        if char in noNos:
            return False
    return True

def checkThree(string):
    listString = list(string)
    doubleList = [i+j for i,j in zip(string, string[1:])]
    numDoubles = 0
    for double in doubleList:
        if double[0] == double[1]:
            if doubleList.count(double) == 1:
                numDoubles += 1
    if numDoubles >= 2:
        return True
    else:
        return False

def main():
    inputPwd = read_input()
    numPwd = 0
    while True:
        inputPwd = incrementPwd(inputPwd)
        if all([checkOne(inputPwd), checkTwo(inputPwd), checkThree(inputPwd)]):
            numPwd += 1
            print(numPwd, inputPwd)
        if numPwd == 2:
            break

main()
