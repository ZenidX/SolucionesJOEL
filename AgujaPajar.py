#Input
a=input()
b=input()

#Calculus
def casos(a_dire, text, i):
    if i == 0:
        return False
    else:
        resultat = []
        
        return resultat, i-1
def calculus():
    resultado=0
    a_dire = {} 
    for element in a:
        if element in a_dire.keys():
            a_dire[element] += 1
        else:
            a_dire[element] = 1
    for element in a_dire.keys():
        
    return a_dire

#Output
print(calculus())
