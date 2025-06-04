# Una persona invierte su capital en un banco y desea saber cuánto dinero ganará
# en un mes, teniendo en cuenta que el banco paga 2% mensual. ¿Cuánto ganará
# en seis meses si deja su dinero invertido?

TASA_INTERES = 0.02

# Se asume que el capital debe ser mayor a cero
capital_inicial = float(input("Ingrese el capital a invertir: "))
while capital_inicial <= 0:
    capital_inicial = float(input("Ingrese el capital a invertir: "))

# Se asume que el plazo debe ser mayor a cero
meses_cant = int(input("Ingrese el plazo de su inversión, en meses: "))
while meses_cant <= 0:
    meses_cant = int(input("Ingrese el plazo de su inversión, en meses: "))

# Se asume interés simple

interes = round(capital_inicial * (TASA_INTERES)* meses_cant)

print("EL interés generado por su capital en", meses_cant, "meses es:", interes)