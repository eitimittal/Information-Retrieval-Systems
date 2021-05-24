antony=[1,1,0,0,0,1]
brutus=[1,1,0,1,0,0]
caesar=[1,1,0,1,1,1]
calpurnia=[0,1,0,0,0,0]
cleopatra=[1,0,0,0,0,0]
mercy=[1,0,1,1,1,1]
worser=[1,0,1,1,1,0]
dic ={0:"Antony and Cleopatra",1:"Julius Caesar",2:"The Tenpeat",3:"Hamlet",4:"Othello",5:"Macbetc"}
q= "Brutus AND Caesar AND NOT Calpurnia"

v1=[0]*6 #list res will store Brutus AND Caesar
for i in range(0,6):
    v1[i]= brutus[i] and caesar[i]

#v1 AND NOT Calpurnia
res=[0]*6 #list res will store Result of query
for i in range(0,6):
    # Not Calpurnia
    if(calpurnia[i]==0): 
        res[i]=v1[i] and 1
    else:
        res[i]=v1[i] and 0
print(res)
print("Query found in these Documents")
for i in range(6):
    if(res[i]==1):
        print(dic[i])
