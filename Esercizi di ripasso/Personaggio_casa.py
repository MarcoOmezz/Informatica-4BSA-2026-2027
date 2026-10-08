import random

class Personaggio:
    def __init__(self, nome:str, pv:int, difesa:int, livello:int):
        self.nome = nome
        self.pv = pv
        self.difesa = difesa
        self.livello = livello
        self.inventario = []
    def attacca(self):
        #n = random.randint(1,10)
        #return n
        return random.randint(1,10)

    def subisciDanno(self, danno:int):
        if self.pv < danno:
            self.pv = 0
        else:
            self.pv -= danno

    def cura(self, valore:int):
        self.pv += valore

    def isVivo(self):
        if self.pv > 0:
            return True
        else:
            return False

    def stampaStato(self):
        print(f"{self.nome}, PV: {self.pv}, Dif: {self.difesa}, LV: {self.livello}")

    def stampaInventario(self):
        if len(self.inventario) > 0:
            for item in self.inventario:
                print(item)
        else:
            print("Inventario vuoto...")

    def stringa(self):
        return f"{self.nome};{self.pv};{self.difesa};{self.livello}"

class Mago(Personaggio):
    def __init__(self, nome:str, pv:int, difesa:int, livello:int, mana:int):
        super().__init__(nome, pv, difesa, livello)
        self.mana = mana

    def lancia_magia(self, consumo_mana):
        if self.mana >= consumo_mana:
            self.mana -= consumo_mana
            return random.randint(1,10)+consumo_mana
        else:
            print("Impossibile lanciare magia!")
            return #ritorna None

    


def main():
    p = Mago("Mario", 10, 4, 1, 10)
    p.inventario.append("Pozione di cura")
    p.stampaStato()
    danno = p.lancia_magia(3)
    if danno == None:
        pass
    else:
        pass

if __name__=="__main__":
    main()
