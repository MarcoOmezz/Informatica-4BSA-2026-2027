class Prodotto:
    def __init__(self, codice:str, nome:str, prezzo:str, qta:int):
        self.nome = nome
        self.prezzo = prezzo
        self.qta = qta

    def valore_magazzino(self):
        return self.prezzo*self.qta

    def descrivi(self):
        return f"{self.nome}, {self.prezzo}, {self.qta}"

class ProdottoElettronico(Prodotto):
    def __init__(self, codice:str, nome:str, prezzo:str, qta:int, mesiGaranzia: int):
        super().__init__(codice, nome, prezzo, qta)
        self.mesiGaranzia = mesiGaranzia

    def descrivi(self):
        return super().descrivi() + f" , {self.mesiGaranzia}"

class Abbigliamento(Prodotto):
    def __init__(self, codice:str, nome:str, prezzo:str, qta:int, taglia: str):
        super().__init__(codice, nome, prezzo, qta)
        self.taglia = taglia

    def descrivi(self):
        return super().descrivi() + f" , {self.taglia}"

def calcolaTotaleMagazzino(listaProdotti: list[Prodotto]):
    somma = 0
    for item in listaProdotti:
        somma += item.valore_magazzino()
    return somma

def main():
    listaProdotti = []

    with open("ereditarietà e polimorfismo\\lezione del 22-10-2026\\prodotti.txt", "r") as file:
        contenuto = file.read()
        righe = contenuto.split("\n")
        temp = None
        for riga in righe:
            elementi = riga.split(";")
            if riga[0] == "P":
                temp = Prodotto(elementi[1], elementi[2], float(elementi[3]), int(elementi[4]))
            elif riga[0] == "E":
                temp = ProdottoElettronico(elementi[1], elementi[2], float(elementi[3]), int(elementi[4]), int(elementi[5]))
            elif riga[0] == "A":
                temp = Abbigliamento(elementi[1], elementi[2], float(elementi[3]), int(elementi[4]), elementi[5])

            listaProdotti.append(temp)

    print(f"Valore magazzino: {calcolaTotaleMagazzino(listaProdotti)}")

    #creazione del dizionario contenente la lista di categorie e somma valore di magazzino
    categorie = {"Prodotto": 0, "ProdottoElettronico": 0, "Abbigliamento": 0}

    for prodotto in listaProdotti:
        if isinstance(prodotto, Prodotto):
            categorie["Prodotto"] += prodotto.valore_magazzino() #attenzione, prende tutte le istanze
        if isinstance(prodotto, ProdottoElettronico):
            categorie["ProdottoElettronico"] += prodotto.valore_magazzino()
        if isinstance(prodotto, Abbigliamento):
            categorie["Abbigliamento"] += prodotto.valore_magazzino()

    print(categorie)

    with open("ereditarietà e polimorfismo\\lezione del 22-10-2026\\scorte_base.txt", "w") as file:
        for prodotto in listaProdotti:
            if prodotto.qta < 20:
                file.write(prodotto.descrivi() + "\n")

if __name__=="__main__":
    main()