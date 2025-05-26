"""d)	[**] En una empresa el pago a sus trabajadores depende de las horas trabajadas a la semana y la sucursal en la que se encuentran. En la sucursal A se paga $10/hora si se trabajan menos de 40 horas, y en la sucursal B se paga $12/hora si se trabajan menos de 45 horas. Las horas extra en la sucursal A se cobran a $20 y en la sucursal B a $25. Calcule el salario semanal de acuerdo a las horas trabajadas y la sucursal ingresada por el usuario."""

horas = int(input("Ingrese las horas trabajadas: "))
sucursal = input("Ingrese la sucursal (A o B): ").upper()
pago = 0
salario = 0

if sucursal == "A":
    if horas <= 40:
        salario = horas * 10
    else:
        horas_extra = horas - 40
        salario = (40 * 10) + (horas_extra * 20)
elif sucursal == "B":
    if horas <= 45:
        salario = horas * 12
    else:
        horas_extra = horas - 45
        salario = (45 * 12) + (horas_extra * 25)
else:
    print("Sucursal no válida. Debe ser A o B.")
    salario = 0
print("El salario semanal es:", salario)


print(ty)