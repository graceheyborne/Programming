#!/usr/bin/env python
# coding: utf-8

# In[1]:


# use a standard function to filter a list to a desired threshold.


# In[2]:


input_list = [1,2,3,4,5,6,7,8,9]

def threshold_function(input_list):
    new_list = []
    threshold = 7
    for x in input_list:
        if x > threshold:
            new_list.append(x)
    return new_list

threshold_function(input_list)

