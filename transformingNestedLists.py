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

nestedListsFromInput = input("Input your list: ")
nestedList = unravel_list_string(nestedListsFromInput)

nestedList = rotate_nested_lists(nestedList, 0)
nestedList = flip_nested_lists(nestedList, 1, 0)
print(nestedList)