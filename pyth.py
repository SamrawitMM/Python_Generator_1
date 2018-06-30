import sys
keywordArray = ["while", "for", "{", "}", "if", "else", "elif", "(", ")"]
f = input("\n Hello, user. "
    "\n \n Please type in the path to your file and press 'Enter': ")
file = open('f', 'r')
with open("file", "r") as ins:
    arrayStore = []
    for line in ins:
        if keywordArray[0] in line:
            arrayStore.append(keywordArray[0])
            if keywordArray[2] in line:
                arrayStore.append(keywordArray[2])
                if keywordArray[7] in line:
                    if True:
                        if keywordArray[8] in line:
                            if keywordArray[2] in line:
                                arrayStore.append(keywordArray[2])
                               
                                
        elif keywordArray[1] in line:
            arrayStore.append(keywordArray[1])
            if keywordArray[2] in line:
                arrayStore.append(keywordArray[2])
        elif keywordArray[2] in line:
            arrayStore.append(keywordArray[2])
            if keywordArray[1] in line:
                arrayStore.append(keywordArray[1])
            elif keywordArray[4] in line:
                arrayStore.append(keywordArray[4])
                #print(arrayStore)
            elif keywordArray[5] in line:
                arrayStore.append(keywordArray[5])
            elif keywordArray[6] in line:
                arrayStore.append(keywordArray[6])
            if keywordArray[3] in line:
                arrayStore.append(keywordArray[3])
        elif keywordArray[3] in line:
            arrayStore.append(keywordArray[3])
        elif keywordArray[4] in line:
            arrayStore.append(keywordArray[4])
            if keywordArray[2] in line:
                arrayStore.append(keywordArray[2])
        elif keywordArray[5] in line:
            arrayStore.append(keywordArray[5])
            if keywordArray[2] in line:
                arrayStore.append(keywordArray[2])
        elif keywordArray[6] in line:
            arrayStore.append(keywordArray[6])
            if keywordArray[2] in line:
                arrayStore.append(keywordArray[2])
    print(arrayStore)


#manipulate the stored array
''' if keywordArray[1] in line:
                                    arrayStore.append(keywordArray[1])
                                elif keywordArray[4] in line:
                                    arrayStore.append(keywordArray[4])
                                    #print(arrayStore)
                                elif keywordArray[5] in line:
                                    arrayStore.append(keywordArray[5])
                                elif keywordArray[6] in line:
                                    arrayStore.append(keywordArray[6])
                                    if keywordArray[3] in line:
                                        arrayStore.append(keywordArray[3])'''
        
