f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\lines.txt","r")
words=[]

for line in f:
    line=line.rstrip("\n")
    all_words=line.split(" ")
    
    for wrd in all_words:
        words.append(wrd)
print(words)
word_count={wrd:words.count(wrd)  for wrd in words }
print(word_count)


sorted_word_count = sorted(word_count.items(), key=lambda x: x[1],reverse=True)
# sorted_word_count=sorted(word_count,key=lambda k:word_count.get(k)[word_count.get(k)])
print(sorted_word_count)