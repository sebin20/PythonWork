users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]
rahul_followers=["rohit","kohli","rishab","rahul"]
sanju_followers=["sanju","rohit","kohli"]
user_set=set(users)
rahul_set=set(rahul_followers)

# follow_suggetion=user_set.difference(rahul_set)
# print(list(follow_suggetion))

mutual=set(rahul_followers).intersection(set(sanju_followers))
print(mutual)