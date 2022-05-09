def solution(n, classes, b, c):
    classdict = {}
    answer = 0
    for j in classes:
        element = 0
        if j in classdict:
            answer = answer + classdict[j]
        else:
            if (j < b): element = 1
            else:
                if ((j-b)%c)>0: element = 1
                element = element+ ((j - b) // c + 1)
            classdict[j] = element
 
        answer = answer+ element
    print(answer)
    return answer
                

n = int(input())
classes = []
a = input().split()
for i in a:
    classes.append(int(i))
b, c = map(int, input().split())
solution(n,classes,b,c)
