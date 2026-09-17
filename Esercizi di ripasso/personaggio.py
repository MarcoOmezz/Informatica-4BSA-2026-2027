class Personaggio:
    def __init__(self, nome:str, vita:int, energia:int, monete: int):
        self.nome = nome
        self.__vita = vita
        self.energia = energia
        self.monete = monete

    def mostra_stato(self):
        print(f"Nome: {self.nome}, Vita: {self.__vita}, energia: {self.energia}, monete: {self.monete}")

    def subisci_danno(self, danno:int):
        if danno < self.__vita:
            self.__vita -= danno
        else:
            self.__vita = 0

    def cura(self, valore:int):
        self.__vita += valore

    def compra_pozione(self, prezzo:int):
        if self.monete >= prezzo:
            self.monete -= prezzo
            self.cura(20)
        else:
            print("Non hai abbastanza soldi!")
    
    def guadagna_monete(self, valore: int):
        self.monete += valore

    def usa_energia(self, numero:int):
        if self.energia >= numero:
            self.energia -= numero
        else:
            print("Non hai abbastanza energia!")