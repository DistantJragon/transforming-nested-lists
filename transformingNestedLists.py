import math

def unravel_list_string(nestedListsString):
    nestedListsString = nestedListsString[1:-2]
    listOfListsStrings = nestedListsString.split('], ')
    for i in range(len(listOfListsStrings)):
        listOfListsStrings[i] = listOfListsStrings[i][1:]
        listOfListsStrings[i] = listOfListsStrings[i].split(', ')
    for i in range(len(listOfListsStrings)):
        for j in range(len(listOfListsStrings[0])):
            try:
                listOfListsStrings[i][j] = int(listOfListsStrings[i][j])
            except:
                listOfListsStrings[i][j] =  listOfListsStrings[i][j]
            else:
                listOfListsStrings[i][j] = int(listOfListsStrings[i][j])
                
    return listOfListsStrings

def convert_list_to_matrix_string_list(givenList):

    givenNumberOfRows = len(givenList)
    givenNumberOfColumns = len(givenList[0])

    biggestLengthByColumn = []
    matrixStringList = []


    for i in range(givenNumberOfColumns):
        biggestLengthByColumn.append(0)
        for j in range(givenNumberOfRows):
            if biggestLengthByColumn[i] < len(str(givenList[j][i])): biggestLengthByColumn[i] = len(str(givenList[j][i]))
    
    for i in range(givenNumberOfRows):
        matrixLine = ''
        for j in range(givenNumberOfColumns):
            spacesNeeded = biggestLengthByColumn[j] - len(str(givenList[i][j]))
            for k in range(math.floor(spacesNeeded / 2)):
                matrixLine += ' '
            matrixLine += str(givenList[i][j])
            for k in range(math.ceil(spacesNeeded / 2) + 1):
                matrixLine += ' '
        matrixStringList.append(matrixLine)

    return matrixStringList

def rotate_nested_lists(givenList, numberOfRotations):
    
    givenNumberOfRows = len(givenList)
    givenNumberOfColumns = len(givenList[0])

    rotatedNestedList = []
    rotatedNumberOfRows = givenNumberOfColumns
    rotatedNumberOfColumns = givenNumberOfRows

    # simplify #OfRots
    numberOfRotations %= 4
    if (numberOfRotations < 0): numberOfRotations += 4

    if (numberOfRotations > 0):
        for j in range(rotatedNumberOfRows):
            rotatedNestedList.append([])
            for k in range(rotatedNumberOfColumns):
                rotatedNestedList[j].append(givenList[givenNumberOfRows - k - 1][j])
        numberOfRotations -= 1
        rotatedNestedList = rotate_nested_lists(rotatedNestedList, numberOfRotations)
    else: rotatedNestedList = givenList

    return rotatedNestedList

def flip_nested_lists(givenList, numberOfHorizFlips, numberOfVertFlips):

    givenNumberOfRows = len(givenList)

    # simplify #OfHFlips
    numberOfHorizFlips %= 2
    numberOfHorizFlips = abs(numberOfHorizFlips)

    # simplify #OfVFlips
    numberOfVertFlips %= 2 
    numberOfVertFlips = abs(numberOfVertFlips)

    if (numberOfHorizFlips == 1):
        for i in range(givenNumberOfRows):
            givenList[i] = givenList[i][::-1]
    
    if (numberOfVertFlips == 1):
        givenList = givenList[::-1]

    return givenList

nestedListsFromInput = input('Input your list: ')
nestedList = unravel_list_string(nestedListsFromInput)
for list in convert_list_to_matrix_string_list(nestedList):
    print(list)

nestedList = rotate_nested_lists(nestedList, 0)
nestedList = flip_nested_lists(nestedList, 1, 0)
for list in convert_list_to_matrix_string_list(nestedList):
    print(list)
