class Animale:
    def __init__(self, nome):
        self.nome = nome

    def verso(self):
        print("L'animale emette un verso")


class Cane(Animale):
    def __init__(self, nome, razza):
        super().__init__(nome)
        self.razza = razza

    def verso(self):
        print(self.nome, "dice: Bau!")


class Gatto(Animale):
    def verso(self):
        print(self.nome, "dice: Miao!")


# Creazione degli oggetti
cane1 = Cane("Fido", "Labrador")
gatto1 = Gatto("Micio")

cane1.verso()
gatto1.verso()

print(cane1.nome)
print(cane1.razza)