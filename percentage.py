
n = int(input("ogrenci sayisi :"))
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("ortalamasi hesaplanacak öğrenci")
#print(student_marks)
sum=0
for i in student_marks.get(query_name):
    print(i)
    sum+=i
#print(sum)
#print(len(student_marks.get(query_name)))
c=len(student_marks.get(query_name))
avarege=sum/c
#print (avarege,2)
print(f"avarege: {avarege:.2f}")