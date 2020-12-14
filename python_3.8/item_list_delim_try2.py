itemList = ['cat','bat','rat','shat','dog']

itemList.insert(-1, 'and')

print(', '.join(itemList[:-2]) + ' ' + ' '.join(itemList[-2:]))
