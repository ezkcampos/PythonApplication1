#carrega os dados do arquivo para o computador primeiro(mais lento)
arquivo =open('pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    #usando o split para formatar o registro em formato nome e idade
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))