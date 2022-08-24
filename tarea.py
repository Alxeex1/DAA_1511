""" 
Se requiere controlar el número de habitantes de un edificio con 6 pisos y 4 puertas (A, B, C Y D) en cada piso.
Se deberá realizar un programa que pida al usuario que introduzca el numero de habitantes de cada puerta del edificio. 
El programa debe decir la puerta que más habitantes tiene todo el edificio.


"""

pisos = int(input("Introduce el numero de pisos del edificio: "))
puerta = int(input("Introduce el numero de puertas: "))

matriz = []
for i in range(pisos):
    matriz.append([0]*puerta)

mayor = None  # Mayor valor encontrado hasta el momento.
fila = 0      # Fila de `mayor`
columna = 0   # Columna de `mayor`
for i in range(pisos):
    for j in range(puerta):
        matriz[i][j] = int(input("Piso {}, Puerta {} : ".format(i + 1, j + 1)))
        if mayor is None: # Inicializamos mayor aqui.
            mayor = matriz[i][j] - 1
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            fila = i
            columna = j

print("El numero mayor de habitantes es: ")
print(mayor)
print("Se encuentra en el Piso", pisos , ",y es la  puerta", puerta )
print("La matriz es:")
print(matriz)
