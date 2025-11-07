print("Ejercicio 1 con while")

#Inicializamos una variable contador
contador_numero = 1

#Mientras contador sea menor o igual a 5
while contador_numero <=5:    
    print(f"Numero: {contador_numero}")
    contador_numero = contador_numero + 1 #Incrementamos el contador

# Mientras el número sea mayor que 0
while numero > 0:
    print(f"Faltan {numero} segundos...")
    numero = numero - 1  # Decrementamos el contador

print("¡Despegue!")

print("\nEjercicio 3 con while - suma acumulativa")
# Inicializamos las variables
numeros = 1
suma = 0

# Mientras numeros sea menor o igual a 50
while numeros <= 50:
    suma = suma + numeros   # Acumulamos la suma
    numeros = numeros + 1   # Incrementamos el contador

print(f"La suma del 1 al 50 es: {suma}\n")



print("\nEjercicio 4 - Tabla de Multiplicar")
# Inicializamos el contador
multiplicador = 1

# Mientras el multiplicador sea menor o igual a 10
while multiplicador <= 10:
    resultado = 7 * multiplicador
    print(f"7 x {multiplicador} = {resultado}")
    multiplicador = multiplicador + 1

print("¡Tabla completa!\n")

print("\nEjercicio 5 - Números pares del 2 al 50")
# Inicializamos el contador en 2 (primer par)
numeros_pares = 2

# Mientras el número sea menor o igual a 50
while numeros_pares <= 50:
    print(f"Número par: {numeros_pares}")
    numeros_pares = numeros_pares + 2  # Incrementamos de 2 en 2

print("¡Todos los paresmostrados!\n")

print("\nEjercicio 6 - Dividir un número a la mitad")
# Inicializamos con un número
numero_a_dividir = 100

# Mientras el número sea mayor o igual a 1
while numero_a_dividir >= 1:
    print(f"Número actual: {numero_a_dividir}")
    numero_a_dividir = numero_a_dividir / 2  # Dividimos entre 2

print(f"Número final (menor a 1): {numero_a_dividir}")

# Ejercicio 7
print("\nEjercicio 7 - Loop infinito")
# Queremos contar del 1 al 5
contador = 1
while contador <= 5:
 print(f"Número: (contador]")
print("Aqui terminan los ejercicios de while")

# Ejercicio 8
print("\nEjercicio & - Loop corregido")
# Queremos contar del 1 al 5
contador = 1
while contador <= 5:
 print(f"Número: (contador)")
contador = contador + 1 # ¡Ahora sí incremetamos!

print("¡Loop terminado correctamente/\n")