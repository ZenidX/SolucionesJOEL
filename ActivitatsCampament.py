#Input
n_casos=int(input())
casos=[]
for i in range(n_casos):
  caso={
    "nens":input().split(),
    "acti":int(input()),
    "capa":[int(i) for i in input().split()]
  }
  casos.append(caso)

#Calculus
def calculus(caso):
    j=0
    for i in range(caso["acti"]):
        nens_acti=[]
        while caso["capa"][i]>=0 and j<len(caso["nens"]):
            nens_acti.append(caso["nens"][j])
            caso["capa"][i]=caso["capa"][i]-1
            j=j+1
        print(f"Activitat {i+1}: ",end="")
        print("[",end="")
        for i in range(len(nens_acti)-1):
            print(f"{nens_acti[i]}, ", end="")
        if nens_acti!=[]:
            print(f"{nens_acti[-1]}]")
        else: 

    if j==len(caso["nens"]):
        print("Tots els nenes han estat assignats")
    else:
        print("Nens sobrants: ",end="")
        while j<len(caso["nens"]):
            print(caso["nens"][j],end="")
            j=j+1
        print("")
    print("")
    return

#Output
for caso in casos:
    calculus(caso)
