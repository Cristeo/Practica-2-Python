hombres_count = 0
suma_edad_hombres = 0
mujeres_count = 0
suma_edad_mujeres = 0

# Pedimos la primera edad para entrar al while
edad = float(input("Dame tu edad (negativa para terminar): "))

# Bucle normal mientras la edad sea mayor o igual a 0
while edad >= 0:
    sexo = input("Pon H o M: ")
    
    if sexo == "H":
        hombres_count = hombres_count + 1
        suma_edad_hombres = suma_edad_hombres + edad
    else:
        if sexo == "M":
            mujeres_count = mujeres_count + 1
            suma_edad_mujeres = suma_edad_mujeres + edad

    # Pedimos la siguiente edad dentro del bucle
    edad = float(input("Dame tu edad (negativa para terminar): "))

# Cálculo de medias con un if clásico (por si no se ha introducido ninguno)
if hombres_count > 0:
    media_hombres = suma_edad_hombres / hombres_count
else:
    media_hombres = 0

if mujeres_count > 0:
    media_mujeres = suma_edad_mujeres / mujeres_count
else:
    media_mujeres = 0

# Resultados con el formato exacto pedido
print("- Se han introducido", mujeres_count, "mujeres y la media de edad es de", media_mujeres, "años.")
print("- Se han introducido", hombres_count, "hombres y la media de edad es de", media_hombres, "años.")