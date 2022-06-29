#bloco with faz um melhor gerenciamento de leitura de arquivos
with open('pessoas.csv') as arquivo:
    #gera um arquivo txt, a letra w significa write
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)
    print('Arquivo criado com sucesso')
if arquivo.closed:
    print('Arquivo já foi fechado')
