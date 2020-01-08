import argparse
import sys

from Pub import Pub
from Osteria import Osteria
from Prodotto import Prodotto


class Gestione():
    _lista_ristoranti = []

    def trova_rist_caro(self):
        maxc = 0.0 # max costo
        nome_max = ''
        for r in self._lista_ristoranti:
            costo_medio_menu = r.get_costo_medio_menu()
            if costo_medio_menu >= maxc:
                maxc = costo_medio_menu
                nome_max = r.get_nome_ristorante()
        return nome_max

    def main(self):
        cod_rist = {}

        with open("ristoranti.txt") as file:
            line = file.readline().strip()
            while line != '':
                tok = line.split()
                codice = int(tok[0])
                tipo = tok[1]
                nome_ristorante = file.readline().strip()

                if tipo == "pub":
                    tok = file.readline().strip().split()
                    n_dipendenti = int(tok[0])
                    n_tavoli = int(tok[1])
                    p = Pub(codice, tipo, nome_ristorante, n_dipendenti, n_tavoli)
                    self._lista_ristoranti.append(p)
                    cod_rist[codice] = p
                elif tipo == "osteria":
                    tok = file.readline().strip().split()
                    n_posti_a_sedere = int(tok[0])
                    superficie = float(tok[1])
                    bagno_disabili = bool(tok[2])
                    o = Osteria(codice, tipo, nome_ristorante, n_posti_a_sedere, superficie, bagno_disabili)
                    self._lista_ristoranti.append(o)
                    cod_rist[codice] = o
                line = file.readline().strip()

        with open("menu.txt") as file:
            line = file.readline().strip()
            while line != '':
                codice = int(line)
                descrizione = file.readline().strip()
                tok = file.readline().strip().split()
                tipo = tok[0]
                prezzo = float(tok[1])
                costo_produzione = float(tok[2])
                p = Prodotto(descrizione, tipo, prezzo, costo_produzione)
                r = cod_rist.get(codice)
                r.add_prodotto(p)
                line = file.readline()
                line = file.readline().strip()

        # PUNTO 3
        print("nome, codice, tipo, n. dipendenti, n. tavoli, n. posti, superficie, bagno disabili")
        for r in self._lista_ristoranti:
            print(r)
        print("\n")
        # PUNTO 4
        for r in self._lista_ristoranti:
            print(r.stampa_menu())
        # PUNTO 5
        print("\n")
        nome_ristorante = self.trova_rist_caro()
        print("Il ristorante più caro è: " + nome_ristorante);


if __name__ == '__main__':
    g = Gestione()
    g.main()
