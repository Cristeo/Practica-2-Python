# Pedimos el número N entero y positivo
N = int(input("Introduce un número entero positivo (N): "))

# Inicializamos la suma en 0
S = 0

# Recorremos desde el 1 hasta el N
for i in range(1, N + 1):
    S = S + (1 / i)

# Mostramos el resultado
print("El resultado de la serie (S) es:", S)