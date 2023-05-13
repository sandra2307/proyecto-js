for j in range(3):  # llamado outer for o outer loop
    for k in range(2):  # llamado inner for o inner loop
        print(f"{j}, {k}")  # f=formateado

# la primera vez j=0 y k=0

# la segunda vez j=0 sigue siendo 0 y se ejecuta por segunda vez la segunda linea k=1
# la siguiente vez tocaría j=0 y k=2 pero k no puede ser 2, por lo que pasamos a cambiar la primera linea

# la tercera vez j=1 y la segunda linea vuelve a ser k=0

# la cuarta vez j=1 y la segunda puede ser k=1

# despues no puede ser k=2, asiq volvemos a la primera line. j=2 y k=0

# la siguiente vez j=2 y k=1

# la última vez k no puede ser 2. y volvemos a j y no puede ser 3. por lo que el loop se ha terminado
