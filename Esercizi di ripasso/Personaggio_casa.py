import random

class Personaggio:
    def __init__(self, nome:str, pv:int, difesa:int, livello:int):
        self.nome = nome
        self.pv = pv
        self.difesa = difesa
        self.livello = livello
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


def main():
    p = Personaggio("Mario", 10, 4, 1)
    p.stampaStato()

if __name__=="__main__":
    main()
