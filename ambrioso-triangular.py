# Inputs
n_casos = int(input())
intros = []
for _ in range(n_casos):
    intros.append(int(input()))

# Calculus+
def calcular(caso):
    result = 0
    sum_antes = 0
    for i in range(1,caso+1):
        result += sum_antes + i
        sum_antes = sum_antes + i
    return result

# Outputs
for element in intros:
    print(calcular(element))