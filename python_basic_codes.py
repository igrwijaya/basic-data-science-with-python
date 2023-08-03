#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ---------------------------------------------- #
# Assignment Operator

x = 8
y = 10
print(x+y) # output: 18
# ---------------------------------------------- #


# In[ ]:


# ---------------------------------------------- #
# Comparison Operator

a = "wadah gula aren"
b = "gula aren"
print(len(a)) # output: 15
print(len(b)) # output: 9
print(a > b) # output: True
# ---------------------------------------------- #


# In[ ]:


# ---------------------------------------------- #
# Logical Operator

x = 7
y = 8
print(x == 8 and y == 8) # output: False
print(x == 8 or y == 8) # output: True

z = (x == 8 or y == 8)
print(z) # output: True
# ---------------------------------------------- #


# In[ ]:


# ---------------------------------------------- #
# Data Structure
# List
# list can be added, update, remove

students = ["Toni", "Gede", "Wahyu"]
print(students) # output: ['Toni', 'Gede', 'Wahyu']

# to add item to list
students.append("Yono")
print(students) # output: ['Toni', 'Gede', 'Wahyu', 'Yono']

# to remove last item in list
students.pop()
print(students) # output: ['Toni', 'Gede', 'Wahyu']

# to remove specific item in list
students.pop(0)
print(students) # output: ['Gede', 'Wahyu']

# to edit item in the list
students[1] = "Wijaya"
print(students) # output: ['Gede', 'Wijaya']

randomVals = [1, "Budi", False]
print(randomVals) # output: [1, 'Budi', False]
# ---------------------------------------------- #


# In[ ]:


# ---------------------------------------------- #
# Data Structure
# Tuples
# tuples cannot added or update or remove. Initial / read only

# initial Tuples
scores = ("20", "40", "80")
print(scores) # output: ('20', '40', '80')
# ---------------------------------------------- #


# In[ ]:


# ---------------------------------------------- #
# Data Structure
# Set
# set is collection of unique data / value


# initial Set
ingridients = {"salt", "salt", "sugar"}
print(ingridients) # output: {'salt', 'sugar'}

# parse as Set from List
students = ["Budi", "Tono", "Wayan", "Tono"]
print(set(students)) # output: {'Budi', 'Tono', 'Wayan'}
# ---------------------------------------------- #


# In[ ]:


# ---------------------------------------------- #
# Data Structure
# Dictionary
# Dictionary is collection with "key" and "value"

# initial dictitonary
profile = {}
profile['name'] = 'Gede'
profile['email'] = 'wijaya@mailinator.com'
print(profile) # output: {'name': 'Gede', 'email': 'wijaya@mailinator.com'}

# get by key
print(profile['name']) # output: Gede

# update by key
profile['name'] = 'Wijaya'
print(profile['name']) # output: Wijaya

# delete by key
del profile['email']
print(profile) # output: {'name': 'Wijaya'}
# ---------------------------------------------- #


# In[ ]:


# ---------------------------------------------- #
# Flow Control

# if..else

studentScore = 8

if studentScore > 7:
    print('Passed')
elif studentScore < 7:
    print('Not Passed')
else:
    print('Study Over Again')
# output: Passed

randomNumb = 80

if randomNumb % 2 == 0:
    print(randomNumb, 'is', 'an Even Number')
else:
    print(randomNumb, 'is', 'an Odd Number')
# output: 80 is an Even Number
# ---------------------------------------------- #


# In[3]:


# ---------------------------------------------- #
# Flow Control

# while..loop

age = 1

while(age < 5):
    print(age, "is", "not Adult")
    age += 1
# output:
# 1 is not Adult
# 2 is not Adult
# 3 is not Adult
# 4 is not Adult
# ---------------------------------------------- #


# In[6]:


# ---------------------------------------------- #
# Flow Control

# for..loop
courses = ['DSC', 'BI', 'FSD']

for course in courses:
    print(course)
# output:
# DSC
# BI
# FSD

# using "break" in for..loop (break = force stop the looping process)
for course in courses:
    print(course)    
    if course == 'BI':
        break
# output:
# DSC
# BI

# using "continue"  in for..loop (contine = to skip the rest of logic and contine to the next looping process)
for course in courses:
    if course == 'DSC':
        continue
    print(course)
# output:
# BI
# FSD

# ---------------------------------------------- #


# In[10]:


# ---------------------------------------------- #
# Function
# Function without Parameters
def renderName():
    print('Gede')

# call function
renderName() # output: Gede

# Function with Parameters
def calculateCustomerPayment(totalPrice, qty, discount):
    totalPayment = (totalPrice * qty) - discount
    print(totalPayment)

# call function
calculateCustomerPayment(1000, 2, 100) # output: 1900

# Function with Default Parameters
def calculatePrice(itemPrice, comission = 100):
    price = itemPrice + comission
    print(price)
    
# call function
calculatePrice(1000) # output: 1100

# ---------------------------------------------- #


# In[ ]:


# ---------------------------------------------- #
# User Input

#age = input("Your age:") # by default the data type is string
# ---------------------------------------------- #

