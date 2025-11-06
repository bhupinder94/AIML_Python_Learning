#!/usr/bin/env python
# coding: utf-8

# 
# # Day 2 - Control Flow in Python
# # Author: Bhupinder Garg
# 
# if / elif / else – decisions
# 
# for loops – repeating tasks
# 
# while loops – continuous repetition
# 
# break, continue, and pass

# In[1]:


print('welcome to day 2: control flow in python!')


# In[2]:


# if /elif/ else statements
age = int(input('enter your age:' ))
if age < 18:
    print('you are a minor')
elif age < 65:
    print('you are a adult')
else:
    print('you are a seniorcitizen')    

                


# In[3]:


# for loop exmple
for i in range (67,78):
    print('numberis:', i)


# In[5]:


# while loop example
count = 0
while count<= 5:
    print('count is:', count)
    count += 1
    


# In[33]:


# break, continue, pass statements
for i in range (1, 11):
    if i == 5:
     break
    print(i)
print('loop stopped at 5')

  





# In[46]:


# break, continue, pass statements

for j in range(1, 6):
    if j == 3:
        continue
    print(j)
print('value 3 is skipped')


# In[12]:


for k in range (1, 12):
 if k == 4:
      pass
 print(k)
print('value passed at 4')






# In[16]:


# small project : student grading system
marks = int(input('enter your marks:'))
if marks >=  90:
    grade = 'A+'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade= 'B'
elif marks >= 60:  
    grade   = 'C'
else:
    grade = 'Fail'
    print('your number is:', grade)






# In[ ]:




