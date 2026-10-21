age_list=[24,25,26,27,28]
print(age_list)

name_list=["abhi","alap","jithu","kannan","manu"]
print(name_list)

name_list.append("Yazhini")
print(name_list)
age_list.insert(2,30)
print(age_list)
name_list.remove("Yazhini")
print(name_list)
age_list.pop()
print(age_list)
age_list.extend([29,30,26])
print(age_list)
age_list.sort()
print(age_list)
age_list.reverse()
print(age_list)

print(min(age_list))
print(max(age_list))
print(sum(age_list))



print(name_list[0])
print(name_list[-1])
print(name_list[2:5])

print(name_list[::-1])


student_marks={"Juli":65,"Ben":70,"Merlin":80,"Zoya":88,"Fiona":90}
print(student_marks)
print(student_marks["Fiona"])
student_marks["Janani"]=80
print(student_marks)
student_marks["Juli"]=82
print(student_marks)
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())




my_set={'a','e','i','o','u','a','a','i'}
print(my_set)
'''set is un ordered,it may not follow the same order as i given,dupliactes are not allowed(a,i repetition is not allowed''',
'''my_set[4]="s"
print(my_set)'''
''' the error came because of SET is mutable , that we can add and delete elements but cant change the elements from the set ,because it doesnt have index number since it is unordered'''




set1={1, 3, 5, 7, 9}
print(set1)
set2={2, 3, 5, 8, 10}
print(set2)

print(set1.union(set2))
print(set1.intersection(set2))
print(set2.union(set1))
print(set2.intersection(set1))



score=(int(input("Enter your score (0 to 10):")))
if  score >7 and score<=10:
    print("Above average:,well done, keep it up")
elif score>=4 and score <=7:
    print("Average: Good effort! Keep practicing, there's room for improvement")
elif score<4:
    print("Need to Improve your performance, consistent practice will lead to better results")
else:
    print("Invalid")
    

    
    








