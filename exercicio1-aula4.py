def somar_dois_valores(a, b):
    resultado = a + b

    if (resultado > 40):
        print('O valor é: ', resultado)
    else:
        print('Ops, só retorno valores acima de 40')
    
    return resultado

# variavel = chamada de funcao(argumento1, argumento2)

a_input = int(input('Digite o valor a: '))
b_input = int(input('Digite o valor b: '))

somar_dois_valores(a_input, b_input)