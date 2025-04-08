#input
m=int(input())
n=int(input())
mapa=[]
for i in range(n):
    mapa.append([int(i) for i in input().split(" ")])

#calculus
def calculus():
    sitios={(1,1)}
    whille
    for i in sitios:
        nuevos_sitios=lugares(mapa[i[0],i[1]])
        sitios.add(nuevos_sitios)
        if (m,n) in sitios:
            return "yes"
    

def lugares(valor):
    div=[]
    for i in range(1,valor+1):
        if valor%i==0:
            div.append(i)
    lugaretes=[]
    for i in div:
        for j in div:
            if i!=j:
                lugaretes.append((i,j))
    return lugaretes
#output
print(calculus())
