import re



def isPhoneNumber_improved(text):
    phoneNumRegex = re.compiler(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search(text)
    print('phone nubmer found: ' + mo.group())



message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
isPhoneNumber_improved(message)

    
