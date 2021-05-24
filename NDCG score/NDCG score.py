import math
def ndcg(x):
    y=sorted(x,reverse=True) 
    dcg=0
    idcg=0
    for i in range(len(x)):
        x[i]=int(x[i])
        y[i]=int(y[i])
        dcg=dcg+(x[i]/math.log((i+1+1),2))
        idcg=idcg+(y[i]/math.log((i+1+1),2))
    return dcg/idcg  
    
doc=int(input("Enter no of documents:"))
sys=int(input("Enter no of retrieval sys:"))
for i in range (sys):
    print("Enter ranks of system "+ str(i+1),":")
    ranks=(input()).split(",")
    score=ndcg(ranks)
    print("NDCG Score= ",round(score,2))
        
