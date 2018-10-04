#!/usr/bin/env python3

import re, pyperclip

password = pyperclip.paste()

eightLettersRegex = re.compile(r'\S{8,}')
oneUppercaseRegex = re.compile(r'[A-Z]')
oneNumberRegex = re.compile(r'\d')

check = {
    eightLettersRegex: 'Your password must be 8 letters',
    oneUppercaseRegex: 'Your password must have at least one uppercase Letter.',
    oneNumberRegex: 'Your password must have at least one number.'
}

print('Analyzing your password.')

count = 1
for regex, msg in check.items():
    mo = regex.search(password)
    if mo == None:
        print(msg)
        break
    if count == len(check):
        print('Good! Your password is strong enough!')
    count += 1

print('End.')