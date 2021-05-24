import docx
import pandas as pd
from docx import Document
document = Document("assignment.docx")
table=(document.tables[0])
data = [[cell.text for cell in row.cells] for row in table.rows]
df = pd.DataFrame(data)
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import sent_tokenize , word_tokenize
import glob
import re
import os
import numpy as np
import sys
Stopwords = set(stopwords.words('english'))

def finding_all_unique_words_and_freq(words):
    words_unique = []
    word_freq = {}
    for word in words:
        if word not in words_unique:
            words_unique.append(word)
    for word in words_unique:
        word_freq[word] = words.count(word)
    return word_freq
def finding_freq_of_word_in_doc(word,words):
    freq = words.count(word)
        
def remove_special_characters(text):
    regex = re.compile('[^a-zA-Z0-9\s]')
    text_returned = re.sub(regex,'',text)
    return text_returned



all_words = []
dict_global = {}
file_folder=[]
doc=1
for i in range(1,10):
    file_folder.append(df[1][i])
idx = 1
files_with_index = {}
query = 'Natural Language Processing Information Retrieval Book Text Web HTML Theory';
query = query.lower().split()
for file in (file_folder):
    fname = file
    print("\n")
    text = file
    text = remove_special_characters(text)
    text = re.sub(re.compile('\d'),'',text)
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    words = [word for word in words if len(words)>1]
    words = [word.lower() for word in words]
    words = [word for word in words if word not in Stopwords]
    dict_global.update(finding_all_unique_words_and_freq(words))
    files_with_index[idx] = os.path.basename(fname)
    idx = idx + 1
    
    print("doc ")
    print(doc)
    doc=doc+1
    print("----query matched----")
    for i in query:
        if i in words:
            print(i)
    word_freq_in_doc = finding_all_unique_words_and_freq(words)
    print (word_freq_in_doc)
unique_words_all = set(dict_global.keys())

##value=(max(dict_global.values()))
##for key,val in dict_global.items() :
##    if val == value :
##        print("The highest KEY in the dictionary is ",key)



##class Node:
##    def __init__(self ,docId, freq = None):
##        self.freq = freq
##        self.doc = docId
##        self.nextval = None
##    
##class SlinkedList:
##    def __init__(self ,head = None):
##        self.head = head
##
##
##linked_list_data = {}
##for word in unique_words_all:
##    linked_list_data[word] = SlinkedList()
##    linked_list_data[word].head = Node(1,Node)
##word_freq_in_doc = {}
##idx = 1
##for file in (file_folder):
##    text = file
##    text = remove_special_characters(text)
##    text = re.sub(re.compile('\d'),'',text)
##    sentences = sent_tokenize(text)
##    words = word_tokenize(text)
##    words = [word for word in words if len(words)>1]
##    words = [word.lower() for word in words]
##    words = [word for word in words if word not in Stopwords]
##    word_freq_in_doc = finding_all_unique_words_and_freq(words)
##    print (word_freq_in_doc)
##    for word in word_freq_in_doc.keys():
##        linked_list = linked_list_data[word].head
##        while linked_list.nextval is not None:
##            linked_list = linked_list.nextval
##        linked_list.nextval = Node(idx ,word_freq_in_doc[word])
##    idx = idx + 1
##
##query = input('Enter your query:')
##query = word_tokenize(query)
##connecting_words = []
##cnt = 1
##different_words = []
##for word in query:
##    if word.lower() != "and" and word.lower() != "or" and word.lower() != "not":
##        different_words.append(word.lower())
##    else:
##        connecting_words.append(word.lower())
##print(connecting_words)
##total_files = len(files_with_index)
##zeroes_and_ones = []
##zeroes_and_ones_of_all_words = []
##for word in (different_words):
##    if word.lower() in unique_words_all:
##        zeroes_and_ones = [0] * total_files
##        linkedlist = linked_list_data[word].head
##        print(word)
##        while linkedlist.nextval is not None:
##            zeroes_and_ones[linkedlist.nextval.doc - 1] = 1
##            linkedlist = linkedlist.nextval
##        zeroes_and_ones_of_all_words.append(zeroes_and_ones)
##    else:
##        print(word," not found")
##        sys.exit()
##print(zeroes_and_ones_of_all_words)
