# # vamos a duplicar el numero hasta que sea igual o mayor a 100
numero = 1
while numero < 100:  # no olvidarme de los dos puntos!!
    # imprime el numero que es 1 y luego hace la linea siguiente, que es multiplicarlo por 2
    print(numero)
    numero = numero * 2  # o numero *= 2

comando = ""
while comando != "salir":
    comando = input("$")
    print(comando)

comando = ""
while comando.lower() != "salir":
    comando = input("$")
    print(comando)
# el comando lower() convierte todas las letras en minuscula para que salir se pueda esribir de cualquier manera

while True:
    comando = input("$")
    print(comando)
    if comando.lower() == "salir":
        break
