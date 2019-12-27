import sys
import argparse

from Ricerca import Ricerca
from Innovazione import Innovazione
from Ricercatore import Ricercatore

class Gestione():
    def __init__(self, args):
        self._args = args

    def main(self):
        lista_progetti = []
        lista_ricercatori = []
        cod_titolo = {}
        # LETTURA DEL FILE progetti.txt

        with open("progetti.txt") as file:

            string = file.readline().strip()
            while string != '':
                tok = string.split()
                codice, tipo = int(tok[0]), tok[1]
                titolo_progetto = file.readline().strip()
                coordinatore = file.readline().strip()
                organizzazione = file.readline().strip()
                cod_titolo[codice] = titolo_progetto
                line = file.readline().strip()
                if tipo == "ricerca":
                    tok = line.split()
                    cod_arg, num_partner = tok[0], int(tok[1])
                    importo_totale = float(file.readline().strip())
                    prog = Ricerca(codice, tipo, titolo_progetto, coordinatore, organizzazione, cod_arg, num_partner, importo_totale)
                    lista_progetti.append(prog)

                if tipo == "innovazione":
                    tok = line.split()
                    az_coinv, importo_totale = int(tok[0]), float(tok[1])
                    prog = Innovazione(codice, tipo, titolo_progetto, coordinatore, organizzazione, az_coinv, importo_totale)
                    lista_progetti.append(prog)
                string = file.readline().strip()

        # LETTURA DEL FILE ricercatori.txt
        with open("ricercatori.txt") as file:
            string = file.readline().strip()
            while string != '':
                nome = string
                string = file.readline().strip()
                cognome = string
                r = Ricercatore(nome, cognome)
                string = file.readline().strip()
                while string != '':
                    tok = string.strip().split()
                    codice, impegno_orario = int(tok[0]), float(tok[1])
                    titolo_progetto = cod_titolo.get(codice)
                    r.add_impegno(codice, titolo_progetto, impegno_orario)
                    string = file.readline().strip()
                lista_ricercatori.append(r)
                string = file.readline().strip()



        # stampa della lista progetti
        print("tipo, titolo, codice, coordinatore, organizzazione, argomento," +
                "partner, aziende, importo totale in migliaia di euro")
        for prog in lista_progetti:
            print(prog)
        print()

        for ric in lista_ricercatori:
            print(ric)

        print()
        for ric in lista_ricercatori:
            if ric.get_cognome() == self._args:
                print(ric.get_max_impegno())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cognome', action='store')
    cognome = parser.parse_args()
    g = Gestione(cognome.cognome)
    g.main()




