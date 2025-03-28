#Input
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