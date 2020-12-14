#! python3
# pw.py - an insecure password locker program

PASSWORDS ={'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()


account = sys.argv[1] #this turns the first command line argument the account variable

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('password for ' + account + ' copied to clipboard.')
else:
    print('there is not account name ' + account)
