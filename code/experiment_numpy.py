# %%
import numpy as np



#%%
a = np.arange(35)
five_by_seven = a.reshape(5, 7)
five_by_seven


#%%
seven_by_five = a.reshape(7, 5)
seven_by_five
#%%
try:
    np.vstack((five_by_seven, seven_by_five))
except ValueError:
    print("number of columns must be same")
#%%
two_by_seven = np.arange(14).reshape(2, 7)

np.vstack((five_by_seven, two_by_seven))

#%%

try:
    np.hstack((seven_by_five, two_by_seven))
except ValueError:
    print("number of rows must be same")

#%%
seven_by_two = np.arange(14).reshape(7, 2)
np.hstack((seven_by_five, seven_by_two))

#%%

np.random.random()

#%%
np.random.random((2, 5))

#%%
m = np.floor(100 * np.random.random((2,6 )))
m
#%%
np.floor(10.4)

#%%
np.ceil(10.4)

#%%
np.hsplit(m, 3)

#%%
n = np.floor(100 * np.random.random((8 ,3 )))
n
#%%
x = np.vsplit(n, 2)
x[0].shape
#%%

p = np.array([1, 2, 3, 4, 5])
p

#%% [markdown]
# reference of p is created instead of copying p to q
# 
#%%
q = p
q
#%%
p[3] = 400
q
#%%
q = p.copy()
q

#%%
p[3] = 4
p
#%%
q

#%%
