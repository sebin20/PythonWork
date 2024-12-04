from re import findall
f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\url.txt")

content=f.read()
pattern=r"https?://[\w\S./]+"
urls=findall(pattern,content)
for url in urls:
    print(url)