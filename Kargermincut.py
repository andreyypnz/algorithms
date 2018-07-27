
# coding: utf-8

# In[20]:



import random



# In[21]:


def graph():
    d={}
    with open('karger.txt') as f:
        a = f.readlines()
    a = [x.strip() for x in a] 
    for i in range(len(a)):
        a[i]=a[i].split("\t")
    a=[[int(float(j)) for j in i] for i in a]
    for i in a:
        d[i[0]]=i[1:]
    return d


# In[22]:


def cutmin():
    d=graph()
    while len(list(d.keys()))>2:
        r=random.choice(list(d.keys()))
        rr=random.choice(list(set(d[r])))
        while r==rr:
            r=random.choice(list(d.keys()))
            rr=random.choice(list(set(d[r])))
        d[min(r,rr)]=[x for x in d[min(r,rr)] if x != max(r,rr)]
        for x in list(set(d[max(r,rr)])):
            for n, i in enumerate(d[x]):
                if i == max(r,rr):
                    d[x][n] = min(r,rr)
        d[max(r,rr)]=[x for x in d[max(r,rr)] if x != min(r,rr)]
        d[min(r,rr)]=d[min(r,rr)]+d[max(r,rr)]
        d.pop(max(r,rr))
    return len(d[1])
    


# In[23]:


def kargerresult():
    a=[]
    for i in range(400):
        a.append(cutmin())
    return min(a)
        


# In[24]:


print(kargerresult())


# In[ ]:



    
        

