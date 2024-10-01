#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# use a while loop to return the inner most part of a list + 1. 
input_list= [1,3,5,7,9,[2,4,6,8,[10,11,12]]]
output_list= []

def while_function(input_list): 
    x = input_list 
    while isinstance(x[-1], list): 
            x = x[-1] 
    for num in x: 
        output_list.append(num + 1) 
    return output_list

while_function(input_list)

