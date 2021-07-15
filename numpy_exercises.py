#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1, 2, 3])
a


# In[3]:


matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix


# In[4]:


a[0]


# In[5]:


print('a    == {}'.format(a))
print('a[0] == {}'.format(a[0]))
print('a[1] == {}'.format(a[1]))
print('a[2] == {}'.format(a[2]))


# In[6]:


matrix[1, 1]


# In[7]:


should_include_elements = [True, False, True]
a[should_include_elements]


# In[8]:


original_array = np.array([1, 2, 3, 4, 5])
original_array + 1


# In[9]:


my_array = np.array([-3, 0, 3, 16])

print('my_array      == {}'.format(my_array))
print('my_array - 5  == {}'.format(my_array - 5))
print('my_array * 4  == {}'.format(my_array * 4))
print('my_array / 2  == {}'.format(my_array / 2))
print('my_array ** 2 == {}'.format(my_array ** 2))
print('my_array % 2  == {}'.format(my_array % 2))


# In[10]:


my_array = np.array([-3, 0, 3, 16])


# In[11]:


my_array[my_array > 0]


# In[12]:


my_array[my_array % 2 == 0]


# In[ ]:




