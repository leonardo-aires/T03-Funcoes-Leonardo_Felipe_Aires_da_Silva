# 2) Escreva uma função que receba dois números inteiros "a","b" e verifique se "a" é divisível por "b". Retornar verdadeiro caso sejam divisíveis, e falso em caso contrário. 


# Função que verifica se o número é divisível ou não.
def divisivel(a, b):
    if b == 0:
        return False
    return a % b == 0


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


if divisivel(num1, num2):
    print(f"{num1} é divisível por {num2}.")
else:
    print(f"{num1} não é divisível por {num2}.")


