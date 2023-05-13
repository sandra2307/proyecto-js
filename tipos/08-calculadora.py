# la funcion input permite obtener datos del usuario
n1 = input("ingresa primer numero")
n2 = input("ingresa segundo numero")

n1 = int(n1)
n2 = int(n2)
# print(n1 + n2)  # en el terminal primero aparece n1, hay que meter un numero y hay que darle intro para que aparezca n2

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2
divNO = n1 // n2
pot = n1 ** n2

# la f permite que se ejecute de manera correcta, es como el mensaje final
mensaje = f"""
para los números {n1} y {n2},
el resultado de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado de la multiplicación es {multi}.
el resultado de la división es {div}.
el resultado de la división sin decimales es {divNO}
el resultado de la potencia es {pot}.
"""

print(mensaje)
