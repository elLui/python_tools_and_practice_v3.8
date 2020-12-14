def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
            if text[7] != '-':
                return False
            for i in range(8, 12):
                if not text[i].isdecimal():
                    return False
            return True

def findNumber(text):
    for i in range(len(text)):
        chunk = text[i:i+12]
        if isPhoneNumber(chunk):
            print('phone number found: ' + chunk)
    print('done')


### driver

phone = 'message 415-324-2532 is the naoigjv 873-091-5892'
print(isPhoneNumber(phone))
print(findNumber(phone))

phone = '912344-7719'
print(isPhoneNumber(phone))
