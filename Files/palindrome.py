f=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\words_palindrome.txt","r")

lp=open("C:\\Users\\sebin\\OneDrive\\Desktop\\Python\\Datasets\\palindrome_words","w")


def reverse_word(word):
    reversed_word=word[::-1]
    return reversed_word

for line in f:
    word=line.rstrip("\n")
    wrd=reverse_word(word)
    
    if wrd==word:
        lp.write(word+"\n")
        
f.close()
lp.close()