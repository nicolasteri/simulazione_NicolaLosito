
class Catalogo():

    def __init__(self, nome, prezzomin, prezzomax):
        self.nome = nome
        self.prezzomin = prezzomin
        self.prezzomax = prezzomax
        self.lista = []

    def inserisci(self):
        lista.append(self)
        print("\nL'immobile è stato inserito con successo!\n")

class Immobili():
    
    def __init__(self, proprietario, indirizzo, prezzo, catalogo):
        self.proprietario = proprietario
        self.indirizzo = indirizzo
        self.prezzo = prezzo
        self.catalogo = catalogo

    def inserimento(self, lista):
        lista.append(self)
        print("\nL'immobile è stato inserito con successo!\n")


    def modifica(self):
        new_proprietario = str(input("Inserire nuovo Proprietario: "))
        if new_proprietario != "":
            self.proprietario = new_proprietario

        new_indirizzo = str(input("Inserire nuovo Indirizzo: "))
        if new_indirizzo != "":
            self.indirizzo = new_indirizzo

        new_prezzo = str(input("Inserire nuovo Prezzo: "))
        if new_prezzo != "":
            self.prezzo = new_prezzo


    def elimina(self, lista):
        lista.remove(self)
        print("L'immobile è stato rimosso con successo!\n")

    def stampa(self):
        print("Proprietario: %s \nIndirizzo: %s \nPrezzo: %s " % (self.proprietario, self.indirizzo, self.prezzo))


lista_immobili = []    
#creo Categorie
Di_Prestigio = Catalogo("di prestigio", "100000" "200000")
Popolare = Catalogo("popolare", "10000" "50000")
Vacanza = Catalogo("vacanza", "50000" "100000")
#creo Immobili
immobile1 = Immobili("nicola", "via uno", "100000", "Vacanza")
immobile2 = Immobili("pino", "via due", "50000", "Popolare")


RicIndirizzo = str(input("Quale indirizzo vuoi ricercare? "))
for im in lista_immobili:
    if im.indirizzo == RicIndirizzo:
        im.stampa()


immobile1.inserimento(lista_immobili)
immobile1.modifica()

for im in lista_immobili:
    im.stampa()

immobile1.elimina(lista_immobili)


for im in lista_immobili:
    im.stampa()