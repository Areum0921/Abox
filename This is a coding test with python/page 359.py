N=int(input())
student = []
for i in range(N):
    info = list(map(str,input().split(" ")))
    student.append(info)

student = sorted(student, key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in student:
    print(i[0])
