class Persona:
    def __init__(self, nome:str, cognome:str, eta:int):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def descrivi(self):
        return f"{self.nome} {self.cognome}, {self.eta}"


class Studente(Persona):
    def __init__(self, nome:str, cognome:str, eta:int, classe:str, media:float):
        super().__init__(nome, cognome, eta)
        self.classe = classe
        self.media = media

    #override
    def descrivi(self):
        return super().descrivi() + f" Classe: {self.classe} - Media: {self.media}" 

def main():
    listaPersone = []
    with open("ereditarietà e polimorfismo\\lezione del 22-10-2026\\persone.txt", "r") as file:
        contenuto = file.read()
        righe = contenuto.split("\n")
        for riga in righe:
            elementi = riga.strip().split(";")
            temp = None
            if riga[0] == "P":
                temp = Persona(elementi[1], elementi[2], elementi[3])
            else:
                temp = Studente(elementi[1], elementi[2], elementi[3], elementi[4], float(elementi[5]))
            listaPersone.append(temp)

    for p in listaPersone:
        print(p.descrivi())

    #calcolo della media dei soli studenti
    somma = 0
    n = 0
    for p in listaPersone:
        if isinstance(p, Studente):
            somma += p.media
            n += 1

    media = somma/n
    print(f"{media:.2f}")

    #inserire in file studenti meritevoli
    with open("StudentiMeritevoli.txt", "w") as file:
        for studente in listaPersone:
            if isinstance(studente, Studente):
                if studente.media >= 8:
                    #scrivi su file
                    file.write(studente.descrivi()+"\n")


if __name__=="__main__":
    main()