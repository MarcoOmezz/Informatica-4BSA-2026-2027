class Animale:
    def verso(self):
        print("Verso generico")


class Cane(Animale):
    def verso(self):
        print("Bau!")


class Gatto(Animale):
    def verso(self):
        print("Miao!")


class Mucca(Animale):
    def verso(self):
        print("Muuu!")


animali = [Cane(), Gatto(), Mucca()]

for animale in animali:
    animale.verso()