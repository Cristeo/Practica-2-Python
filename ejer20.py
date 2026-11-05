N = int(input("Introduce cuántos números de la serie de Fibonacci quieres ver: "))

a = 1
b = 1

if N >= 1:
  print(a)
if N >= 2:
  print(b)

# El bucle empieza a calcular a partir del tercer número
for i in range(3, N + 1):
  siguiente = a + b
  print(siguiente)
  
  # Actualizamos las variables para la siguiente suma
  a = b
  b = siguiente