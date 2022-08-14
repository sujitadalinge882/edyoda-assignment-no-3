#!/usr/bin/env python
# coding: utf-8

# In[36]:


# write a python program to count the number of even and odd numbers from a series of numbers.
list=(21,3,4,6,33,2,3,91,50,60,70,58,40)
even_count,odd_count=0,0
for num in list:
    #even numbers 
    if num % 2 == 0:
        even_count += 1
    #odd numbers 
    else:
        odd_count += 1
print ("even numbers available in the list:",even_count)
print("odd numbers available in the list:",odd_count) 


# In[35]:


# write a python program to count the number of even and odd numbers from a series of numbers.nimbers
numbers=(15,10,97,4,5,6,7,8,95,15,14,30,40,45,48)
count_odd = 0 
count_even = 0 
for x in numbers:
    if not x % 2:
        count_even+=1
    else:
        count_odd+=1
print ("number of even numbers :",count_even)
print ("number of odd numbers :",count_odd)


# In[ ]:





# In[ ]:




