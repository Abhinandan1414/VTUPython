'''
5.a'
    Write a function called isphonenumber () to recognize a pattern 415-555-4242 without
using regular expression and also write the code to recognize the same pattern using
regular expression.
'''
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
