#!/usr/bin/env python
# coding: utf-8

# In[71]:


import re
import numpy
import pandas as pd
from numpy import dot
from numpy.linalg import norm


# In[72]:


text = open("sentences.txt", "r")
sentences = []
for line in text:
    sentences.append(line.strip().lower())
# print(len(sentences))


# In[73]:


words = {}
i = 0
ind = 0
sent_ww = sentences.copy()
for line in sent_ww:
    line = re.split('[^a-z]', line)
    sent_ww[i] = line
    i+=1
    for w in line:
        if w not in words and w!='':
            words[w] = ind
            ind+=1

# print(len(words))
# print(sentences)


# In[74]:


num_w = len(words)
num_s = len(sentences)

matrix = numpy.zeros((num_s, num_w))

for i in range(num_s):
    sen_w = sent_ww[i]
    for x in sen_w:
        if x!='':
            matrix[i][words[x]] += 1


# In[75]:


distances = {}

fsm = matrix[0, :]
for i in range(num_s):
    csm = matrix[i, :]
    distances[i] = 1 - (dot(fsm, csm)/(norm(fsm)*norm(csm)))
# print(distances)


# In[76]:



dist_df = pd.DataFrame.from_dict(distances, orient = 'index')
dist_df.columns = ['Distance']
dist_df['Sentence'] = list(map(lambda x: sentences[x], dist_df.index.values))
# print(sentences[0])


# In[77]:


dist_df.sort_values('Distance')


# In[ ]:




