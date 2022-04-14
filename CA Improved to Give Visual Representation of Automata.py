#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  Here the possible combinations of 0, 1, and 2 in two sites are made into the "pairs" list.

pairs = [[0,0],[0,1],[1,0],[1,1],[0,2],[1,2],[2,0],[2,1],[2,2]]
rule = [0,0,0,0,0,0,0,0,0]
newrule = []

#  This loop reverses the order of the rule so that it matches index for index with the pairs of values.

k = len(rule)-1
while k >= 0:
    newrule.append(rule[k])
    k-=1
    
rule = newrule

initialcond = [1,0,0]  #  Choosing an arbitrary initial condition.

rulenum = int(input("Enter the rule number: "))

print(initialcond)


# This creates the rule for evolving states into future states. It finds the largest allowable entry that does not push the
#  standard number equivalent above the rule number.

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



j=0
while j < 10:

    initpaired=[]
    i = 0
    while i < len(initialcond):
        #  This breaks the current list into 2-long pieces that can be identified as items in the "pairs" list
        if i == 0:
            initpaired.append([initialcond[len(initialcond)-1], initialcond[0]])
        else:
            initpaired.append([initialcond[i-1], initialcond[i]])
        i += 1

    newlist = []
    for i in initpaired:
        #  Matching items in the "pairs" list to the pairs generated in the previous while loop
        
        a = 0
        while a < len(pairs):
            if pairs[a] == i:
                newlist.append(rule[a])
            a+=1

    print(newlist)
    initialcond = newlist
    j +=1




# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
get_ipython().run_line_magic('matplotlib', '')
from pylab import *


#  This the original code but allows for the creation of multiple automata whose rules and output can 
#  be referenced. 

class CA:
    def __init__(self, rule, numiterations=10, automata = None):
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

        initialcond = [1,0,0]  #  Assigning an arbitrary inital condition

        rulenum = self.rulenum

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

        
        #  Now the user can specify the number of iterations they want to run
        
        j=0
        while j < self.numiterations:
            
            #  This applies the evolution rule self.numiterations times.

            initpaired=[]
            i = 0
            while i < len(initialcond):
                if i == 0:
                    initpaired.append([initialcond[len(initialcond)-1], initialcond[0]])
                else:
                    initpaired.append([initialcond[i-1], initialcond[i]])
                i += 1


            newlist = []
            for i in initpaired:
                a = 0
                while a < len(pairs):
                    if pairs[a] == i:
                        newlist.append(rule[a])
                    a+=1

            #  This appends each new step in the cellular automata to the list "fullautomata".
                    
            fullautomata.append(newlist)
            initialcond = newlist
            j +=1
            
            self.automata = fullautomata




    
rulenum = int(input("Enter the rule for your 2 neighbor cellular automata"))
newCa = CA(rulenum, 50)

adjustedarray=[]
for i in newCa.automata:
    adjusted = []
    
    #  The following for loop scales the entries in the 1x3 matrices to be less than or equal to one so they can be plotted
    #  via imshow.
    
    for j in i:
        adjusted.append(j/2)
    adjustedarray.append(adjusted)
    print(i)
    
    plt.imshow(adjustedarray)
    
print("Number of iterations:", newCa.numiterations)
print("Rule number:", newCa.rulenum)




    


# In[ ]:




