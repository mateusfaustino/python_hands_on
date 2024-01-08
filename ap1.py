# # Lista original de números
# lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Criando uma nova lista com números pares usando compreensão de lista
# lista_pares = [num for num in lista_original if num % 2 == 0]

# # Exibindo a lista com os números pares
# print(lista_pares)

# Lista original de números
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializando uma lista vazia para armazenar os números pares
lista_pares = []

# Percorrendo a lista original com um loop for
for num in lista_original:
    # Verificando se o número é par
    if num % 2 == 0:
        # Adicionando o número par à lista de números pares
        lista_pares.append(num)

# Exibindo a lista com os números pares
print(lista_pares)
