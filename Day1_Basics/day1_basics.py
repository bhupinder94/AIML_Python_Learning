#!/usr/bin/env python
# coding: utf-8

# # 🧠 Day 1 – Python Basics for AIML
# 
# ## 🎯 Goal:
# Understand how Python works, run your first code, and learn the core elements: variables, data types, and basic operations.
# 
# 
# 

# In[ ]:





# In[5]:


# my first python program
print('hello bhupinder! welcome to day 1 of python for AIML')

#VARIABLES
NAME = 'BHUPINDER'
GOAL = 'BUILD AIML SKILLS FAST'
YEAR = 2025
print(f'My NAME is {NAME}. My GOAL is to {GOAL} in YEAR {YEAR}.')


# In[8]:


#DATA TYPES
x = 10
y = 3.14
z = "Ai"
a = False
print(type(x), type(y), type(z), type(a))


# In[16]:


# INPUT and OUTPUT

user = ('AI Agent:')
print('i like to building', user)



# In[21]:


#Basic Calculator
a = float(input("Enter first number:"))
b = float(input('Enter second number:'))


print('Addition:', a + b)  
print('subtraction:', a-b)
print('Multiplication:', a * b)
print('Division:', a/b)


# In[23]:


#Basic Calculator
a = float(input("Enter first number:"))
b = float(input('Enter second number:'))


print('Addition:', a + b)  
print('subtraction:', a-b)
print('Multiplication:', a * b)
print('Division:', a/b)


# In[10]:


# basic math

a= 10 
b = 4
print('addition of the a and b is = ',a + b)
print(f'subtraction = {a-b}')
print(f'multiplication = {a * b}')
print(f'division = {a/b}')
print(f'floor division = {a // b}')
print(f'modulus = {a % b}')
print(f'exponent = {a**b} ')


# In[11]:


# comparison and logical operators

x = 7
y = 10

print(x > y)
print(x<y)
print(x == y)
print(x != y)
print(x > 5) and (y < 15)
print(x > 8) or (y < 8)
print(not(x > 5))


# In[12]:


name = input('bhupinder')
print('hello', name)


# In[ ]:




