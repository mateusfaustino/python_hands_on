# Conjunto de nomes de cores
cores = {'azul', 'verde', 'amarelo', 'vermelho', 'roxo', 'preto', 'branco'}

# Função para retornar as cores com mais de quatro letras
def cores_mais_quatro_letras(cores):
    cores_mais_longas = set()  # Inicializa um conjunto vazio para armazenar as cores com mais de quatro letras
    for cor in cores:
        if len(cor) > 4:
            cores_mais_longas.add(cor)  # Adiciona a cor ao conjunto se tiver mais de quatro letras
    return cores_mais_longas

# Obtendo as cores com mais de quatro letras usando a função
cores_com_mais_de_quatro_letras = cores_mais_quatro_letras(cores)
print("Cores com mais de quatro letras:", cores_com_mais_de_quatro_letras)
