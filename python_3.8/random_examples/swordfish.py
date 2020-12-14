while True:
    print('who are you?')
    name = input()
    if name != 'elluis':
        continue
    print('hello, elluis. what is the password? (it is a fish.)')
    password = input()
    if password == 'bubbafish':
        break
print('access granted')