suma_edad = 0

for i in range (5):
    edad = float(input("Dame tu edad: "))
    suma_edad = suma_edad + edad

    if edad < 0:
        print("Edad no valida")

media = suma_edad / 5

if media >= 18:
    print ("Media mayores de edad")
else:
    print ("Media menores de edad")


print("Media ha sido", media)


