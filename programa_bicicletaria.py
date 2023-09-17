# Programa que registra vendas de bicicletas


# Criando uma classe com características
class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

# criando os comportamentos da classe
    def buzinar(self):
        print("Plim Plim...")

    def parar(self):
        print("Parando a biclicleta...")
        print("Bicicleta Parada")

    def correr(self):
        print("Vrummmm....")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Instanciando um Objeto e chamando métodos
b1 = bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()

# exibindo os atributos da classe:
print(b1.cor, b1.modelo, b1.ano, b1.valor)


b2 = bicicleta("verde", "monark", 2000, 189)

# b2.buzinar() = bicicleta.buzinar(b2)
b2.buzinar()
print(b2)
