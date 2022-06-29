def fibonacci(limite):
    resultado = [0, 1]
    #usando lista no lugar de variaveis
    while resultado[-1] < limite:
        resultado.append(resultado[-1] + resultado[-2])
    return resultado

if __name__ == '__main__':
    #o laço for, para fazer uma repetição a partir de cada numero da lista
    for fib in fibonacci(1000):
        print(fib)
