#Input
n_casos=int(input())
casos=[]
for i in range(n_casos):
  caso={
    "nens":input().split(),
    "acti":int(input()),
    "capa":[int(i) for i in input().split()]
  }

#Calculus
def calculus(caso):
    j=0
    for i in range(caso["acti"]):
        nens_acti=[]
        while caso["capa"]!=0 or j==len(caso["nens"]):
            nens_acti.append(caso["nens"][j])
            caso["capa"][i]=caso["capa"][i]-1
            j=j+1
        print(f"Activitat {i+1}: {nens_acti}")
    if j==len(caso["nens"]):
        print("Tots els nenes han estat assignats")
    else:
        print("Nens sobrants: ","")
        while j!=len(caso["nens"]):
            print(caso["nens"][j],"")
        print("")

#Output
for caso in casos:
  calculus(caso)
