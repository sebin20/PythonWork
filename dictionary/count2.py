words=["hello","hai","hello","this","is","sample","this","hai","hai"]

# word : word count

word_freeqs={word:words.count(word) for word in words}
print(word_freeqs)

#print recursive words

word_freeq=[k for k,v in word_freeqs.items() if v>1]
print(word_freeq)

# non recursive words

word_freeq_non=[k for k,v in word_freeqs.items() if v==1]
print(word_freeq_non)


#to find max value and maximum recursive words

max_value=max([val for val in word_freeqs.values()])
print(max_value)
most_recursive=[k for k,v in word_freeqs.items() if v==max_value]
print(most_recursive)
