'''
    Um grupo de jóvens estão concorrendo a uma vaga de trabalho. 
    Dessas pessoas, o grupo das que possuem CNH é representado pelo set {'Maria', 'João', 'Pedro', 'Tiago', 'Joana','Alberto'}.
    o grupo das pessoas que sabem excel é representado pelo set {'Alberto','Pedro','Joana','Tiago'}.
    o grupo das pessoas que NÃO sabem Power BI é representado pelo set {'Maria', 'Pedro', 'Alberto'}.
    Passarão para a próxima fase apenas as pessoas que possuem CNH e sabem Excel e Power BI.
    Use seus conhecimentos em sets para printar a lista das pessoas que passaram para a próxima fase.    
'''

possuem_CNH = {'Maria', 'João', 'Pedro', 'Tiago', 'Joana', 'Alberto'}
sabem_excel = {'Alberto', 'Pedro', 'Joana', 'Tiago'}
nao_sabem_power_bi = {'Maria', 'Pedro', 'Alberto'}

passaram_proxima_fase = possuem_CNH & sabem_excel - nao_sabem_power_bi
passaram_proxima_fase2 = possuem_CNH.intersection(sabem_excel).difference(nao_sabem_power_bi)
print(passaram_proxima_fase)
print(passaram_proxima_fase2)