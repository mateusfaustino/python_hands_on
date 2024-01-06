'''
    Usando dicionários crie uma lista com 5 países e suas capitais. Peça para o usuário digitar o nome de um país.
    Se o país estiver na lista, imprima "A capital de [país] é [capital]".
    Se o país não estiver na lista, imprima "Desculpe, não temos informação desse país".
'''
capitais = {
    'Brasil':'Brasilia',
    'Argentina': 'Buenos Aires',
    'Chile':'Santiago',
    'Mexico':'Cidade do Mexico',
    'França': 'Paris'
}

pais_usuario = input("Digite um país: ")

if pais_usuario in capitais:
    print(f'A capital de {pais_usuario} é {capitais[pais_usuario]}')
else:
    print(f'Desculpe, não temos informação desse país')
