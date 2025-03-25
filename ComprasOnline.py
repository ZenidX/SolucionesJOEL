#Input
n_casos=int(input())
casos=list()
for i in range(n_casos):
    casos.append(dict())
    casos[-1].update({"n_tiendas":int(input())})
    casos[-1].update({"tiendas":list()})
    for j in range(casos[-1]["n_tiendas"]):
        casos[-1]["tiendas"].append(dict())
        casos[-1]["tiendas"][-1].update({"n_articulos":int(input())})
        casos[-1]["tiendas"][-1].update({"articulos":list()})
        for k in range(casos[-1]["tiendas"][-1]["n_articulos"]):
            casos[-1]["tiendas"][-1]["articulos"].append(input().split(" "))
    casos[-1].update({"n_articulos":int(input())})
    casos[-1].update({"compras":list()})
    for j in range(casos[-1]["n_articulos"]):
        casos[-1]["compras"].append(input().split(" "))
        
#Calculus
precios=list()
cantidades=list()
def calculus(caso):
    suma=0
    for compra in caso["compras"]:
        precios=list()
        cantidades=list()
        for tienda in caso["tiendas"]:
            for articulo in tienda["articulos"]:
                if articulo[0]==compra[0]:
                    precios.append(int(articulo[1]))
                    cantidades.append(int(articulo[2]))
        for i in range(int(compra[1])):
            precio_minimo=100
            for j in range(len(precios)):
                if cantidades[j]>0:
                    precio_minimo=min(precios[j],precio_minimo)
            suma+=precio_minimo
            cantidades[precios.index(precio_minimo)]-=1
    return suma

#Output
for caso in casos:
    print(calculus(caso))