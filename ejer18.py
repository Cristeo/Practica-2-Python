suma_grupo = 0
total_alumnos = 0

# Pedimos el primer número de lista antes del bucle
num_lista = int(input("Introduce el número de la lista (0 para terminar): "))

while num_lista != 0:
  nota1 = int(input("Introduce nota de la 1a evaluación: "))
  nota2 = int(input("Introduce nota de la 2a evaluación: "))
  nota3 = int(input("Introduce nota de la 3a evaluación: "))

  # Media del alumno actual
  media_alumno = (nota1 + nota2 + nota3) / 3

  # Mostramos con el formato exacto pedido
  print(
      "El alumno con número de lista",
      num_lista,
      "tiene un",
      media_alumno,
      "de nota media.",
  )

  # Acumulamos para la media del grupo
  suma_grupo = suma_grupo + media_alumno
  total_alumnos = total_alumnos + 1

  # Volvemos a pedir el número de lista para la siguiente vuelta (o un 0 para salir)
  num_lista = int(input("Introduce el siguiente número de la lista (0 para terminar): "))

# Al salir del bucle, calculamos la media del grupo si se introdujo al menos un alumno
if total_alumnos > 0:
  media_grupo = suma_grupo / total_alumnos
  print("\nLa media del grupo en LENGUA es:", media_grupo)
else:
  print("\nNo se han introducido alumnos.")