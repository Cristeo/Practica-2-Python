C_Snota = 0
C_Nnota = 0
suma_nota = 0

for i in range (5):
    nota = float(input("Dame una nota: "))
    suma_nota = suma_nota + nota

    if nota >= 5:
        print("Aprobado")
        C_Snota = C_Snota + 1
    else:
        print("Suspendido")
        C_Nnota = C_Nnota + 1

media = suma_nota / 5

print("Total aprobados:", C_Snota)
print("Total Suspendidos:", C_Nnota)
print("Media de notas", media)


