# product={"id":100,"title":"food","price":50,"brand":"nestle"}
# print(product["id"])


text="ABBACB"

dict={}

for ch in text:
    if ch in dict:
        dict[ch]+=1
        print("first repeat: ",ch)
        break
    else :
        dict[ch]=1
print(dict)
# product["price"]=50
# print(product["price"])

# product["brand"]="parle"
# print(product)

# product["use_by_date"]="10-10-24"
# print(product)