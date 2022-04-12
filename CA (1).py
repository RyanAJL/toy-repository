#!/usr/bin/env python
# coding: utf-8

# In[1]:



pairs = [[0,0],[0,1],[1,0],[1,1],[0,2],[1,2],[2,0],[2,1],[2,2]]
rule = [0,0,0,0,0,0,0,0,0]
newrule = []

#This reverses the order of the rule so that it matches index for index with the pairs of values above

k = len(rule)-1
while k >= 0:
    newrule.append(rule[k])
    k-=1
    
rule = newrule

initialcond = [1,0,0]

rulenum = int(input("Enter the rule number: "))

print(initialcond)

i = 8

sum=0
ind=0
while i >= 0:
    if sum + 2*3**i <= rulenum:
        sum += 2*3**i
        rule[ind]=2
    elif sum + 3**i <= rulenum:
        sum += 3**i
        rule[ind]=1
    else:
        rule[ind]=0
    i-=1
    ind+=1
    
#print(rule)

#pairify
j=0
while j < 10:

    initpaired=[]
    i = 0
    while i < len(initialcond):
        if i == 0:
            initpaired.append([initialcond[len(initialcond)-1], initialcond[0]])
        else:
            initpaired.append([initialcond[i-1], initialcond[i]])
        i += 1

    #print(initpaired)

    newlist = []
    for i in initpaired:
        a = 0
        while a < len(pairs):
            if pairs[a] == i:
                newlist.append(rule[a])
            a+=1

    print(newlist)
    initialcond = newlist
    j +=1




# In[14]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
get_ipython().run_line_magic('matplotlib', '')
from pylab import *


#This the original code but allows for the creation of multiple automata whose rules and output can 
# be referenced. 

class CA:
    def __init__(self, rule, numiterations=10, automata = []):
        self.rulenum = rule
        self.numiterations=numiterations
        fullautomata = []
        

        pairs = [[0,0],[0,1],[1,0],[1,1],[0,2],[1,2],[2,0],[2,1],[2,2]]
        rule = [0,0,0,0,0,0,0,0,0]
        newrule = []
        k = len(rule)-1
        while k >= 0:
            newrule.append(rule[k])
            k-=1

        rule = newrule

        initialcond = [1,0,0]

        rulenum = self.rulenum

        print(initialcond)

        i = 8

        sum=0
        ind=0
        while i >= 0:
            if sum + 2*2**i <= rulenum:
                sum += 2*2**i
                rule[ind]=2
            elif sum + 2**i <= rulenum:
                sum += 2**i
                rule[ind]=1
            else:
                rule[ind]=0
            i-=1
            ind+=1

        #print(rule)

        #pairify
        
        #Now the user can specify the number of iterations they want to run
        
        j=0
        while j < self.numiterations:

            initpaired=[]
            i = 0
            while i < len(initialcond):
                if i == 0:
                    initpaired.append([initialcond[len(initialcond)-1], initialcond[0]])
                else:
                    initpaired.append([initialcond[i-1], initialcond[i]])
                i += 1

            #print(initpaired)

            newlist = []
            for i in initpaired:
                a = 0
                while a < len(pairs):
                    if pairs[a] == i:
                        newlist.append(rule[a])
                    a+=1

            fullautomata.append(newlist)
            initialcond = newlist
            j +=1
            
            self.automata = fullautomata




    
rulenum = int(input("Enter the rule for your 2 neighbor cellular automata"))
newCa = CA(rulenum, 50)

for i in newCa.automata:
    print(i)
    
print(newCa.numiterations)
print(newCa.rulenum)




    


# In[ ]:




