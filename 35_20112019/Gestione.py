import sys
import argparse

from Hockey import Hockey
from Pallamano import Pallamano
from Giocatore import Giocatore


class Gestione():
    def main(self):
        lista_squadre = []
        lista_giocatori = []
        codsquadra = {}
        with open("squadre.txt") as file:
            line = file.readline().strip()
            while line != '':
                tok = line.split()
                codice, sport = int(tok[0]), tok[1]
                nome_squadra = file.readline().strip()
                codsquadra[codice] = nome_squadra
                if sport == 'hockey':
                    tok = file.readline().strip().split()
                    n_vittorie, n_sconfitte, media_goal, media_falli = \
                        int(tok[0]), int(tok[1]), float(tok[2]), float(tok[3])

                    s = Hockey(codice, sport, nome_squadra, n_vittorie, n_sconfitte, media_goal, media_falli)
                    lista_squadre.append(s)
                elif sport == 'pallamano':
                    tok = file.readline().strip().split()
                    n_vittorie, n_sconfitte, media_goal =  int(tok[0]), int(tok[1]), float(tok[2])

                    s = Pallamano(codice, sport, nome_squadra, n_vittorie, n_sconfitte, media_goal)
                    lista_squadre.append(s)
                line = file.readline().strip()
                line = file.readline().strip()

        with open("giocatori.txt") as file:

            line = file.readline().strip()
            while line != '':
                codice_squadra = int(line)
                cognome = file.readline().strip()
                nome = file.readline().strip()
                tok = file.readline().strip().split()
                eta, numero_maglia, ruolo, titolare = int(tok[0]), int(tok[1]), tok[2], bool(tok[3])
                nome_squadra = codsquadra.get(codice_squadra)
                g = Giocatore(nome_squadra, cognome, nome, eta, numero_maglia, ruolo, titolare)
                lista_giocatori.append(g)
                line = file.readline().strip()

        # PUNTO 3
        print("nome della squadra, codice, n. partite vinte, n. partite perse,\
            n. medio di gol, n. medio di falli, n. medio di reti, sport")
        for s in lista_squadre:
            print(s)

        # PUNTO 4
        print("\nnome, cognome, età, numero di maglia, ruolo, titolare, nome squadra")
        for g in lista_giocatori:
            print(g)

        # PUNTO 5
        tot_vittorie_hockey = 0.0
        tot_vittorie_pallamano = 0.0
        count_hockey = 0
        count_pallamano = 0
        for s in lista_squadre:
            sport = s.get_sport()
            vittorie = s.get_vittorie()
            if sport == 'hockey':
                tot_vittorie_hockey += vittorie
                count_hockey += 1
            elif sport == 'pallamano':
                tot_vittorie_pallamano += vittorie
                count_pallamano += 1
        print("\n")
        print("La media delle vittorie per le squadre di pallamano è: "\
              + str(tot_vittorie_pallamano / float(count_pallamano)))
        print("La media delle vittorie per le squadre di hockey è: " + str(tot_vittorie_hockey / float(count_hockey)))


if __name__ == '__main__':
    g = Gestione()
    g.main()
