listToPrint = ['pots', 'pans', 'utensils', 'plates', 'cups', 'glasses']
while True:
    newWord = input("Enter a word to add to the list (press '0' to stop adding words) > ")
    if newWord == "0":
        break
    else:
        listToPrint.append(newWord)

listToPrint.insert(-1, 'and')     # inserts next to last element value

print(', '.join(listToPrint[:-2]) +' '+ ' '.join(listToPrint[-2:]))
