# 1) Escreva uma função que calcule o valor médio de uma lista de números.


# Função para calcular a média da lista
def calc_media(lista):
    if len(lista) == 0: # len -> tamanho da lista
        return None     # None -> Sem valor significativo
    total = sum(lista)  # sum -> Soma os valores da lista
    media = total / len(lista)
    return media


numeros = [10, 15, 20, 25, 30]
media = calc_media(numeros)


print(f"A média dos números é: {media}")
