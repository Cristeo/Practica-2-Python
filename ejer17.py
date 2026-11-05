suma_notas = 0
max_nota = -1  # Empezamos con un valor muy bajo para que la primera nota lo supere seguro
alumno_max = 0
min_nota = 11  # Empezamos con un valor mayor a la nota máxima posible (10)
alumno_min = 0

for i in range(10):
  print("--- Alumno número:", i + 1, "---")
  num_lista = int(input("Introduce el número de la lista: "))
  nota = int(input("Introduce la nota de Matemáticas: "))

  # Sumamos la nota para la media
  suma_notas = suma_notas + nota

  # Comprobamos si es la nota máxima hasta el momento
  if nota > max_nota:
    max_nota = nota
    alumno_max = num_lista

  # Comprobamos si es la nota mínima hasta el momento
  if nota < min_nota:
    min_nota = nota
    alumno_min = num_lista

media = suma_notas / 10

print("\n========== RESULTADOS ==========")
print("Alumno con la nota máxima:")
print("-> Número de lista:", alumno_max, "con una nota de:", max_nota)
print("Alumno con la nota mínima:")
print("-> Número de lista:", alumno_min, "con una nota de:", min_nota)
print("La media de la clase en Matemáticas es:", media)