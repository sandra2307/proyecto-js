# and - para dos condiciones por ejemplo: x>5 y=10. si los dos son true, evalua en true.
# si uno de los dos evalua en false no arroja el mensaje
# or - x>5 y>10 - con que uno sea true el resultado completo evalua true. si los dos son false, los dos evaluan false.
# not - negar el resultado de una operacion
# se ejecuta siempre de izda a dcha, a no ser que indiquemos un parentesis. parentesis siempre primero.

gas = False
encendido = True
edad = 18

if gas and encendido:
    print("puedes avanzar")

if gas or encendido:
    print("puedes avanzar")

if not gas and encendido and edad > 17:
    print("puedes avanzar")

if gas and (encendido or edad > 17):
    print("puedes avanzar")

if not gas and (encendido or edad > 17):
    print("avanza macho")


# OPERACIONES DE CORTO CIRCUITO

if not gas and encendido and edad > 17:
    print("puedes avanzar")

# si lo que hay a al izda del and es false, todo lo que hay a la dcha no se va a ejecutar

if not gas or encendido or edad > 17:
    print("puedes avanzar")

# en or basta que con el valor de la izda sea true para que no se evalue el valor de la dcha
# si el valor de la izda es false entonces se sigue evaluando el valor de la dcha de or
