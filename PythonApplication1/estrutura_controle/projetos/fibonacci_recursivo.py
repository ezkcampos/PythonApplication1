def fibonacci(quantidade, sequencia=(0,1)):
    #importante: condição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    #listar os 20 primeiros valores da sequencia de fibonacci
    for fib in fibonacci(20):
        print(fib)


