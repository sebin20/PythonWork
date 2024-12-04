#Write a Python program to count the occurrences of each element in a list.
lst = [1,4,4,2,1,3,3]
lst.sort()
Occurance=[ ]
for num in lst:
      if num not in Occurance:
              print(num,lst.count(num))
              Occurance.append(num)