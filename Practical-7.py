fh = open('Practical-7.txt','w')
str = 'level'
newstr = str[::-1]

if str == newstr:
    fh.write('It is Palindrome.')
else:
    fh.write('It is not Palindrome.')
fh.close()


