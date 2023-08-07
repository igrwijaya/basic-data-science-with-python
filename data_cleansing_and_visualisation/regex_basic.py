import re

# SPLITTING WORDS
text = """101 COM     Computers
205 MAT Mathematics
205 MATX Mathematics Extra
189 ENG English"""

# split by spaces (\s+)
splitTextBySpace = re.split('\s+', text)
print(splitTextBySpace)
# Output:
# ['101', 'COM', 'Computers', '205', 'MAT', 'Mathematics', '205', 'MATX', 'Mathematics', 'Extra', '189', 'ENG', 'English']

# SUBSTITUTE TEXT
replaceText = re.sub('MAT', 'MATEDIT', text)
print(replaceText)
# Output:
# 101 COM Computers
# 205 MATEDIT Mathematics
# 205 MATEDITX Mathematics Extra
# 189 ENG English

# EXTRACTING DATA
numbInText = re.findall('[0-9]+', text)
print(numbInText)
# Output:
# ['101', '205', '205', '189']

# Extract Specific Condition
## Find all capital char that have length minimum 3 chars
findCapitalText = re.findall('[A-Z]{3}', text)
print(findCapitalText)
# Output:
# ['COM', 'MAT', 'MAT', 'ENG']

# Find -> computers,mathematics,english
findCourses = re.findall('[A-Za-z]{5,}', text)
print(findCourses)
# Output:
# ['Computers', 'Mathematics', 'Mathematics', 'Extra', 'English']