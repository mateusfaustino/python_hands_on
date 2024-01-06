'''
Crie um programa que calcula a quantidade de tinta necessária para pintar uma parede
O usuário deve fornecer as seguintes informações: Rendimento, altura e largura
O programa deve mostrar na tela a mensagem "Você necessita de x latas de tinta".
'''
def calculo_tinta(rendimento, altura, largura):
    area = altura*largura
    total_latas = area/rendimento
    return total_latas


rendimento = float(input('Qual é o rendimento da lata? ')) 
altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))

total_latas = calculo_tinta(rendimento, altura, largura)

print(f'Você precisará comprar {total_latas} latas')