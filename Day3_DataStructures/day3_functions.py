#!/usr/bin/env python
# coding: utf-8

# What is a Function?
# 
# A function is reusable code that performs a specific task.

# In[1]:


# day 3 - Functions in python
#author : Bhupinder Garg

print('welcome to day 3: Functions and Modular Programming!')


# Explanation:
# 
# def means define a new function.
# 
# greet() is the function name.
# 
# Everything inside (indented) is the function body.
# 
# You can call this function anytime by writing:
# 
# greet()
# 
# 
# 🟢 Think of it like:
# A machine that says “Hello” whenever you press a button.

# In[2]:


# basic syntex

def greet():
   print('hello Bhupinder! welcome to functions.')
greet()


# In[3]:


# Function With Parameters
def welcome(name):
 print('Welcome!', name)
welcome('bhupinder')
welcome('AI Learner')
welcome('we will achieve our goals together with dedication, hard work and consistant patience')


# Explanation:
# 
# a and b are parameters (inputs).
# 
# When you call add(10, 5) → it prints 15.
# 
# The function can be reused with any numbers.
# 
# 🟢 Think of it like:
# A calculator machine — you enter two numbers, it gives you the sum.

# In[4]:


def add(a, b):
 print(a+b)
add(2,3)  


# Explanation:
# 
# return gives back the value to the place where you called the function.
# 
# You can store the result in a variable (result) and use it later.
# 
# 🟢 Think of it like:
# A function that gives back the answer instead of printing it immediately.

# In[5]:


# Function With Return Value
def add(a, b):
    return a + b
result = add(43343,56674)
print('Addition =', result)


# You can return more than one value from a function.
# you get four results: sum, difference, multiply, divide.
# 
# 🟢 Think of it like:
# A machine that gives you all 4 math answers in one go.

# In[6]:


# multiple returns
def calculation(a, b):
    return a+b, a*b, a-b, a//b
sum, product, difference, division = calculation(4,5)
print(sum, product, difference, division )


# In[ ]:





# In[7]:


# multiple returns
def calculation(a, b):
    return a+b, a*b, a-b, a//b
sum, product, difference, division = calculation(4,5)
print('sum =', sum)
print('product =', product)
print('difference =', difference)
print('division =',division)


# In[8]:


print('working everything fine!')
print("working")


# In[9]:


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


# Explanation:
# 
# If you don’t pass a value, it uses the default one (“Bhupinder”).
# 
# You can also override it:
# 
# greet("John")
# 
# 
# 🟢 Think of it like:
# A vending machine that gives coffee by default, unless you ask for tea.

# In[10]:


#Default Arguments
#very useful for aiml funnction later
def greet(name = 'Bhupinder', Greeting = 'hello', Goal = 'AIML Mastery', sep = ' '):
   print(Greeting, name, 'how are you? I hope you are enjoying your journey toward', Goal, '.')

greet()
greet('John','hey','millionair')

   



# Explanation:
# 
# You can give arguments by name, so the order doesn’t matter.
# 
# 🟢 Think of it like:
# Labeling your inputs so the function knows exactly which is which.

# In[11]:


# Keyword Arguments(order doesnt matter)
def intro(name, age, skill):
    print(f'My name is {name}. I am {age} years old and I am learning {skill}.')
intro(skill = 'AIML', age = 30, name  = 'Bhupinder')
intro('money', 'das', 30)






# Explanation:
# 
# *numbers means you can give any number of values (1, 2, or 100).
# 
# Python treats them as a list inside the function.
# 
# 🟢 Think of it like:
# A basket that can hold any number of fruits — big or small.

# In[24]:


del sum


# In[26]:


print(sum)


# In[25]:


# args - Unlimited input arguments
def math_all(*numbs):
   # """Return (sum, product, subtraction, division) over the supplied numbers."""
    if not numbs:
        raise ValueError('math_all requires at least one numeric argument')
    
    # sum
    add_no = sum(numbs)
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
    return add_no, mult, sub, div
result = math_all(5858, 5879, 4681, 3555, 4844)
sum_res, prod_res, sub_res, div_res = result
print('Sum =', sum_res)
print('Product =', prod_res)
print('Subtraction =', sub_res)
print('Division =', div_res)









# In[22]:


print(sum)


# In[27]:


def total_sum(*numbers):
  return sum(numbers)
total_sum(1,26,8,48,5)

  




# In[29]:


def total_price(*prices, tax_rate  = 0.05):
     total = sum(prices)
     total += total * tax_rate
     return total
result = total_price(642, 154, 14845,  155, tax_rate = 0.09)
print('total price =', result)



# Explanation:
# 
# **info collects all key=value pairs into a dictionary.
# 
# You can store multiple named details easily.
# 
#  Think of it like:
# Packing details into a box with labels — name, goal, year, etc.

# In[ ]:


#kwargs - unlimited key- value inputs

def profile(**info):
    print(info)

profile(name='Bhupinder', domain='AIML', goal='startup', year=2025)







# In[32]:


def profile(**info):
    return(info)

total = profile(name='Bhupinder', domain='AIML', goal='startup', year=2025)
print(total)


# In[ ]:


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

  


# In[ ]:


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
        


# In[ ]:


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

   
    
    

