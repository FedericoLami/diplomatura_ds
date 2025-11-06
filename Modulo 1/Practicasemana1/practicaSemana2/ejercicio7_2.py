lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
objetivo = 15
print (len(lista))

def encontrar_subsecuencias_suma(lista, objetivo):
    resultados = []
    n = len(lista)

    # Función auxiliar para encontrar todas las subsecuencias que suman el objetivo
    def backtrack(i, sublista, suma):
        if suma == objetivo:
            resultados.append(sublista)
            
        elif suma > objetivo or i == n:
            return
        else:
            # Incluir el i-ésimo elemento
            backtrack(i+1, sublista + [lista[i]], suma + lista[i])
            
            # No incluir el i-ésimo elemento
            backtrack(i+1, sublista, suma) 

    # Llamada inicial a la función auxiliar
    backtrack(0, [], 0)

    return resultados

resultados = encontrar_subsecuencias_suma(lista, objetivo)
print(resultados)