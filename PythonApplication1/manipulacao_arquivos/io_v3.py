#le o arquivo sob demanda(streaming)
arquivo =open('pessoas.csv')
for registro in arquivo:
    #usando o split para formatar o registro em formato nome e idade, usando split para remover os espaços e linhas em branco
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
