#shit does not work but good ideas


def sentence(itemList):
    placeHolder = len(itemList) -1


    # join all values in a list into a string delimited by a ','
    stringList = ", ".join(itemList)
    
    print(stringList)
    # join all values from a string back into a list
    itemList2 = stringList.split(",")
    print (itemList2)    
    print(stringList)
    
    itemList.insert((len(itemList)-1), ' and')
    stringList = " ".join(itemList)
    print(stringList)



itemList = ['apples', 'bananas','tofu','cats']


print(itemList)
sentence(itemList)
