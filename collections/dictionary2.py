product={"id":100,"title":"food","price":50,"brand":"nestle"}

if "offer" in product:
    product["offer"]=10
else:
    product["offer"]=20
    
print(product)