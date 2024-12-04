# def sums(num1,num2):
#     return num1+num2

# print(sums(10,20)) 


sums=lambda n1,n2:n1+n2
print(sums(10,20))


# find max of two strings

max_string=lambda str1,str2: str1 if len(str1)> len(str2) else  str2
print(max_string("apple","oranges"))

#find min of two strings
min_string=lambda str1,str2: str1 if len(str1)< len(str2) else  str2
print(min_string("apple","oranges"))

#longest word
words=["hai","hello","apple","morning"]
print(max(words,key=lambda word:len(word)))


str="The cat sat on the mat, and the cat looked around on mat"
words=str.split(" ")

print(max(words,key=lambda str:len(str)))


#sort the words


str="the cat sat on the mat, and the cat looked around on mat"
words=str.split(" ")

def get_length(w):
    return len(w)
srt_words=sorted(words,key=get_length,reverse=True)
print(srt_words)


#to get most recursive words
str="the cat sat on the mat, and on the cat looked around on mat"
words=str.split(" ")

def word_count(w):
    return words.count(w)

most_recursive_word=max(words,key=word_count)
print(most_recursive_word)

# to get least recursive words
str="the cat sat on the mat, and on the cat looked around on mat"
words=str.split(" ")

def word_count(w):
    return words.count(w)

least_recursive_word=min(words,key=word_count)
print(least_recursive_word)

# to get non recursive words

str="the cat sat on the mat and on the cat looked around on mat"
words=str.split(" ")

non_recursive_word=[wrd for wrd in words if words.count(wrd)==1]
print(non_recursive_word)