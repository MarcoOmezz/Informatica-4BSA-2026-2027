class Veicolo:
    def __init__(self, marca:str, modello:str):
        self.marca = marca
        self.modello = modello

    def descrizione(self):
        print(f"Marca: {self.marca} - Modello: {self.modello}", end="")

class Auto(Veicolo):
    def __init__(self, marca:str, modello:str, nPorte:int):
        super().__init__(marca, modello)
        self.nPorte = nPorte

    def descrizione(self):
        super().descrizione()
        print(f" - N.Porte: {self.nPorte}")

class Moto(Veicolo):
    def __init__(self, marca:str, modello:str, tipo:str):
        super().__init__(marca, modello)
        self.tipo = tipo

    def descrizione(self):
        super().descrizione()
        print(f" - Tipo: {self.tipo}")

def main():
    a = Auto("Audi", "RS3", 5)
    m = Moto("Ducati", "Panigale", "Sportiva")

    a.descrizione()
    m.descrizione()

if __name__ == "__main__":
    main()