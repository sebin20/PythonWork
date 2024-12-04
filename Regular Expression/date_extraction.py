from re import findall
f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\date_data.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

date=findall(pattern,content)

# for da in date:
#     print(da)

print(date)


# from re import finditer
# f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\date_data.txt")

# for line in f:
#     lines=line.rstrip("\n")
    
#     pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

#     date=finditer(pattern,lines)
#     for dat in date:
#          print(dat.group())
