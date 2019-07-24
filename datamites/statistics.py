

#%% [markdown]

# # Statistics
# I cover only 30% of what you should know

# Any research statistics can prove or disprove a theory

# research
# Statistics is essential block for any researcher

# ## Descriptive statistics

# Eg. Sales graph provides a summary of sales, 
# You can identify the trend

# mean, standard deviation, mode etc.

# Descriptive statistics is bare minimum you should know 
# to run a business.


# BI(Business intelligence) tools like tableau
# 100 percent data presented in an informative manner
# tableau visual analytics

# ## Inferential statistics
# Your are infering the output of something from data.

# Exit polls
# population, china, India

# Ask few thousands of people

# How many percentage of people are voting for party x

# Using the subset of the population
# Take a Sample population
# Study sample.
# Conclude for entire population.

# Field is called inferential statistics.

# You can plot charts
# Read the same topic from at least 3 different sources

# Confusion is better, because then you research more

# A conflict will make you remember

# Go for critical reading

# Terms
# ## Population 
# (grains in sand) Infinite population, Finite population
# ## Sample
# sample of pupulation
# population is 1 cr
# sample is 30 lakhs
# 30 % is married out of 30 lakhs
# error = parameter - statistic

# ## Variable


# Women safety perception survey in bangalore

# total poulation of bangalore = 1 cr
# women population = 30 lakhs
# 30 lakhs 50 50 possibility
# about 60 percent come under safety research
# Demographics of india wikipedia page

# https://en.wikipedia.org/wiki/Demographics_of_India

# Age, Working?, Location, Working in night shift?, Skills, Education, Married?

# Variables are the ones where we get answers for

# What we collect here is 

# 35, y, BTM, Software Engineer|Music player, N, PG, Y

# Single valued variables
# Singular data
# statistic (singular without s) is a summary of a sample
# 

# Sampling error
# parameter - statistic
# 
# Skills plural data

# Multivalues are hard to analyse

# Singular data is easy to analyse

# OneHotEncoding

# Software Engineer| Musician
# Finance | LLB
# ....

# Skills can be converted to singular variable

# Skills_Software_Engineer
# Skills_Finance
# Skills_Musician

# one hot encoding

# Converting a plural data into singular data

# Skills_Software_Engineer 0
# Skills_Finance 1
# Skills_Musician 0

# Variable is either 0 or 1

# ## Experiment

# Pediasure

# 40 kids

# 20 pediasure 20 milk
# Experiment

# # Data 

# ## Numerical data
# Made of numbers
# ### Continuous data
# Age, weight, blood pressure, temperature
# ### Discrete data
# 
# ## Categorical data
# Eye colourr, gender blood type, ethnicity
# ### Ordinal data
# With order
# ### nominal data
# BMW, Tata, battery is defective or not
# 

# Qualitative and quantitative data
# Qualitative is called categorical data

# Blood group is nominal by nature
# This can be converted to ordinal by ordering it by
# availability or rareness

# by attaching some thing to it

# dog breed nominal, arranged in order of height is ordinal

# Amazon review, ordinal
# Employee appraisal, categorical ordinal

# Discrete data
# Numerical
# Shoe size
# Predefined discrete data
# Number of children

# Step size in discrete data need not be same

# ## Continous variable
# same as Ratio data
# ## Discrete variable
# Same as interval

# Examples

# length of time continuous
# number of chocolates discrete
# brand nominal
# overall satisfaction rate ordinal
# number of files discrete
# ph level continuous
# number of staples discreted

# Age
# continuous data

# 26, 25, 30, 40, 23, 60, 50
# Discrete
# Between range
# Interval
# 0-10  5(mid value)
# 11-20 15
# 20-30 25
# 30-40 35

# By taking mid values of the interval you can convert 
# a continuous variable to a discrete variable

# young, mid, old ordinal categories can be made from 
# the discrete data
# by defining a certian > or < operator

# Can it be converted to nominal data

# < 15 age and > 60 age play arcade games
# mario pacman arcade games

# Group1, Group2, Group3
# These groups does not have any order
# because both 15 year olds and 60 year olds are interested in playing
# these games


# losing information as we go right in that slide(review)


# # Making sense of data
# Harnessing data
# Sampling
# ## With replacement
# You put it back and take again
 
# ## Without replacement
# Eg. lottery ticket
# Third price winner cannot win the first price as well

# 10000 people survey on employee satisfaction
# Random sample is the only valid
# Non random invalid
# ## Simple random sample
# Every employee equal probability of getting picked up
# ## Stratified sample
# IT, Student, Textile, House wives, Teachers, Others
# Principle of mutually exclusive and collectively exhaustive
# Group should not overlap
# All groups put together should cover the population
# strata means group

# 70 80 % will use stratified sampling
# achieving this can be default
# Different channel for different strata

# ## Cluster sample
# Sampling the strata itself
# Read about this
# As data scientists you may not encouter this kind of sampling

# ## Systematic
# Perspective difference
# people who has been there for long time(management decision is not good, strategy is not good)
# people who are 5 months old (coffee machine is not working, work hours)

# E0001
# E0002
# Employee number is sequential
# Every 100th employee to surveyed
# 
# Working with organization systematic is good

# ## Biased Sampling
#  Cultural diff Business survey done for PHD University of amsterdam
# Tolerance - US less tolerant
# Germany - 10 O clock meeting 5 minute early(9:55)
# India - 15 minutes early India are yes people

# 10 managers from each region
# china, india, uk, usa

# convenient sampling(Biased sampling)
# Doing the sampling of people who are university of amsterdam students

# a small error can happen because of convenient sampling

# This can be offset by using certain techniques

# ## Volunteer Sampling 
# is not recommended
# volunteers are usually affected. 
# They have a strong bias towards a topic.

# # Exploratory analysis
# ## EDA Exploratory data analysis

# ## Central tendency tendencies: Mean median and mode
# ### Mean
# ### Median
# ### Mode


#%%
import numpy as np
# INR thousands per month
org_a_salaries = [80, 75, 100, 45, 30, 45, 65, 120, 1500]
org_b_salaries = [90, 85, 60, 60, 80, 69, 75, 35, 130]

print(np.mean(org_a_salaries))
print(np.mean(org_b_salaries))


#%%

import scipy as sp

from scipy import stats

print('mean of the salaries company A', sp.mean(org_a_salaries))
print('mean of the salaries company B', sp.mean(org_b_salaries))

print('median of the salaries company A', sp.median(org_a_salaries))
print('median of the salaries company B', sp.median(org_b_salaries))

print('mode of the salaries company A', sp.stats.mode(org_a_salaries))
print('mode of the salaries company B', sp.stats.mode(org_b_salaries))


#%%

# ## Mean is failing because of an outlier
# Mean is not a good measure if data has extreme values

# Median is preferred in this case
# Median is middle value
# ## Median
# Dividing the data into two equal parts

# 50 percent are getting below it
# 50 percent are getting above it
# Measures of tendency you consider both mean and median

# 

#%%
# Measures of variability

train_a = [10, 15, 12, 17, 20]
train_b = [2, 30, 15, 5, 28]

print('Mean of train a:', sp.mean(train_a))
print('Mean of train b:', sp.mean(train_b))


print('Median of train a:', sp.median(train_a))
print('Median of train b:', sp.median(train_b))

# Wide variation for train b
# measures of central tendency is insufficient to understand this


#%%

# ## Methods of variability
# Range  Max - Min of a distribution
# Range is a measure of variability 
# Equal to max - min

#%%

max_a = max(train_a)
min_a = min(train_a)

max_b = max(train_b)
min_b = min(train_b)

print('Train a', max_a - min_a)
print('Train b', max_b - min_b)

#%%

# Range is not a great measure
# One bad day can screw it up


# #%%
# mean is 15

# 10 - 15 5 25  
# 15 - 15 0 0
# 20 - 15 5 25

# (25 + 0 + 25) / (3 - 1)
# correction for sampling error

# use n-1 instead of n

# mean of the squares of the deviation 

# https://en.wikipedia.org/wiki/Bessel%27s_correction

# Standard deviation
# squareroot of variance
# 6 8 12
# find standard deviation manually
# 6  8.7 7.28  
# 8  8.7 0.48
# 12 8.7 10.89

# variance 6.21

# std 3.105
#%%
(7.28 + 0.48 + 10.89 ) / 3

6.21 ** 1/2

#%%

np.std([6, 8, 12])

#%%

# Blood pressure

# BP 120/80

# Stress
# Social media psychology
# Hypothetical paper

# Lion entering the den
# caveman
# Lion / Wife / Husband / Boss
# EMI
# Fight or flight
# Smile
# Punching bags in office and on the road

# BP
# systolic blood pressure
# 

# 120, 125, 130, 140, 110, 115, 110

# # Histogram is a frequency distribution plot
# Blood pressure in mmhg
# Systolic blood pressure

# Important graph

# Normal curve
# Normally occurs
# Bell curve
# Gaussian distribution

# Z values or standard values
# +1 sigma + 2 sigma
# -1 sigma - 2 sigma
# How many times I am away from the mean

# mu = 120
# sigma = 10
# x = mu + z * sigma

# 120 + 1.5 * 10 = 135

# bp is 90

# 95 = 120 + z * 10
# -25 = z * 10
# z = -2.5

# z = (x - mu) / sigma

# Empirical rule
# Normal distribution

# 68% percent of data is going to be in between -1sigma and +1sigma

# 95% of data is going to be in between -2sigma and 2sigma

# 99.7% of data is going to be in between -3sigma and +3sigma

# .3 % of data will fall away from +-3sigma

# Outliers
# More than or less than 3 sigma


# 6 sigma data will fall 99.9997%
# 3 in a million

# 6 sigma company
# out of 1 million only 3 can fail

# Dabawala of mumbai
# Carry home food to office
# Studied in harvard
# They are 6 sigma

# Outlier is a univariant analysis


#%%
# # Central limit theorem

# Example of blood pressure
# Data can be normal or not normal
# You take a sample of the data


# take 5 randomly from it
# Take average of it
# random sample 5 take average put it there
# if we create a distribution of it then that distribution
# tends to be normal

# As per CLT, distribution of sample means
# tend to be normal 

# as sample size tend to be larger

# Parametric method -> Normal
# Non - parametric -> Not normal

# Data -> Normal -> parametric technique

# Not normal -> non parametric

# Not normal -> convert to normal and then use clt

# Normality testing

# skewness testing
# Kurtosis testing

# Perfect normal distribution
# Skewed distribution

# tail is pointing towards positive side
# positively skewed
# 

# tail is ponting towards -ve side

# -vely skewed

# +ve skewness s>0
# -vely skewed s < 0


# s = 0 normal
# -1 < s < 1

#%%
bp = [120, 125, 112, 150, 140, 100, 95, 130, 110, 120, 119]

import seaborn as sb 

%matplotlib inline 

sb.distplot(bp)

#%%
stats.skew(bp)
#%%

sb.distplot(bp)


#%%
bp1 = []
for k in [i  * [i] for i in range(100)]:
    bp1.extend(k)

print(stats.skew(bp1))
sb.distplot(bp1)

#%%
bp1 = []
for k in [(100-i)  * [i] for i in range(100)]:
    bp1.extend(k)

print(stats.skew(bp1))
sb.distplot(bp1)

#%%

stats.kurtosis(bp)
sb.distplot(bp)

#%%
stats.kurtosis(bp)
#%%

bp1 = range(10)
stats.kurtosis(bp1)

#%%

sb.distplot(bp1)
#%%

# if both kurtosis and skewness is between -1 and +1
# data is considered normal
# 

#%%
# Measure of distance
# Euclidean distance
# Byjus
# Manhattan distance
# road distance right angles
# distance for grid systems
# Minkowski distance
# Generalization of both minkowski and manhattan distance
# 

#%%

# # Hypothesis testing
# There is no life beyond earth

# H null = H0 = there is no life beyond earth
# H alt = Ha = There is life beyond earth

# H alternate hypothesis
# allen bryman

# https://www.amazon.in/Business-Research-Methods-4-Ed/dp/0198747586/ref=sr_1_1?keywords=business+research+methods+alan+bryman&qid=1563700972&s=books&sr=1-1


# Reject H null
# Accept H alt


#%%
# ## One sample T test

# H0 = Mar age of IT Prof Male in Bangalore is 30
# Ha = Mar age of IT Prof Male in Bangalore is NOT 30

#%%
age_mar_ban = [34, 32, 29, 28, 27, 31, 29, 36, 27]
age_mar_ban

#%%
stats.ttest_1samp(age_mar_ban, 30)

#%%

# P = 76%
# Shall ACCEPT or REJECT NULL Hypothesis
# P < 5%, we reject H0, 95 % confidence interval study
# In this case P = 76 %, So accept null hypothesis

#%%
# H0 always equates samples


# T test


# ## Two sample T test

# %%
age_mar_ban = [34, 32, 29, 28, 27, 31, 29, 36, 27]
age_mar_che = [25, 27, 28, 29, 33, 26, 27, 23, 26, 29]


#%%

# H0 -> Both Ban and Che mar IT Prof male are same
# Ha -> Both ban and Che mar IT prof male are not same

#%%
stats.ttest_ind(age_mar_ban, age_mar_che)

#%%

# P = 3.7%, P < 5%, so REJECT H0 and ACCEPT Ha

# Ha -> Ban and Che mar age IT prof male is not SAME


#%% # Two sample relational T test

# experimental data and relational data 

# Response time

# Critical test
# 100 centi seconds = 1 seconds

before_rb = [45, 65, 70, 45, 50]
after_rb = [25, 35, 40, 35, 30]



#%%

# H0 -> Response time before and after RB is same
# Ha -> Response time before and after RB is not same

stats.ttest_rel(before_rb, after_rb)

#%%

# P = 0.4 %, P < 5%, we reject H0, ACCEPT Ha
# Ha -> Response time before and after RB is not same 

# Redbull is effective

#%%
# Anova test - Analysis of variance

# F - test 
# Ronald fisher

# Lemon water Coffee REdbull
# 36 23 18
# . 
# . 
# . 

# all three are same

# F value = Variance Between / Variance within

#%%
# va = [36, 12, 46, 10, 15, 20]
# vb = [33, 10, 38, 12, 13, 19]
# vc = [31, 9, 39, 13, 10, 15]

# v_within = (vt + vb + vc) / 3 = 400

# v_between = var(mu lemon, mu coffee, mu redbull) = 2 / 400

# Fcritical table

# Anova test is used for machine learning

#%%

lemon = [36, 12, 46, 10, 15, 20]
coffee = [33, 10, 38, 12, 13, 19]
rb = [31, 9, 39, 13, 10, 15]

# H0 -> All drinks response time is same

# Ha -> All drinks response time are not same


stats.f_oneway(lemon, coffee, rb)

#%%

# P = 88%, P is not < 5%, We fail to reject H0, Accept H0

# H0 -> all drinks response times are SAME

# DRINKS have no effect


#%%

# ## Correlation bivariate analysis

# -ve Correlation

# corr coefficient -0.7

# -1 0 +1

# +1 perfect Correlation

# -1 perfect negative Correlation

# 0 ? no Correlation

# -1 to -0.5 strong negative
# -0.5 to +0.5 weak positive
# 0.5 to 1 strong positive


#%%
exp = [5, 10, 12, 8, 15]
sal = [8, 20, 25, 15, 28]
age = [30, 38, 40, 35, 42]

print(sp.corrcoef(exp, sal))
print(sp.corrcoef(age, sal))

#%%


# Albert heine
# liddle shares

# Distribute your money to negatively correlated shares

