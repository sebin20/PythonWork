text="this is a simple text this is sample"
words=text.split(" ")
word_dictionary={}
for w in words:
    if w in word_dictionary:
        word_dictionary[w]+=1
    else:
        word_dictionary[w]=1
        
print(word_dictionary)