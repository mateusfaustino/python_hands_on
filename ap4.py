def eh_palindromo(s):
    return s == s[::-1]

def strings_palindromos(lista_strings):
    palindromos = []
    for string in lista_strings:
        if eh_palindromo(string):
            palindromos.append(string)
    return palindromos

# Exemplo de lista de strings
lista_de_strings = ["ana", "arara", "python", "radar", "socorrammesubinoonibusemmarrocos"]

# Obtendo as strings palíndromos da lista
palindromos = strings_palindromos(lista_de_strings)
print("Strings palíndromos na lista:", palindromos)


