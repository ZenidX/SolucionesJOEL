#Input
n_casos=int(input())
casos=[]
for i in range(n_casos):
    casos.append([])
    n_tareas=int(input())
    for j in range(n_tareas):
        casos[i].append(input().split("-"))
        casos[i][j][1]=casos[i][j][1].split(",")


#Calculus
def calculus(caso):
    orden=dict()
    for i in caso:
        orden.add({i[0]:len(i[1])})
    for i in range(len(orden)):
        
    return result

#Output
for i in casos:
    print(*calculus(i))