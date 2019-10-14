#!/usr/bin/env python
# coding: utf-8

# # Numpy - Numerical python

# In[73]:


# Numpy array is homegeneous

import numpy as np

a = np.array([4.5, 5, 6, 'data'])
a


# In[74]:


c = np.array(['abcd', '5', 6])
c


# In[75]:


a = np.array([4, 5, 6, 8])
print(a)
print('size of array: ', a.size)
print('datatype of the array', a.dtype)
print('Dimension of the array', a.ndim)
print('Shape of the array', a.shape)

print('type of the array', type(a))


# 2d array is a collection of one dimensional array

# In[76]:


a = np.array([[4, 5, 6, 8], [8, 4, 26, 18], [8, 52, 16, 22] ])
print(a)
print('size of array: ', a.size)
print('datatype of the array', a.dtype)
print('Dimension of the array', a.ndim)
print('Shape of the array', a.shape)

print('type of the array', type(a))


# collection of one dimensional arrays
# Dont think about this as rows and columns
# Rows and columns are in pandas.
# Do not get confused

# In[77]:


a = np.array([[4, 5, 6, 8], [5]])
print(a)
print('size of array: ', a.size)
print('datatype of the array', a.dtype)
print('Dimension of the array', a.ndim)
print('Shape of the array', a.shape)

print('type of the array', type(a))


# In the above case it is not a 2 d array anymore
# because one of the lists contains only 1 element.
# 
# It becomes a 1 dimensional array with 1 object
# 
# 3 dimensional array is a collection of 2 d array and so on
# 

# In[78]:


a = np.array([
    
   [ [4, 5, 6, 8], [8, 4, 26, 18], [8, 52, 16, 22] ],

   [  [4, 5, 6, 8], [8, 4, 26, 18], [8, 52, 16, 22] ]


])
print(a)
print('size of array: ', a.size)
print('datatype of the array', a.dtype)
print('Dimension of the array', a.ndim)
print('Shape of the array', a.shape)

print('type of the array', type(a))


# In[79]:


a[1]


# In[80]:


a[1][0]


# In[81]:


a[1][0][0]


# In[82]:


a[1,0,0]


# Any kind of data used for artificial intelligence finally ends up in numpy in python
# 
# April fool joke of communicating with plants by google
# 
# 

# In[83]:


print(np.arange(10))


# In[84]:


print(np.arange(10, 20))


# starting position is included, excludes the end position

# In[85]:


print(np.arange(10, 20, 2))


# # np.linspace() Linear space

# In[86]:


np.linspace(10, 50, 3)


# give me 41 numbers equally spaced between 10 and 50 including both numbers
# 
# linspace is useful to generate sample space
# 
# 

# In[87]:


np.linspace(10, 50, 41)


# In[88]:


np.arange(24)


# In[89]:


b = np.arange(24).reshape(4, 6) # . is also used for piping
b


# In[90]:


b.shape


# In[91]:


b.reshape(2, 3, 4)


# In[92]:


c = b.reshape(1,3,2,2,2)
c


# In[93]:


c.shape


# In[94]:


d = b.reshape(2, 2, 2, 3, 1, 1)
d


# In[95]:


d.shape


# In practice we play with one or two dimensions

# In[96]:


# ravel flatten an array back to single dimension


# In[97]:



d.ravel()


# # np.random.rand()
# random subpackage
# 

# In[98]:


# 16 digit decimal precision number between 0 and 1
np.random.rand()


# In[99]:


np.random.rand() * 100


# In[100]:


# number between 35 and 100
# min + rand() * (max - min)
35 + int(np.random.rand() * 65) 


# In[101]:


def random_between(min_value, max_value):
    """ A fuction which returns an integer between min_value and max_value
    """
    return min_value + int(np.random.rand() * (max_value - min_value))

random_between(65, 70)


# In[102]:


# 5 ranodm numbers between 0 and 1
np.random.rand(5)


# In[103]:


# 3 x 4 2d array
# takes any shape and gives a random array of that shape
np.random.rand(3, 4)


# In[104]:


# randint
# what we wrote above
np.random.randint(35, 100)


# In[105]:


# 100 numbers between 35 and 100
np.random.randint(35, 100 ,100)


# In[106]:


np.random.randint(35, 100, 100).reshape(20, 5)


# In[107]:


# numpy is very efficient
np.sqrt(np.random.randint(35, 100, int(1e6)).reshape(int(1e3), 1000))


# In[109]:


np.log(np.pi)


# In[111]:


a = np.arange(24).reshape(4, 6)


# In[112]:


a


# In[116]:


np.hsplit(a, 2)


# In[114]:


np.vsplit(a, 2)


# In[118]:


np.hstack((a, b))


# In[119]:


np.vstack((a, b))


# In[121]:


a = [4, 5, 6]

b = a

print(a, b)

a[1] = 500

print(a, b)


# In[122]:


a = [4, 5, 6]

b = a.copy() # deep copy

print(a, b)

a[1] = 500

print(a, b)


# In[ ]:




