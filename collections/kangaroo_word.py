source_word="CHICKEN"

target_word="HEN"

is_kangaroo=True

source_count={i:source_word.count(i) for i in source_word}

for ch in target_word:
    if ch in source_count and source_count.get(ch)>0:
        source_count[ch]-=1
    else:
        is_kangaroo=False
        
print("The word is kangaroo " if is_kangaroo==True else "Not kangaroo")
