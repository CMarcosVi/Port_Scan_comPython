#!/usr/bin/env python
# coding: utf-8

# In[8]:


import socket
url = input("diga a Url do site")
portas = range(1,65535)

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)
    code = cliente.connect_ex((url, porta))
    if code == 0:
        print(porta, "OPEN")


# In[10]:


#!pip install dnspython

import dns.resolver

res = dns.resolver.Resolver()
arquivo = open("", "r")#arquivo
subdominios = arquivo.read().splitlines()

alvo = input("digite a url do alvo") #exemplo


for subdominio in subdominios:
    try:
        sub_alvo = subdominio + "." + alvo
        resultado = res.resolve(sub_alvo, "A")
        for ip in resultado:
            print(sub_alvo, "->", ip)

    except:
        pass


# In[ ]:




