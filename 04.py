'''
Use a lista 'frutas' do exercício anterior. Remova o item 'manga' usando o método remove(). 
Após isso, remova o último item da lista usando o método del.
'''

frutas = ['maçã', 'banana', 'manga', 'uva','abacaxi']

frutas.remove('manga')

del frutas[-1]

print(frutas)