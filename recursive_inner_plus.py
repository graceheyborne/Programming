#!/usr/bin/env python
# coding: utf-8

# In[1]:


input_list= [1,3,5,7,9,[2,4,6,8,[10,11,12]]]
output_list= []

def recursive_function(input_list): 
    if all(not isinstance(num, list) for num in input_list):
        for index in input_list: 
            output_list.append(index + 1) 
    else:
        for newnum in input_list:
            if isinstance(newnum, list):
                recursive_function(newnum)
    return output_list
      
recursive_function(input_list)

