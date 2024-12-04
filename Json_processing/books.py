from json import load
f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\JSON_FILES\\books.json")

data=load(f)

# for bk in data:
#     print(bk.get('title'))
    
all_titles_under_200=[bk.get('title') for bk in data if bk.get('pages')<250]
print(all_titles_under_200)

# max_price=max([bk.get('price')  for bk in data ])
# max_book=[bk.get('title') for bk in data if bk.get('price')==max_price]
# print(max_book)


max_price_book=max(data,key=lambda x:x.get('price'))['title']
print(max_price_book)


#print all genres


all_genres=[bk.get('genre') for bk in data]
print(set(all_genres))


#count of genres

count_genre={gen:all_genres.count(gen) for gen in all_genres}
print(count_genre)

# To get maximum value of genres and genre

# max_gen_value=max([val for val in count_genre.values()])
# print(max_gen_value)

max_gen=max(count_genre.items(),key=lambda x:x[1])[0]
print(max_gen)


all_authors=[bk.get('author')  for bk in data]

count_auth={auth:all_authors.count(auth)  for auth in all_authors}


authors_more_than_one=[ key for key,val in count_auth.items() if val>1]
print(authors_more_than_one)