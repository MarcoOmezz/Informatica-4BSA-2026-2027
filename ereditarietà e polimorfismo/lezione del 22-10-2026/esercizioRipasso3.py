class Libro:
    def __init__(self, titolo, autore, prezzo):
        self.titolo = titolo
        self.autore = autore
        self.prezzo = float(prezzo)

    def descrivi(self):
        return self.titolo + " - " + self.autore + " - " + str(self.prezzo) + " euro"


class LibroScolastico(Libro):
    def __init__(self, titolo, autore, prezzo, materia, anno_corso):
        super().__init__(titolo, autore, prezzo)
        self.materia = materia
        self.anno_corso = int(anno_corso)

    def descrivi(self):
        return super().descrivi() + " - " + self.materia + " - Anno: " + str(self.anno_corso)



def main():
  libri = []
  
  # Lettura del file
  file = open("libri.txt", "r")
  
  for riga in file:
      dati = riga.strip().split(";")
  
      if dati[0] == "L":
          l = Libro(dati[1], dati[2], dati[3])
          libri.append(l)
  
      elif dati[0] == "S":
          l = LibroScolastico(dati[1], dati[2], dati[3], dati[4], dati[5])
          libri.append(l)
  
  file.close()
  
  
  # 1. Stampa tutti i libri
  print("ELENCO LIBRI")
  
  for l in libri:
      print(l.descrivi())
  
  
  # 2. Prezzo medio
  somma = 0
  contatore = 0
  
  for l in libri:
      if isinstance(l, LibroScolastico):
          somma = somma + l.prezzo
          contatore = contatore + 1
  
  if contatore > 0:
      media = somma / contatore
      print("Prezzo medio libri scolastici:", media)
  
  
  # 3. Salva i libri del terzo anno
  file = open("libri_terza.txt", "w")
  
  for l in libri:
      if isinstance(l, LibroScolastico):
          if l.anno_corso == 3:
              file.write(l.descrivi() + "\n")
  
  file.close()
  
  
  # 4. Conta i libri con prezzo superiore a 20 euro
  contatore = 0
  
  for l in libri:
      if l.prezzo > 20:
          contatore = contatore + 1
  print("Libri con prezzo superiore a 20 euro:", contatore)

if __name__=="__main__":
  main()
