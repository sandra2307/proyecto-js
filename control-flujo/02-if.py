edad = 70
if edad > 65:  # : indica lo que se encuentra anidado # si if evalua true ya no pasa al elif y else
    print("puede ver la película con superdescuento")
elif edad > 54:
    print("puede ver la película con descuento")
elif edad > 17:
    print("puede ver la película")  # elif es como un añadido
else:  # si if y else van a false se va a else
    print("No puedes entrar")

print("Listo")
