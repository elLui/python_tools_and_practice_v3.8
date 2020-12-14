print('how many sweedish valhunds do you have?')
numPups = input()

try:
    if int(numPups) >= 4:
           print('that is alot of pups!')
    elif int(numPups) < 0:
            print('did you loose your pups you crazy pschyco!')
    else:
        print('that is not that many pups!')
except ValueError:
    (print('you did not enter a number!'))

