#!/usr/bin/env python
# coding: utf-8

# In[127]:


import re
import numpy
import pandas as pd
from scipy import spatial


# In[128]:


text = open("sentences.txt", "r")
sentences = []
for line in text:
    sentences.append(line.strip().lower())
# print(len(sentences))


# In[129]:


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


# In[130]:


num_w = len(words)
num_s = len(sentences)

matrix = numpy.zeros((num_s, num_w))

for i in range(num_s):
    sen_w = sent_ww[i]
    for x in sen_w:
        if x!='':
            matrix[i][words[x]] += 1


# In[131]:


distances = {}

first_sentence_metric = matrix[0, :]
for i in range(num_s):
    cmp_sentence_metric = matrix[i, :]
    
    distances[i] = spatial.distance.cosine(first_sentence_metric, cmp_sentence_metric)
    
# print(distances)


# In[132]:



distances_df = pd.DataFrame.from_dict(distances, orient = 'index')
distances_df.columns = ['distance']
distances_df['sentence'] = list(map(lambda x: sentences[x], distances_df.index.values))
# print(sentences[0])


# In[133]:


distances_df.sort_values('distance')

