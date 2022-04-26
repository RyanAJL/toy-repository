#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import matplotlib.pyplot as plt


#4

def newVar():
    variances =[]
    random = []
    a = 0
    i = 0 
    while a < 100:
        while i < 100:
            random.append(np.random.normal())
            i +=1
        variances.append(np.var(random))
        a+=1
    return np.mean(variances)

i = 0



variances = []

i = 0
while i < 100:
    variances.append(newVar())
    i += 1
    

plt.plot(np.arange(0,100), variances)

    
#It looks like the probability of being at some variance a is 1/(size of set a is chosen from)


# In[30]:


#5

E1 = variances[int(np.random.uniform()*100)]
steps = 100

def decision(E1=0):
    r = np.random.uniform()
    E2 = variances[int(np.random.uniform()*100)]
    if r < np.exp(-1*E2-E1):
        E1=E2
        return E1
    return E1
    
time = []
Earray = []
i = 0
while i < steps:
    time.append(i)
    Earray.append(decision())
    i+=1
    
#6
    
plt.plot(time, Earray)


# In[33]:


#7


plt.hist(np.histogram(Earray))


# In[ ]:




