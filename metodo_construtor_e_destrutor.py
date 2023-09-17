# Exemplo de Método Construtor.

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a Instância da Classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Exemplo de Aplicabilidade de método destrutor
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("Auau")


def criar_cachorro():
    c = Cachorro("Bird", "Particolor", False)
    print(c.nome)


criar_cachorro()

c = Cachorro("Skye", "Branco")
c.falar()

print("Olá Mundo!")

del c

print("Olá Mundo!")
print("Olá Mundo!")
print("Olá Mundo!")
