arr=["apple","orange","mangoes","jackfruit","blueberry"]

longest_count=max([len (w) for w in arr])

longest_word=[w for w in arr if len(w)==longest_count]

longest_word.sort()
print(longest_word)