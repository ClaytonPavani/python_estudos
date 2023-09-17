# nesse exemplo vamos converter INTEIRO - FLOAT


preco = 10
print(preco)

preco = float(preco)
print(preco)

divisao = (preco / 2)
print(divisao)


# Como converter Float para Integer

preco = 10.30
print(preco)

preco = int(preco)
print(preco)


# como converter numéricos em strings


preco = 10.50
idade = 28

print(str(preco))
print(str(idade))

texto = f"idade é igual a {idade} e preço igual à {preco}"
print(texto)


# convertendo STRING PARA NUMÉRICO:


preco = "10.50"
idade = "28"

print(float(preco))
print(int(idade))

soma_idade = (int(idade) + 10)
print(soma_idade)


# Exemplos de Erro de Conversão
'''
preco = "python"
print(float(preco))
'''
# veja que não será possível fazer essa forma

# identificando um tipo:

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))
