while True:
    print('enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('please enter an integer for your age')

while True:
    print('select a new password (leter and numbers only): ')
    password = input()
    if password.isalnum():
        break
    print('password can only be numbers and letters')
