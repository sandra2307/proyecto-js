# for - para iterar una lista de elementos, para buscar elementos, operaciones matematicas...

# for numero in range(5):
#     print(numero, numero * "hola mundo")
# range 5 lo que hace es crear un secuencia de numeros. range(5) = (0,1,2,3,4)

buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break

    # cuando llega al 3 se para


buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontrado")

# se para en el 4 por el range(5)

for char in "Ultimate python":
    print(char)
# muestra todos los caracteres de "Ultimate Python", uno en cada linea
