def linearSearch(intList,target):
    #print (target)
    found = False
    position = 0
    while position < len(intList):
        #print(intList[position])
        if intList[position] == target:
            found = True
            break
        position = position + 1

    return found

linearList = [3,5,9,7,6,12,15,9,1]
numInput = int(input("What number are you looking for? "))
numFound = linearSearch(linearList,numInput)
if numFound:
    print("The number is in index: ")
else:
    print("The number is not in the list")
