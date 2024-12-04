# List of dictionaries for mobile products
products = [
    {
        "id": 1,
        "title": "iPhone 14",
        "brand": "Apple",
        "price": 999.99
    },
    {
        "id": 2,
        "title": "Galaxy S21",
        "brand": "Samsung",
        "price": 799.99
    },
    {
        "id": 3,
        "title": "samsung s23",
        "brand": "Samsung",
        "price": 599.99
    },
    {
        "id": 4,
        "title": "Nokia G50",
        "brand": "Nokia",
        "price": 249.99
    },
    {
        "id": 5,
        "title": "Pixel 6",
        "brand": "Google",
        "price": 599.99
    },
    {
        "id": 6,
        "title": "OnePlus 9",
        "brand": "OnePlus",
        "price": 729.99
    },
    {
        "id": 7,
        "title": "Xiaomi Mi 11",
        "brand": "Xiaomi",
        "price": 749.99
    },
    {
        "id": 8,
        "title": "Sony Xperia 5 II",
        "brand": "Sony",
        "price": 899.99
    }
    ]

#to get titles

print(len(products))
mobile_titles=[mob.get('title') for mob in products]
print(mobile_titles)


#titles of samsung mobiles
samsung_mobiles=[mob.get('title') for mob in products if mob.get('brand')=='Samsung']
print(samsung_mobiles)
print(len(samsung_mobiles))

#to print title of product having max price
print(max(products,key=lambda d:d.get('price'))['title'])


#to get sam count
count_sam=sum([1 for mob in products if mob.get('brand')=='Samsung'])
print(count_sam)

#to get brand counts 
all_brands=[br.get("brand") for br in products]
brand_count={br:all_brands.count(br) for br in all_brands}
print(brand_count)

#most repeating brands

most_repeating=max(all_brands,key=lambda b:all_brands.count(b))
print(most_repeating)