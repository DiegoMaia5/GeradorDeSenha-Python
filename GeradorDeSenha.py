import random

print("BEM VINDO AO GERADOR DE SENHAS!!\n")

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,0123456789'

numero = input("Quantidade de senhas para gerar: ")
numero = int(numero)

tamanho = input("Quantos digitos será sua senha: ")
tamanho = int(tamanho)

print("\nAqui está a sua senha: ")

for pwd in range(numero):
    senha = ''
    for c in range(tamanho):
        senha += random.choice(caracteres)
    print(senha)
