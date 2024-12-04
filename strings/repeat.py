text="BBCADCG"
    # 0123456
i=0
for ch in text:
    i=i+1
    if ch in text[i:]:
        break
print(ch)