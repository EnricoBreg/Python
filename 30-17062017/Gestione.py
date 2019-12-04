import sys
import argparse

from Pallacanestro import Pallacanestro
from Pallamano import Pallamano
from Giocatore import Giocatore


class Gestione():

    def main(self):
        lista_squadre = []
        lista_giocatori = []
        cod_squadra = {} # codice-nome_squadra

        # lettura del squadre.txt
        try:

            f = open("squadre.txt")
            line = f.readline().strip()

            while line != '':
                tok = line.split()
                codice = int(tok[0])
                sport = tok[1]
                nome_squadra = f.readline().strip()

                if sport == "pallacanestro":
                    tok = f.readline().strip().split()
                    vittorie = int(tok[0])
                    sconfitte = int(tok[1])
                    media_falli = float(tok[2])
                    punti_totali = int(tok[3])
                    s = Pallacanestro(codice, sport, nome_squadra, vittorie, sconfitte, media_falli, punti_totali)
                    lista_squadre.append(s)
                    cod_squadra[codice] = s
                if sport == "pallamano":
                    tok = f.readline().strip().split()
                    vittorie = int(tok[0])
                    sconfitte = int(tok[1])
                    media_goal = float(tok[2])
                    s = Pallamano(codice, sport, nome_squadra, vittorie, sconfitte, media_goal)
                    lista_squadre.append(s)
                    cod_squadra[codice] = s
                line = f.readline()
                line = f.readline().strip()
            f.close()
        except IOError as e:
            print(e)

        # lettura del file giocatori.txt
        try:
            f = open("giocatori.txt")
            line = f.readline().strip()
            while line != '':
                codice = int(line)
                s = cod_squadra.get(codice) # return squadra
                nome_squadra = s.get_nome()
                cognome = f.readline().strip()
                nome = f.readline().strip()
                tok = f.readline().strip().split()
                titolare, eta, numero_maglia, ruolo = bool(tok[0]), int(tok[1]), int(tok[2]), tok[3]
                g = Giocatore(codice, nome_squadra, cognome, nome, titolare, eta, numero_maglia, ruolo)
                lista_giocatori.append(g)
                s.add_giocatore(g)
                line = f.readline().strip()
            f.close()
        except IOError as e:
            print(e)

        # punto 3
        print("nome della squadra, codice, n. partite vinte, n. partite perse, punti totali, n. medio di falli, n. medio di reti, sport")
        for squadra in lista_squadre:
            print(squadra)

        # DA FINIRE PUNTO 4 e PUNTO 5
        # punto 4
        print("\nnome, cognome, età, numero di maglia, ruolo, nome squadra")
        for giocatore in lista_giocatori:
            print(giocatore)
        print("\n")
        for squadra in lista_squadre:
            print(squadra.get_nome() + " " + squadra.get_num_giocatori())


if __name__ == '__main__':
    g = Gestione()
    g.main()

