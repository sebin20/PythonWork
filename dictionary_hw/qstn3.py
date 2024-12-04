#Given a dictionary where the keys are student names and the values are their scores,write a program to calculate the average score.
student_scores = {"Alice": 50,"Bob": 92,"Charlie": 78,"Diana": 88,"Ethan": 95}

scores=[val for val in student_scores.values() ]
length=len(scores)

sum=0
for num in scores:
    sum+=num
avg=sum/length

print(avg)
