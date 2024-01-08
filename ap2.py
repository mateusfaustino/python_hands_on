# Dicionário de produtos (exemplo inicial)
produtos = {
    1: {'nome': 'Camiseta', 'preco': 29.99, 'estoque': 50},
    2: {'nome': 'Calça', 'preco': 49.99, 'estoque': 30},
    3: {'nome': 'Meias', 'preco': 9.99, 'estoque': 100}
}

# Função para adicionar um novo produto
def adicionar_produto(id_produto, nome, preco, estoque):
    produtos[id_produto] = {'nome': nome, 'preco': preco, 'estoque': estoque}

# Função para remover um produto pelo ID
def remover_produto(id_produto):
    if id_produto in produtos:
        del produtos[id_produto]
    else:
        print("Produto não encontrado.")

# Função para atualizar informações de um produto pelo ID
def atualizar_produto(id_produto, nome=None, preco=None, estoque=None):
    if id_produto in produtos:
        if nome:
            produtos[id_produto]['nome'] = nome
        if preco:
            produtos[id_produto]['preco'] = preco
        if estoque:
            produtos[id_produto]['estoque'] = estoque
    else:
        print("Produto não encontrado.")

# Testando as funções
print("Produtos existentes:", produtos)

# Adicionando um novo produto
adicionar_produto(4, 'Boné', 19.99, 20)
print("Após adicionar um novo produto:", produtos)

# Removendo um produto pelo ID
remover_produto(2)
print("Após remover um produto:", produtos)

# Atualizando informações de um produto pelo ID
atualizar_produto(3, nome='Meias Esportivas', estoque=80)
print("Após atualizar informações de um produto:", produtos)
