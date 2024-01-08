# Dicionário que representa as vendas de produtos (exemplo)
vendas = {
    'produto1': 50,
    'produto2': 30,
    'produto3': 50,
    'produto4': 20,
    'produto5': 50,
}

# Encontrar a quantidade máxima de vendas
max_vendas = max(vendas.values())

# Encontrar todos os produtos que têm a quantidade máxima de vendas
produtos_mais_vendidos = []

for venda in vendas.items():
    print(f" venda -> {venda[0]}")

# Exibir o(s) produto(s) mais vendido(s)
print("Produto(s) mais vendido(s):", produtos_mais_vendidos, "com", max_vendas, "vendas.")


# Dicionário que representa as vendas de produtos (exemplo)
vendas = {
    'produto1': 50,
    'produto2': 30,
    'produto3': 50,
    'produto4': 20,
    'produto5': 50,
}

# Encontrar a quantidade máxima de vendas
max_vendas = max(vendas.values())

# Encontrar todos os produtos que têm a quantidade máxima de vendas
produtos_mais_vendidos = [produto for produto, quantidade in vendas.items() if quantidade == max_vendas]

# Exibir o(s) produto(s) mais vendido(s)
print("Produto(s) mais vendido(s):", produtos_mais_vendidos, "com", max_vendas, "vendas.")
