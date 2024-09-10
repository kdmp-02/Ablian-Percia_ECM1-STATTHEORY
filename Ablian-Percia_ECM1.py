#!/usr/bin/env python
# coding: utf-8

# In[41]:


from itertools import combinations
from IPython.display import display
import pandas as pd

comb = combinations(['Marcos','Marcos','Marcos','Marcos','Robredo','Robredo'], 4)
x=1
population = []
total_M = 0
total_R = 0
# Print the obtained combinations
for i in list(comb):
    #population.append(i)
    p_M = i.count('Marcos')
    p_R = i.count('Robredo')
    
    realprop_M = p_M/4
    tupe_M = (p_M/4,)
    i += tupe_M
    
    realprop_R = p_R/4
    tupe_R = (p_R/4,)
    i += tupe_R
    
    total_M += realprop_M
    total_R += realprop_R
    
    population.append(i)
    x+=1
    
samp_distrib = x-1
df = pd.DataFrame(population, columns=['1st Pick','2nd Pick','3rd Pick','4th Pick','p_M','p_R'])
display(df.transpose())

ave_M = total_M/samp_distrib
ave_R = total_R/samp_distrib

print(f"Average Proportion of Marcos: {ave_M:.2f}")
print(f"Average Proportion of Robredo: {ave_R:.2f}")

