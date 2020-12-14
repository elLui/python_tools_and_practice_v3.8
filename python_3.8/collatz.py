def collatz(number):
    if number%2 == 0:
        print(number)
    else:
        return 3 * number + 1
