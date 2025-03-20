#Inputs
n_casos=int(input())
case_paths=list()
for i in range(n_casos):
    n_path=int(input())
    case_paths.append({"n_caminos":n_path,"caminos":list(),"origen":"","contador":0})
    for j in range(n_path):
        case_paths[i]["caminos"].append(input().split("->"))
    case_paths[i]["origen"]=input() 

#Calculus
for i in range(n_casos):
    origen=case_paths[i]["origen"]
    sitios_n_pasos={origen}
    while "HITLER" not in sitios_n_pasos and case_paths[i]["contador"]<case_paths[i]["n_caminos"]:
        nuevossitios=set()
        for sitio in sitios_n_pasos:
            for j in case_paths[i]["caminos"]:
                if j[0]==sitio:
                    nuevossitios.add(j[1])
        sitios_n_pasos|=nuevossitios
        case_paths[i]["contador"]+=1
    if "HITLER" not in sitios_n_pasos:
        case_paths[i]["contador"]="IMPOSSIBLE"

#Outputs
for i in range(n_casos):
    print(case_paths[i]["contador"])
