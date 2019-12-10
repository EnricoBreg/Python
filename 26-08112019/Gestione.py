import sys
import argparse

from Regolare import Regolare
from Studente import Studente
from Conferenza import Conferenza
from Partecipazione import Partecipazione
from Partecipante import Partecipante

class Gestione():

    def main(self):
        lista_partecipanti = []
        lista_conferenze = []
        cod_part = {}
        # LETTURA DEL FILE partecipanti.txt
        try:
            f = open("partecipanti.txt")
            line = f.readline().strip()
            while line != '':
                tok = line.split()
                codice = int(tok[0])
                tipo = tok[1]
                nome = f.readline().strip()
                cognome = f.readline().strip()

                if tipo == "studente":
                    corso_studi = f.readline().strip()
                    universita = f.readline().strip()
                    anno_corso = int(f.readline().strip())
                    part = Studente(codice, tipo, nome, cognome, corso_studi, universita, anno_corso)
                    lista_partecipanti.append(part)
                    cod_part[codice] = part
                if tipo == "regolare":
                    ente = f.readline().strip()
                    line = f.readline().strip()
                    tok = line.split()
                    num_dip = int(tok[0])
                    accademico = bool(tok[1])
                    part = Regolare(codice, tipo, nome, cognome, ente, num_dip, accademico)
                    cod_part[codice] = part
                    lista_partecipanti.append(part)

                line = f.readline().strip()
            f.close()
        except IOError:
            raise IOError

        # LETTURA DEL FILE conferenze.txt
        try:
            f = open("conferenze.txt")
            line = f.readline().strip()

            while (line != '' and line != '\n'):
                nome_conferenza = line
                luogo_conferenza = f.readline().strip()
                line = f.readline().strip()
                c = Conferenza(nome_conferenza, luogo_conferenza)
                while (line != '\n'):
                    tok = line.split()
                    codice = int(tok[0])
                    spese_iscrizione = int(tok[1])
                    part = cod_part.get(codice)
                    partecipazione = Partecipazione(part, spese_iscrizione)
                    c.add_partecipazione(partecipazione)
                    line = f.readline()
                lista_conferenze.append(c)
                line = f.readline().strip()
        except IOError:
            raise IOError
        #PUNTO 3
        print("tipo, codice, nome, cognome, corso di studi, università, anno di corso, ente di appartenenza, "
              "numero di dipendenti, accademico")
        for p in lista_partecipanti:
            print(p)
        # PUNTO 4
        print("\n")
        for c in lista_conferenze:
            print(c.__str__())

        # PUNTO 5
        print("\n")
        try:
            codice = input("Inserire il codice\n>>> ")
            part = cod_part.get(int(codice))
            if part.get_tipo() == "studente":
                stud = part
                print(part.get_tipo() + ' ' + stud.get_uni())
            else:
                reg = part
                print(reg.get_tipo() + ' ' + reg.get_ente())
        except IOError as e:
            print(e)


if __name__ == "__main__":
    g = Gestione()
    g.main()
