#!/usr/bin/env python
# coding: utf-8

# What is a Function?
# 
# A function is reusable code that performs a specific task.

# In[ ]:


# day 3 - Functions in python
#author : Bhupinder Garg

print('welcome to day 3: Functions and Modular Programming!')


# In[ ]:


# basic syntex

def greet():
   print('hello Bhupinder! welcome to functions.')
greet()


# In[2]:


# Function With Parameters
def welcome(name):
 print('Welcome!', name)
welcome('bhupinder')
welcome('AI Learner')
welcome('we will achieve our goals together with dedication, hard work and consistant patience')


# In[ ]:


# Function With Return Value
def add(a, b):
    return a + b
result = add(43343,56674)
print('Addition =', result)


# In[2]:


# multiple returns
def calculation(a, b):
    return a+b, a*b, a-b, a//b
sum, product, difference, division = calculation(4,5)
print('sum =', sum)
print('product =', product)
print('difference =', difference)
print('division =',division)


# In[1]:


print('working everything fine!')
print("working")


# In[5]:


#Function with multiple returns
from os import sep


def operations(x, y):
    sum = x+y
    diff = x-y
    prod = x*y
    div = x/y
    return sum, diff, prod, div
a, d, p, q = operations(4545448, 784444)
print(a, d, p, q, sep = '\n')


# In[13]:


#Default Arguments
#very useful for aiml funnction later
def greet(name = 'Bhupinder', Greeting = 'hello', Goal = 'AIML Mastery', sep = ' '):
    print(Greeting, name, 'how are you? I hope you are enjoying your journey toward', Goal, '.')

greet()
greet('John')

   



# In[2]:


# Keyword Arguments(order doesnt matter)
def intro(name, age, skill):
    print(f'My name is {name}. I am {age} years old and I am learning {skill}.')
intro(skill = 'AIML', age = 30, name  = 'Bhupinder')





# In[ ]:


# args - Unlimited input arguments
def math_all(*numbs):
   # """Return (sum, product, subtraction, division) over the supplied numbers."""
    if not numbs:
        raise ValueError('math_all requires at least one numeric argument')
    # sum
    add = sum(numbs)
    # product
    mult = 1
    for n in numbs:
        mult *= n
    # subtraction: start from first item and subtract the rest
    sub = numbs[0]
    for n in numbs[1:]:
   
        sub -= n
    # division: start from first item and divide by the rest (check for zero)
    div = numbs[0]
    for n in numbs[1:]:
        if n == 0:
            raise ZeroDivisionError('division by zero encountered in math_all')
        div /= n
    return add, mult, sub, div
result = math_all(5858, 5879, 4681, 3555, 4844)
sum_res, prod_res, sub_res, div_res = result
print('Sum =', sum_res)
print('Product =', prod_res)
print('Subtraction =', sub_res)
print('Division =', div_res)









# In[ ]:


def total_price(*prices, tax_rate  = 0.05):
     total = sum(prices)
     total += total * tax_rate
     return total
result = total_price(642, 154, 14845,  155)
print('total price =', result)



# In[1]:


#kwargs - unlimited key- value inputs

def profile(**info):
    print(info)

profile(name='Bhupinder', domain='AIML', goal='startup', year=2025)







# In[7]:


# combining everything - Pro Level Functions88
def smart_functions(a, b, *extra, operation='add', **info):
 print('extra values', extra)
 print('Additional info:', info)

 if operation == 'add':
  return a + b
 elif operation == 'mul':
  return a * b
 else:
  return 'unknown operations'
 
print(smart_functions(54,44,84,48, operation='mul', project='AI'))

  


# In[7]:


# PRACTICE EXERCISES(MUST DO)
#Exercise 1 write a function that gives maximum of 3 numbers

def max_of_three(a,b,c):
    return max(a,b,c)
print(max_of_three(242,4343,543))

#exercise 2 right a function to count how many vowels are in this string:

def count_vowels(string):
    vowels = ('aeiouAEIOU')
    count = 0
    for chr in string:
        if chr in vowels:
            count += 1
    return count
print(count_vowels('My name is Bhupinder and  I am a student of AIML'))                
            

# Exercise 3 : Write a function that returns only even numbers from a list?

# Option A: accept an iterable (list/tuple)
def get_even_from_list(nums):
    even = []
    for n in nums:
        if n % 2 == 0:
            even.append(n)
    return even

print(get_even_from_list([484,84,44844,48,15,181,47]))

# Option B: accept variable arguments (convenient for calling with comma-separated numbers)
def get_even(*nums):
    even = []
    for n in nums:
        if n % 2 == 0:
            even.append(n)
    return even

print(get_even(484,84,44844,48,15,181,47))



# exercise 4 write a function that checks if a number is prime?
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n//2+1):
        if n%i ==0:
            return False
        
    return True
prime = int(input('enter no.'))

print(is_prime(prime))
        


# In[9]:


# project : Smart Calculator(2.0 Function Based)

# Step 1 - Create the core functions

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if b == 0:

       return 'error: cannot divide by zero'
    return a/b



def smart_calc():
    print('=== smart calculator 2.0 ===')
    print(' Available Operations: +, -, *, /')

    try:

 
        a = float(input("enter no."))
        b = float(input('enter second no.'))
        op = input('+, -, *, / ')

        if op == '+':
            print('result:',  add(a, b))
        elif op == '-':
            print('result =', sub(a, b) )
        elif op == '*':
            print('result =', mul(a,b))
        elif op == '/':
            print('result =',div(a,b) )
        else:
            print('unknown operation')
    except ValueError:
        print('Invalid input: Please enter numbers only')

    return None

smart_calc()

   
    
    

