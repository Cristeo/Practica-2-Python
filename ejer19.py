anio_inicio = int(input("Introduce el año de inicio: "))
capital = float(input("Introduce el capital inicial: "))
interes = float(input("Introduce el interés fijo (en %): "))
anios = int(input("Introduce el número de años que estará rindiendo: "))

for i in range(anios):
  anio_actual = anio_inicio + i
  capital_inicial_anio = capital
  
  # Calculamos el beneficio de este año (Capital * (interés / 100))
  beneficio = capital_inicial_anio * (interes / 100)
  
  # El nuevo capital a fin de año es el inicial más el beneficio
  capital = capital_inicial_anio + beneficio

  print("\n--- Año:", anio_actual, "---")
  print("Capital a principios de año:", capital_inicial_anio)
  print("Beneficio obtenido en ese año:", beneficio)
  print("Capital a fin de año:", capital)