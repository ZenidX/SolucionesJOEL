#Input XAVI LARA
n_casos = int(input())
casos = []
for i in range(n_casos):
    casos.append([int(i) for i in input().split()])
    
#Calculus
def calculus(caso):
    onda=caso[1:]
    onda.sort(reverse=True)
    result=[]
    for i in range(len(onda)): # 0 1 2 3 4 5 6 ... len(onda)-1
        if i%2==0: #0 2 4 6 8 10 ...
            result.append(onda[int(i/2)]) # 0=(0/2) 1=(2/2) 2=(4/2) 3=(6/2) 4=(8/2) 5=(10/2) ...f(x)=x/2
        else: #i%2!=0   1 3 5 7 9 11 ...
            result.append(onda[int(-(i+1)/2)]) # -1=(-(1+1)/2) -2=(-(3+1)/2) -3=(-(5+1)/2) -4=(-(7+1)/2) ...g(x)=-(i+1)/2
    result.reverse()
    return result
    
#Output
for i in casos:
    print(*calculus(i))
    
    
'''
#Input DAVID VILELLAS
n_casos = int(input())
casos = []
for i in range(n_casos):
    casos.append([int(i) for i in input().split()])
    
#Calculus
def calculus(caso):
    l1 = caso[1:]
    l1.sort()
    petit = len(l1)//2 
    l2 = []
    if len(l1)%2 == 0:
        # QUANTITAT DE VALORS PARELL
        petit -=1
        gran = petit +1
        for i in range(int(len(l1)/2)):
            if petit >= 0:
                l2.append(l1[petit])
                petit -= 1
            if gran<len(l1):
                l2.append(l1[gran])
                gran += 1
    else:
        # QUANTITAT DE VALORS SENAR
        gran = petit +1
        l2.append(l1[petit])
        petit -= 1
        for i in range(int(len(l1)/2)):
            if gran<len(l1):
                l2.append(l1[gran])
                gran += 1
            if petit >= 0:
                l2.append(l1[petit])
                petit -= 1
#    print(f"petit és: {petit}")
#    print(f"gran és: {gran}")
    return l2
    
#Output
for i in casos:
    print(*calculus(i))
'''