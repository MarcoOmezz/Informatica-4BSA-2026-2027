class Veicolo:
    def __init__(self, marca: str, modello: str):
        self.marca = marca
        self.modello = modello

    def descrizione(self):
        print(f"Marca: {self.marca}; Modello: {self.modello}")

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, Nporte: int):
        super().__init__(marca, modello)
        self.Nporte = Nporte

    def descrizione(self):
        super().descrizione()
        print(f"Numero di porte: {self.Nporte}")

    def Ritorna_stringa(self):
        return f"Auto-{self.marca}-{self.modello}-{self.Nporte}"



class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, tipo: str):
            super().__init__(marca, modello)
            self.tipo = tipo


    def descrizione(self):
        super().descrizione()
        print(f"Tipo: {self.tipo}")

    def Ritorna_stringa(self):
        return f"Moto-{self.marca}-{self.modello}-{self.tipo}"



def main():
    auto1 = Auto("Lamborghini", "Aventador", 2)
    auto2 = Auto("Dacia", "Sandero", 4)
    auto3 = Auto("Ferrari", "F40", 2)

    lista_auto = []
    lista_veicoli = []

    lista_auto.append(auto1)
    lista_auto.append(auto2)
    lista_auto.append(auto3)

    with open("M.txt", "w") as file:
        if len(lista_auto) >= 2:
            for e in lista_auto:
                    file.write(e.Ritorna_stringa() + "\n")

        else:
            pass





    with open ("M.txt", "r") as file:
        contenuto = file.read()
        righe = contenuto.split("\n")
        for riga in righe:
            if riga.strip():
                parola = riga.split("-")
                tipoClasse = parola[0]
                marca = parola[1]
                modello = parola[2]
                possibilità = parola[3]

                if tipoClasse == "Auto":
                    car = Auto(marca, modello, int(possibilità))
                    lista_veicoli.append(car)
                elif tipoClasse == "Moto":
                    motocicletta = Moto(marca, modello, possibilità)
                    lista_veicoli.append(motocicletta)

    print("Veicoli che sono stati inizialmente caricati: ")
    for veicolo in lista_veicoli:
        veicolo.descrizione()
        print("-" * 20)


    i = 0
    

    while(i!=1):
        vedi_classe = input("Inserisci la classe (Auto o Moto), mostra per vedere la lista, togli per togliere o esci per uscire: ")
        vedi_classe = vedi_classe.lower().strip()
        if vedi_classe == "auto":
            marca = input("Inserisci la marca dell'auto: ")
            modello = input("Inserisci il modello dell'auto: ")
            Nporte = int(input("Inserisci il numero di porte: "))

            car = Auto(marca, modello, Nporte)
            lista_veicoli.append(car)

        elif vedi_classe == "moto":
            marca = input("Inserisci la marca della moto: ")
            modello = input("Inserisci il modello della moto: ")
            tipo = input("Inserisci il tipo di moto: ")
            

            motocicletta = Moto(marca, modello, tipo)
            lista_veicoli.append(motocicletta)

        elif vedi_classe == "mostra":
            for veicolo in lista_veicoli:
                veicolo.descrizione()
                print("-" * 20)

        elif vedi_classe == "esci":
            i = 1

        elif vedi_classe == "togli":
            da_togliere = input("Inserisci il modello da rimuovere: ").strip()
            trovato = False
            for veicolo in lista_veicoli:
                if veicolo.modello.lower() == da_togliere.lower(): 
                    lista_veicoli.remove(veicolo)
                    print(f"Veicolo {veicolo.modello} rimosso con successo!")
                    trovato = True

            if not trovato:
                print("Veicolo non trovato!")

                



    with open ("Nuovo.txt", "w") as file:
        for e in lista_veicoli:
            file.write (e.Ritorna_stringa() + "\n")




if __name__ == "__main__": 
    main()