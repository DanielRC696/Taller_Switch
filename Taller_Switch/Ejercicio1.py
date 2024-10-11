# inicializa la lista de numeros
numeros = [1,2,3,4,5,6,7,8,9,10,11,12]

def suma_pares(numeros):
    suma = 0
    for numero in numeros:
        if numero % 2 == 0: # verifica si el numero es par
            suma += numero  # suma el numero al total
    return suma


# Llama a la funcion
resultado = suma_pares(numeros)
print(f"Total numeros sumados: {resultado}")

