#!/usr/bin/env python
# coding: utf-8

# In[178]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict


# ## Read data from the dataset.

# In[179]:


f = pd.read_csv('RAW_recipes.csv')


# In[180]:


f.head()


# In[181]:


f.shape[0]


# ## Most similar recipe

# In[182]:


iPerR = defaultdict(set)
rPerI = defaultdict(set)


# In[183]:


for j in range(f.shape[0]):
    ingredientList = eval(f["ingredients"][j])
    for i in range(len(ingredientList)):
        ingredient, recipe = ingredientList[i], f['name'][j]
        iPerR[recipe].add(ingredient)
        rPerI[ingredient].add(recipe)


# In[184]:


def Jaccard(s1, s2):
    numer = len(s1.intersection(s2))
    denom = len(s1.union(s2))
    return numer / denom


# In[185]:


def mostSimilar_recipe(i):
    similarities = []
    ing = iPerR[i]
    for i2 in iPerR:
        if i2 == i: continue
        sim = Jaccard(ing, iPerR[i2])
        similarities.append((sim,i2))
    similarities.sort(key=lambda x: (-x[0]))
    return similarities[:5]


# In[186]:


query = f['name'][500]


# In[187]:


query


# In[188]:


iPerR['perfect chocolate cake  mccall s cooking school']


# In[192]:


iPerR['tex mex chocolate sheet cake   the best']


# In[193]:


mostSimilar_recipe(query)


# In[194]:


f[f['name'].isin(['perfect chocolate cake  mccall s cooking school'])]


# In[195]:


f[f['name'].isin(['tex mex chocolate sheet cake   the best'])]


# In[196]:


f[f['name'].isin(['wanda s cutout cream cookies'])]


# In[197]:


f[f['name'].isin(['hershey s chocolate chocolate cake'])]


# In[198]:


f[f['name'].isin(['rich chocolate cake'])]


# In[199]:


f[f['name'].isin(['best chocolate cake with creamy chocolate frosting'])]


# ## Most similar ingredient

# In[200]:


def mostSimilar_ingredient(i):
    similarities = []
    reci = rPerI[i]
    for i2 in rPerI:
        if i2 == i: continue
        sim = Jaccard(reci, rPerI[i2])
        similarities.append((sim,i2))
    similarities.sort(key=lambda x: (-x[0], x[1]))
    return similarities[:5]


# In[201]:


mostSimilar_ingredient('cherries')


# ## Recommendation

# ### Just use similarity

# In[202]:


query = f['name'][20000]


# In[203]:


query


# In[204]:


iPerR[query]


# In[205]:


ing = {'cinnamon', 
      'cherries', 
      'butterscotch', 
      'vodkag'}


# In[269]:


ing = {'lettuce heart', 
       'butterscotch',
       'low-fat bacon'}


# In[257]:


ing = {'cheese', 'pepper', 'onion', 'chicken'}


# In[270]:


similarities2 = []
for i2 in iPerR:
    sim = Jaccard(ing, iPerR[i2])
    similarities2.append((sim,i2,iPerR[i2]))
similarities2.sort(key=lambda x: (-x[0]))
for j in range(10):
    print(similarities2[j])


# In[208]:


num_list = [i[1] for i in similarities2[0:5]]
prob = [i[0] for i in similarities2[0:5]]


# In[209]:


plt.barh(range(len(prob)), prob, tick_label = num_list)
# plt.savefig('top10.jpg')
plt.show()


# In[210]:


f[f['name'].isin(['chicken cheese ball'])]


# In[211]:


f[f['name'].isin(['avgolemono soup  chicken soup'])]


# In[212]:


f[f['name'].isin(['omelets in a bag'])]


# In[213]:


f[f['name'].isin(['cheese rolls'])]


# In[214]:


f[f['name'].isin(['cheese  cheese   onion  beef   cheese enchilada fillings'])]


# In[215]:


list1 = eval(f.iloc[43730]["nutrition"])
list2 = eval(f.iloc[11032]["nutrition"])
list3 = eval(f.iloc[147698]["nutrition"])
list4 = eval(f.iloc[39553]["nutrition"])
list5 = eval(f.iloc[39686]["nutrition"])


# In[216]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5]
k1 = [list1[0],list2[0],list3[0],list4[0],list5[0]]
# k2 = [list1[1],list2[1],list3[1],list4[1],list5[1]]
# k3 = [list1[2],list2[2],list3[2],list4[2],list5[2]]
# k4 = [list1[3],list2[3],list3[3],list4[3],list5[3]]
# k5 = [list1[4],list2[4],list3[4],list4[4],list5[4]]
plt.plot(x,k1,'s-',color = 'r',label="calories")
# plt.plot(x,k2,'o-',color = 'g',label="total fat")
# plt.plot(x,k3,'o-',color = 'b',label="sugar")
# plt.plot(x,k4,'o-',color = 'y',label="sodium")
# plt.plot(x,k5,'o-',color = 'c',label="protein")
plt.xlabel("Recipe Number")
plt.ylabel("Content(g/mg)")
plt.legend(loc = "best")
# plt.savefig("Recipe number vs. content.jpg")
plt.savefig("Recipe number vs. Calories.jpg")
plt.show()


# In[217]:


list1 = f.iloc[43730]["minutes"]
list2 = f.iloc[11032]["minutes"]
list3 = f.iloc[147698]["minutes"]
list4 = f.iloc[39553]["minutes"]
list5 = f.iloc[39686]["minutes"]


# In[218]:


x = [1,2,3,4,5]
k1 = [list1,list2,list3,list4,list5]
plt.bar(x, k1, tick_label = x)
plt.xlabel("Recipe Number")
plt.ylabel("Time(min)")
# plt.savefig("Recipe number vs. Calories.jpg")
plt.show()


# In[219]:


list6 = f.iloc[43730]["n_steps"]
list7 = f.iloc[11032]["n_steps"]
list8 = f.iloc[147698]["n_steps"]
list9 = f.iloc[39553]["n_steps"]
list10 = f.iloc[39686]["n_steps"]


# In[220]:


fig, ax = plt.subplots()
x = [1,2,3,4,5]
k1 = [list1,list2,list3,list4,list5]
k2 = [list6,list7,list8,list9,list10]
ax.bar(np.arange(5), k1, tick_label = x, width = 0.45, label = 'time')
ax.bar(np.arange(5) + 0.45, k2, tick_label = x, width = 0.45, label = 'steps')
plt.xlabel("Recipe Number")
plt.ylabel("time/steps number")
ax.legend()
plt.savefig("Recipe number vs. time or steps.jpg")
plt.show()


# ### Rank all the ingredients

# In[221]:


ingredients = []
for i in range(f.shape[0]):
    ingredients.extend(eval(f['ingredients'][i]))


# In[222]:


dict = {}
for key in ingredients:
    dict[key] = dict.get(key, 0) + 1


# In[223]:


ingredients_sort = sorted(dict.items(), key=lambda x: x[1], reverse=True)


# In[224]:


ingredient_top50 = []
for i in range(50):
    ingredient_top50.append(ingredients_sort[i][0])


# In[225]:


ingredient_top50[0:10]


# In[226]:


dict['sugar']


# In[227]:


num_list = [dict[i] for i in ingredient_top50[0:10]]
plt.barh(range(len(num_list)), num_list, tick_label = ingredient_top50[0:10])
plt.savefig('top10.jpg')
plt.show()


# Now the problem is that some ingredients does not exist in the dataset. We need to find similar ingredients.
# What I did in this step is to find some similar ingredients as new input.

# In[311]:


new = []


# In[312]:


s = 'lettuce heart'
for i in dict:
    if s.find(i) != -1:
        if dict[i] > 300:
            new.append(i)   


# In[313]:


s = 'butterscotch'
for i in dict:
    if s.find(i) != -1:
        if dict[i] > 300:
            new.append(i) 


# In[314]:


s = 'low fat bacon'
for i in dict:
    if s.find(i) != -1:
         if dict[i] > 300:
            new.append(i)


# In[315]:


new


# In[306]:


dict2 = {}
for key in dict:
    if key.find('butterscotch') != -1:
        dict2[key] = dict[key]
ww = sorted(dict2.items(), key=lambda x: x[1], reverse=True)
if dict[ww[0][0]] > 300:
    new.append(ww[0][0])


# In[307]:


dict3 = {}
for key in dict:
    if key == 'lettuce heart': continue
    if key.find('lettuce heart') != -1:
        dict3[key] = dict[key]
ww2 = sorted(dict3.items(), key=lambda x: x[1], reverse=True)
if dict[ww2[0][0]] > 300:
    new.append(ww2[0][0])


# In[308]:


dict4 = {}
for key in dict:
    if key == 'low fat bacon': continue
    if key.find('low fat bacon') != -1:
        dict4[key] = dict[key]
ww3 = sorted(dict4.items(), key=lambda x: x[1], reverse=True)
if dict[ww3[0][0]] > 300:
    new.append(ww3[0][0])


# In[309]:


new.append('cherries')


# In[320]:


new


# In[321]:


ing = set(new)


# In[322]:


def similarity(s1, s2):
    numer = len(s1.intersection(s2))
    denom = len(s1.union(s2))
    return numer / denom


# In[323]:


similarities2 = []
for i2 in iPerR:
    sim = similarity(ing, iPerR[i2])
    similarities2.append((sim,i2,iPerR[i2]))
similarities2.sort(key=lambda x: (-x[0]))
for j in range(5):
    print(similarities2[j])


# In[ ]:




