casos = int(input())
resultats = []
for _ in range(casos):
    c_inicial, n_eventos, n_dias = list(map(int, input().split()))
    dias_evento = list(map(int, input().split()))
    n_coladas = 0
    contador_camisetas = c_inicial
    contador_dias = 1
    while contador_dias <= n_dias:
        if contador_camisetas == 0:
            n_coladas += 1
            contador_camisetas = c_inicial
        if contador_dias in dias_evento:
            contador_camisetas += dias_evento.count(contador_dias)
            c_inicial += dias_evento.count(contador_dias)
        contador_dias += 1
        contador_camisetas -= 1
    resultats.append(n_coladas)

for element in resultats:
    print(element)