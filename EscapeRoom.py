#input
m=int(input())
n=int(input())
mapa=[]
for i in range(m):
    mapa.append([int(i) for i in input().split(" ")])

#calculus
def calculus():
    sitios={(0,0)}
    k=0
    flag=True
    while (m,n) not in sitios and flag:
        sit=[i for i in sitios]
        for i in range(len(sit)):
            nuevos_sitios=lugares(mapa[sit[i][0]][sit[i][1]])
            if nuevos_sitios.issubset(sitios):
                flag=False    
            sitios=sitios.union(nuevos_sitios)
            print(sitios)
    if (m,n) in sitios:
        return "yes"
    else: return "no"
    
def lugares(valor):
    div=[]
    for i in range(1,valor+1):
        if valor%i==0:
            div.append(i)
    lugaretes=set()
    for i in div:
        for j in div:
            if i*j==valor:
                lugaretes.add((i-1,j-1))
    lugariños=[i for i in lugaretes]
    for i in lugariños:
        if i[0]>n or i[1]>m:
            lugaretes.remove(i)
    return lugaretes
#output
print(calculus())

