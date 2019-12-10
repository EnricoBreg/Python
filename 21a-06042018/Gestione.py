import sys
import argparse

from Ristorante import Ristorante
from Pub import Pub
from Osteria import Osteria
from Prodotto import Prodotto

class Gestione():
    def main(self):
        lista_ristoranti = []
        cod_rist = {}
        # lettura del file ristoranti.txt
        try:
            file = open("ristoranti.txt")
            line = file.readline().strip()
            while line != '':
                tok = line.split()
                codice, tipo = int(tok[0]), tok[1]
                nome_ristorante = file.readline().strip()
                if tipo == "pub":
                    tok = file.readline().strip().split()
                    n_dipendenti, n_tavolini = int(tok[0]), int(tok[1])
                    r = Pub(codice, tipo, nome_ristorante, n_dipendenti, n_tavolini)
                    lista_ristoranti.append(r)
                    cod_rist[codice] = r
                if tipo == "osteria":
                    tok = file.readline().strip().split()
                    n_posti_sedere, superficie, bagno_disabili = int(tok[0]), float(tok[1]), bool(tok[2])
                    r = Osteria(codice, tipo, nome_ristorante, n_posti_sedere, superficie, bagno_disabili)
                    lista_ristoranti.append(r)
                    cod_rist[codice] = r
                line = file.readline().strip()
            file.close()
        except IOError as err:
            print(err)

        # lettura del file menu.txt
        try:
            file = open("menu.txt")
            line = file.readline().strip()
            while line != '':
                codice = int(line)
                # ristorante con quel codice
                rist = cod_rist.get(codice)
                descr_prodotto = file.readline().strip()
                tok = file.readline().strip().split()
                tipo, prezzo, costo_materie = tok[0], float(tok[1]), float(tok[2])
                prod = Prodotto(descr_prodotto, tipo, prezzo, costo_materie)
                rist.add_prodotto(prod)
                line = file.readline()
                line = file.readline().strip()

        except IOError as err:
            print(err)

        # stampa lista ristoranti
        print("nome, codice, tipo, n. dipendenti, n. tavoli, n. posti, superficie, bagno disabili")
        for rist in lista_ristoranti:
            print(rist)

        # stampa dei menu
        print("\n")
        for rist in lista_ristoranti:
            nome_ristorante, menu = rist.get_nome(), rist.menu_to_string()
            print(nome_ristorante + "\n\t" + menu)

        for rist in lista_ristoranti:
            max = 0.0
            if rist.get_prezzo_medio() > max:
                max = rist.get_prezzo_medio()
                rist_piu_caro = rist.get_nome()

        print("\n Il ristorante più caro e': " + rist_piu_caro)


if __name__ == '__main__':
    g = Gestione()
    g.main()

