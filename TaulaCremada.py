import math
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
    slopes=list()
    for i in caso:
        vectors.append(list())
        slopes.append(list())
        for j in caso:
            vectors[-1].append([i[k]-j[k] for k in range(2)])
            div=math.gcd(vectors[-1][-1][0],vectors[-1][-1][1])
            if div == 0:
                slope="Nul"
            elif div!=0:
                if vectors[-1][-1][0]==0:
                    slope="Ver"
                    vectors[-1][-1][1]=1
                elif vectors[-1][-1][1]==0:
                    vectors[-1][-1][0]=1
                    slope=0
                else:
                    vectors[-1][-1][0]/=div
                    vectors[-1][-1][1]/=div
                    if vectors[-1][-1][0]<0:
                        vectors[-1][-1][0]*=-1
                        vectors[-1][-1][1]*=-1
                    slope=vectors[-1][-1][1]/vectors[-1][-1][0]
            slopes[-1].append(slope)
    for i in vectors:
        print(i)
    for i in slopes:
        print(i)
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
