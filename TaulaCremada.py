#Input
marcas=int(input())
casos=list()
while marcas!=0:
    casos.append(list())
    for i in range(marcas):
        casos[-1].append([int(i) for i in input().split(" ")])
    marcas=int(input())
    
    
#Calculus
def calculus(caso):
    mesa=[[" " for i in range(10)] for j in range(10)]
    for i in caso:
        print(i)
        mesa[i[0]][i[1]]="#"
    for i in mesa:
        print(i)
    vectors=list()
    for i in caso:
        vectors.append(list())
        for j in caso:
            vectors[-1].append([i[k]-j[k] for k in range(2)])
    condition=True
    if condition:
        return True
    else:
        return False

#Output
print(casos)
for i in casos:
    if calculus(i):
        print("SI")
    else: print("No")
