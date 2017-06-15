import re

names_file = open("names.txt")
data = names_file.read()

names_file.close()

last_name= r'Love'
first_name = r'Kenneth'

#print(re.match(last_name,data))
#print(re.match(r'Kenneth',data))
#print(re.search(first_name , data))

# print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))

# print(re.search(r'\(\d{3}\) \d{3}-\d{4}', data))

#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data)) #? means 0 time or one time

#print(re.findall(r'\w*, \w+', data))

# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+' ,data))

# print(re.findall(r'\b[trehous]{9}\b' ,data, re.IGNORECASE)) #ignore lowercase or uppercase

# print(re.findall(r'''
#     \b@[-\w\d.]*   #first a word boundary , an @ , and then any number of charcter
#     [^.gov\t]+      #ignore 1+ instances of the letters 'g' 'o' or 'v'and a tab
#     \b              #match another boundary
# ''' ,data , re.VERBOSE | re.I))


# print(re.findall(r"""
#     \b[-\w]*,   #find a word boundary , 1+ hyphen or characters
#     \s          #find 1 whitespace
#     [-\w ]+       #1+ hyphens and characters and explicit spaces
#     [^\t\n]     #ignore tabs and new lines

# """ , data , re.X)) # re.X == re.VERBOSE : allow spaces and tabs in regex 


# print(re.findall(r'''
#     ^([-\w ]*,\s[-\w ]+)\t           #last and first names
#     ([-\w\d.+]+@[-\w\d.]+)\t        #email
#     (\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone
#     ([\w\s]+,\s[\w\s.]+)\t?         #job and company
#     (@[\w\d]+)?$                      #twitter

# ''',data ,re.X| re.MULTILINE))



# line = re.search(r'''
#     ^(?P<name>[-\w ]*,\s[-\w ]+)\t           #last and first names
#     (?P<email>[-\w\d.+]+@[-\w\d.]+)\t        #email
#     (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone
#     (?P<job>[\w\s]+,\s[\w\s.]+)\t?         #job and company
#     (?P<twitter>@[\w\d]+)?$                      #twitter

# ''',data ,re.X| re.MULTILINE)
# print(line)
# print(line.groupdict())

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t           #last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t        #email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?         #job and company
    (?P<twitter>@[\w\d]+)?$                      #twitter
''',re.X| re.MULTILINE)

#print(re.search(line,data).groupdict())
#print(line.search(data).groupdict())
for match in line.finditer(data):
    #print(match.group('name'))
    print('{first} {last} <{email}>'.format(**match.groupdict()))

















