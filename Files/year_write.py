f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\year.txt","w")

for year in range(1800,2025):
    f.write(str(year)+"\n")
f.close()