# inicializa la lista de numeros
numeros = [1, 2, 2, 3, 4, 4, 5, 5, 6]

def elimina_Duplicados(numeros):
    nueva_lista = []  #
    numeros_vistos = set()  # Conjunto para almacenar los numeros vistos

    for numero in numeros:  # Ciclo que recorre la lista
        if numero not in numeros_vistos: # verifica si ya se ha visto
            nueva_lista.append(numero)   # agrega a la nueva lista
            numeros_vistos.add(numero)   # agrega al conjunto

    return nueva_lista  # Devolver la lista sin duplicados

# Llamada a la funcion, muestra el resultado
resultado = elimina_Duplicados(numeros)
print(resultado)
