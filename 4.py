# 4) Escreva uma função que testa se um número "a" dado é primo. Deve retornar verdadeiro apenas se "a" for primo, e falso caso contrário. Exemplo de uso: if (x>0 and primo(x)):


# Função que verifica se o número é primo.
def primo(a):
    if a <= 1:
        return False
    if a <= 3:
        return True
    if a % 2 == 0:
        return False
    i = 3
    while i * i <= a:
        if a % i == 0:
            return False
        i += 2  # Pular para o próximo número ímpar
    return True



x = int(input("Digite um número inteiro positivo: "))


if x > 0 and primo(x):
    print(f"{x} é um número primo.")
else:
    print(f"{x} não é um número primo.")

