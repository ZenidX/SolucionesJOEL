#Input
n_casos=int(input())
casos=list()
for i in range(n_casos):
    casos.append(dict())
    casos[-1].update({"n_tiendas":int(input())})
    casos[-1].update({"tiendas":list()})
    for i in range(casos[-1][n_tiendas]):
        casos[-1]["tiendas"].append(input().split())
    casos[-1].update({"n_articulos":int(input())})
    casos[-1].update({"compras":list()})
    for i in range(casos[-1]["n_articulos"]):
        casos[-1]["compras"].append(input().split())
precio=list()
cantid=list()
#Calculus
def calculus(caso):
    suma=0
    for compra in caso["compras"]:
        precios=list()
        cantidades=list()
        for tienda in caso["tiendas"]:
            if tienda[0]==compra[0]:
                precios.append(int(j[1]))
                cantidades.append(int(j[2]))
        for i in range(int(i[1])):
            precio_minimo=precios[0]
            for precio in precios:
                if cantidades[precios.index[precio]]>0:
                    precio_minimo=min(i,precio_minimo)
            suma+=precios[precios.index[precio]]
            cantidades[precios.index[precio]]-=1
    return suma

#Output
for i in casos:
    calculus(caso)