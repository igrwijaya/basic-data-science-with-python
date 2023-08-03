#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Assignment Operator

x = 8
y = 10
print(x+y)


# In[8]:


# Comparison Operator

a = "wadah gula aren"
b = "gula aren"
print(len(a))
print(len(b))
print(a > b)


# In[13]:


# Logical Operator

x = 7
y = 8
print(x == 8 and y == 8)
print(x == 8 or y == 8)


# In[18]:


z = (x == 8 or y == 8)
print(z)


# In[29]:


# Data Structure
## List
## list can be added, update, remove

students = ["Toni", "Gede", "Wahyu"]
print("initial list:", students)

## to add item to list
students.append("Yono")
print("add item to list:", students)

## to remove last item in list
students.pop()
print("remove last item in list:", students)

## to remove specific item in list
students.pop(0)
print("remove specific item in list:", students)

## to edit item in the list
students[1] = "Wijaya"
print("edit item in the list:", students)

randomVals = [1, "Budi", False]
print(randomVals)


# In[31]:


# Data Structure
## Tuples
## tuples cannot added or update or remove. Initial / read only

## initial Tuples
scores = ("20", "40", "80")
print(scores)

