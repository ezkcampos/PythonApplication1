#le o arquivo sob demanda(streaming)
arquivo =open('pessoas.csv')
for registro in arquivo:
    #usando o split para formatar o registro em formato nome e idade
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()
