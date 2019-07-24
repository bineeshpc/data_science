
#%%
# Python essentials
## Data types in python

#%% [markdown]
# a = 3

#%%
a

#%% [markdown]
# # Data types in python
# - Bool: True/False
# - int: 2, 10
# - float: 3.4, 4.0, -2.0
# - String: "Hello world"
# - Time: Data/time type
# 

#%%
type(a)


#%%
type(4.2)


#%%
type(True)


#%%
type('I am a Data Scientist')


#%%
import datetime


#%%
datetime.date.today()


#%%
datetime.datetime.now()


#%%
from datetime import datetime, date


#%%
date.today()


#%%
# Create a date
my_dads_bday = date(2010, 7, 15)
my_dads_bday


#%%
print(date.today() - my_dads_bday)


#%%
my_bday = date(2011, 7, 15)
my_dads_bday - my_bday


#%%
my_bday - my_dads_bday


#%%
date.today() - my_dads_bday


#%%
import datetime
# Time delta - to add 100 days from today
# hund_day = date.today() + 100 - Gives error 100 is int

hund_day = date.today() + datetime.timedelta(days=100)
hund_day

#%% [markdown]
# # Typecasting
# 

#%%
# Order of conversion
# Bool -> Int -> Float -> Str


#%%
# Auto Typecasting
3 + 4.0


#%%
# Forced typecasting
3 + int(4.5)


#%%
float(2)


#%%
bool(5)


#%%
int(True)


#%%
float(True)


#%%
str(True)


#%%
int(bool(-18))

#%% [markdown]
# # Read about Polynomial, multinomial, Linear Algebra, Matrices

#%%
str('6') + str('datamites')


#%%
4.5 + 5 + bool(-8) + int('6') + 3.5 + True


#%%
text = 'I am Data Scientist'
text


#%%
# Index in python starts from zero
text[5]


#%%
# Slicing operation ':', [Start:stop:step]
# This excludes the last element
# 5:12 takes from index 5 to 11 not from 5 to 12
text[5:12]


#%%
text[5:12:2] # Steps take alternative characters


#%%
text[5:-1] # 5 to the last but 1 number


#%%
text[50:-1] # 50 is not there, python returns empty string


#%%
len(text)


#%%
# Math operators
## +, -, *, /, //, power, modulus

10 + 4 # add
10 - 4 # subtract
10 * 4 # multiply
10 / 4 # float divide
10 // 4 # integer divide
10 ** 4 # power
10 % 4 # modulus


#%%
5 > 3


#%%
5 >=3


#%%
5 != 5


#%%
False and -2.0


#%%
5 > 3 and 6 > 3


#%%
5 > 3 and 5 < 3


#%%
# Conditional statements
x = 2
if x > 0:
    print("this is positive")
elif x == 0:
    print("this is zero")
else:
    print("this is negative")


#%%
# Numpy stands for numerical python
# We will deal with it later

# Array is a collection of same data type

#%% [markdown]
# # Lists
# - List is a heterogeneous data structure
# - Python lists are very flexible and can hold completely heterogeous, arbitrary data and they are also appended very efficiently
# 

#%%
a = [3, 4.5, True, 'DataMites']

type(a)


#%%
a[3]


#%%
myfamily = ['dad', 'mom', 'me']
myfamily


#%%
myfamily.append('wife')


#%%
myfamily


#%%
myfamily.extend(['son', 'brother'])
myfamily


#%%
myfamily.remove('brother')
myfamily


#%%
myfamily.pop(4)
myfamily


#%%
myfamily.sort()
myfamily


#%%
myfamily.sort(reverse=True)
myfamily


#%%
# myfamily.reverse()
# myfamily


#%%
myfamily.count('dad')


#%%
myfamily[0:5:2]

#%% [markdown]
# # Tuple
# - Immutable Ex: call log
# 

#%%
a = tuple([3, 4, 5])
print(a)
type(a)


#%%
(3, 4, 5) # creating a simple tuple

#%% [markdown]
# # Dictionary

#%%
b = dict(name='Sagar', job='data scientist')
b


#%%
b['name']


#%%
c = {1: 2, 3: 4}
c

#%% [markdown]
# # Sets

#%%
lang = set(['Java', 'C', 'Python'])
snakes = set(['cobra', 'Mambo', 'Python'])
snakes


#%%
lang


#%%
lang.intersection(snakes)


#%%
lang.union(snakes)


#%%
lang.difference(snakes)


#%%
a = (1, 2, 3)

#%% [markdown]
# # Functions
# 

#%%
def bmi(weight, height):
    """ Weight in kilograms
    Height in metres
    """
    return weight / (height ** 2)

bmi(80, 1.76)

#%% [markdown]
# # For loop

#%%
fruits = ['guava', 'cherry', 'mango', 'apple']
type(fruits)


#%%
for f in fruits:
    print(f)


#%%
for f in fruits:
    if f == 'cherry':
        print('hi cherry')
    print(f)


#%%
for i in range(1, 3):
    print(i)


#%%
import datetime as dt
today = dt.date.today()
today


#%%
type(today)


#%%
today.month


#%%
# John Mccarthy
# Geoffrey hilton
# Yann Lecun
# Andrew ng




