#Input
n_casos=int(input())
casos=[]
for i in range(n_casos):
    casos.append([])
    n_tareas=int(input())
    for j in range(n_tareas):
        casos[i].append(input().split("-"))
        casos[i][j][1]=casos[i][j][1].split(",")
for i in casos:
    for j in i:
        print(*j)
#Calculus
def calculus(caso):
    result=0
    return result

#Output
for i in casos:
    print(*calculus(i))

