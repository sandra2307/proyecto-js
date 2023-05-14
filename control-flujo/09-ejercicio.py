# bienvenidos a la calculadora
# Para salir escribe Salir
# Las operaciones son suma, multi, div y resta
# Ingresa numero:

print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son suma, multi, div y resta")


# SOLUCIÓN
resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":    # si escribe salir se para
            break
        # si escribe un integer seguimos a la siguiente linea
        resultado = int(resultado)

    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break

    n2 = input("Ingresa siguiente número ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida")
        break

    print(f"El resultado es: {resultado}")


# MI SOLUCIÓN
#     n1 = input("Ingresa tu número")
#     print(n1)
#     op = input("Ingresa un operador")
#     print(op)
#     n2 = input("Ingresa otro número")
#     print(n2)
#     suma = n1 + n2
#     resta = n1 - n2
#     multi = n1 * n2
#     div = n1 / n2


# if op == suma:
#     print(suma)
# elif op == resta:
#     print(resta)
# elif op == multi:
#     print(multi)
# elif op == div:
#     print(div)
