# Vamos definir uma classe

class cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("auau")

    def dormir(self):
        self.acordado = False
        print("ZzzZzzz...")

# Vamos definir um OBJETO - Vamos instanciar um objeto para utilizar a classe.


#                 nome    cor      dormindo ou não
cao_1 = cachorro("Bird", "Creme", False)
cao_2 = cachorro("Skye", "Branco e Creme")

cao_1.latir()
print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)
