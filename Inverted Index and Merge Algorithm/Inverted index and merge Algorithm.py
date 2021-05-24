import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import time
import re
from collections import defaultdict
from stemming.porter2 import stem
stop_words = []
with open ("Stopword-List.txt",'r') as file:
    s=file.read().replace('\n',' ')
stop_words = s.split()


def inverted_index(stop_words):
 dictionary = {}
 documents = {}
 
 for i in range(0,2):
     doc_no = i+1
     with open ('F:\\6th sem\\data\\doc'+ str(doc_no) + '.txt','r') as file:
         
         s=file.read().replace('\n',' ')
         

##cleaning documents
     s = re.sub('  ', ' ', s)
     s = re.sub(r"won't", "will not", s)
     s = re.sub(r"can\'t", "can not", s)
     s = re.sub(r"n\'t", " not", s)
     s = re.sub(r"\'re", " are", s)
     s = re.sub(r"\'s", " is", s)
     s = re.sub(r"\'d", " would", s)
     s = re.sub(r"\'ll", " will", s)
     s = re.sub(r"\'t", " not", s)
     s = re.sub(r"\'ve", " have", s)
     s = re.sub(r"\'m", " am", s)
     s = re.sub(r'[0-9]+', '', s)
     s=re.sub(r'[^\w\s]',' ', s)
     key = 'doc' + str(doc_no)
    
     documents.setdefault(key,[])
     documents[key].append(s)
    
    #removing stopwords and lowercase
     s = s.lower()
     s = [words if words not in stop_words else '' for words in s.split(' ')]
     doc = []
     doc = list(filter(None, s)) 
     stemmed = []
     
    
    #stemming
     for i in doc:
        stemmed.append(stem(i))
     
    #creating posting list
     for x in stemmed:
        key = x
        dictionary.setdefault(key, [])
        dictionary[key].append(doc_no)
        
    #removing duplicates
     dictionary = {a:list(set(b)) for a, b in dictionary.items()}
        
 return dictionary,documents


def intersect(p1,p2):
    answer=[]
    answer=[value for value in p1 if value in p2] 
    return answer

#calling the functions
dictionary,documents=inverted_index(stop_words)
print(documents)
print ('INVERTED INDEX:',dictionary)

#AND query
print('\nDOCUMENT NUMBER AND RESULTANT DOCUMENT:')
p1=dictionary.get('caesar')
p2=dictionary.get('brutus')
doc_no=intersect(p1,p2)
for i in doc_no:
    i='doc'+str(i)
    
    print (i,':',documents.get(i))

