orders=["tea","coffee","tea","coffee","gheeroast","plainroast","poratta","tea"]

summary={}
for item in orders:
    if item in summary:
        summary[item]+=1
        
    else:
        summary[item]=1
        
print(summary)