# 3) Escreva uma função que receba um número  inteiro "a" e retorne uma lista com todos os divisores de "a". Exemplo: os divisores de 12 são 12,6,4,3,2 e 1.


# Função que retorna os divisores de um número.
def divisores(a):
    lista_divisores = []        # Cria um array para os divisores.
    for i in range(1, a + 1):   # Loop vai de 1 até a
        if a % i == 0:  
            lista_divisores.append(i) # Adiciona o número ao array lista_divisores.
    return lista_divisores


num = int(input("Digite um número inteiro: "))


lista_de_divisores = divisores(num)


print(f"Os divisores de {num} são: {lista_de_divisores}")
