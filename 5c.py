'''
5.b
Develop a python program that could search the text in a file for phone numbers
(+919900889977) and email addresses (sample@gmail.com)
'''

import re

phoneNumRegex = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
emailRegex = re.compile(r'\w+\@\w+\.\w+')

mo = phoneNumRegex.search('(+919900889977)')
print(mo.group())

em = emailRegex.search('Abhinandan@gmail.com')
print(em.group())