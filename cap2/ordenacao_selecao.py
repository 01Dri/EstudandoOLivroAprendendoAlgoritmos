def busca_menor(arr):
    menor = arr[0] # 5
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i] #5 -> 3 (menor antes era o 5, agora é o 3)
            menor_indice = i # Novo indice do menor valor é o da iteração atual
    return menor_indice

def ordena_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr) #Pega o menor valor do array e coloca em um novo array
        novo_arr.append(arr.pop(menor))
    return novo_arr


print(ordena_por_selecao([5, 3, 2, 10])) # Resultado em um novo array ordenado

#Vale ressaltar que o tempo de crescimento desse algorimo é de o(n2), 
#Pois esse algoritmo cresce de forma linear n vezes 