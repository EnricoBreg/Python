import sys
import argparse

from Nutrizionista import Nutrizionista
from Trainer import Trainer
from Servizio import Servizio
from Cliente import Cliente


class Gestione():
    _lista_dipendenti = []
    _lista_clienti = []

    def ricerca_max(self):
        maxnum = 0
        nomemax = ''
        for cli in self._lista_clienti:
            num = cli.get_numero_servizi()
            if num >= maxnum:
                maxnum = num
                nomemax = cli.get_nome()
        return nomemax, maxnum

    def main(self):
        cod_dip = {}
        # Lettura del file dipendenti.txt
        with open("dipendenti.txt") as file:
            line = file.readline().strip()
            while line != '':
                tok = line.split()
                codice = int(tok[0])
                tipo = tok[1]
                nome = file.readline().strip()

                if tipo == 'trainer':
                    tok = file.readline().strip().split()
                    ore_settimana = int(tok[0])
                    costo_orario = float(tok[1])
                    specialita = file.readline().strip()
                    d = Trainer(codice, tipo, nome, ore_settimana, costo_orario, specialita)
                    self._lista_dipendenti.append(d)
                    cod_dip[codice] = d
                elif tipo == 'nutrizionista':
                    tok = file.readline().strip().split()
                    telefono = int(tok[0])
                    medico = bool(tok[1])
                    appuntamenti_settimanali = int(tok[2])
                    costo_orario = float(tok[3])
                    d = Nutrizionista(codice, tipo, nome, telefono, medico, appuntamenti_settimanali, costo_orario)
                    self._lista_dipendenti.append(d)
                    cod_dip[codice] = d
                line = file.readline().strip()

        # Lettura del file clienti.txt
        with open("clienti.txt") as file:
            line = file.readline().strip()
            while line != '':
                codice = int(line)
                nome_cliente = file.readline().strip()
                c = Cliente(codice, nome)
                line = file.readline().strip()
                # servizi utilizzati
                while line != '' and line != "\n":
                    tok = line.split()
                    codice_dip = int(tok[0])
                    ore_servizio = float(tok[1])
                    dip = cod_dip.get(codice_dip)
                    costo_orario = dip.get_costo()
                    s = Servizio(codice_dip, ore_servizio, costo_orario)
                    c.add_servizio(s)
                    line = file.readline().strip()
                self._lista_clienti.append(c)
                line = file.readline().strip()

        # PUNTO 3 - stampa lista dipendenti
        prompt = "nome, codice, tipo, ore settimanali, specialità, telefono, medico, app.sett., costo orario"
        print(prompt)
        for dip in self._lista_dipendenti:
            print(dip)
        print("\n")
        # PUNTO 4
        prompt = "codice, nome, costo totale servizi"
        print(prompt)
        for cli in self._lista_clienti:
            print(cli)
        print("\n")
        # PUNTO 5
        nome_cliente, num_servizi = self.ricerca_max()
        prompt = "Cliente con maggior servizi usufruiti\n" \
                 "Nome \t Numero servizi"
        print(nome_cliente + "\t" + str(num_servizi))


if __name__ == '__main__':
    g = Gestione()
    g.main()
