def main():
    #apre un file e lo chiude in automatico quando finisce il corpo del width
    with open("testo.txt", 'w') as file:
        file.write("....")
        #QUANDO ARRIVO QUI, IL FILE SI CHIUDE DA SOLO
    
    #versione 2
    # file = open("test.txt", "w")
    # file.write("....")
    # file.close()

    with open("testo.txt", 'r') as f:
        contenuto = f.read()
        print(contenuto)

if __name__ == "__main__":
    main()