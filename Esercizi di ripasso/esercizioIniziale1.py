'''
Realizza una classe Personaggio, con questi attributi:
- nome
- vita
- energia
- monete

Nel costruttore assegna i valori iniziali come parametri.

Crea poi i seguenti metodi:
- mostra_stato() -> stampa nome, vita, energia e monete
- subisci_danno(danno) -> diminuisce vita del valore indicato
    (attenzione la vita non può scendere sotto 0)
- cura(valore) -> aggiunge valore a vita
- usa_energia(numero) -> diminuisce l'energia, solo se ce n'è abbastanza
- guadagna_monete(numero) -> aumenta il numero di monete
- compra_pozione(prezzo) -> se il personaggio ha abbastanza monete
    sottrae il prezzo e aumenta la vita di 20

Nel main poi crea almeno un'istanza e richiama su di essa tutti
i metodi implementati.
'''
import personaggio
from personaggio import Personaggio


def main():
    p = Personaggio(nome="Mario", vita=100, energia=50, monete=10)
    p.mostra_stato()
    p.cura(10)
    p.subisci_danno(50)
    p.compra_pozione(5)
    p.mostra_stato()

if __name__ == "__main__": #esegui questa parte quando questo file è il programma principale
    main()