import sys
import argparse

from Teoria import Teoria
from Laboratorio import Laboratorio
from Studente import Studente
from Voto import Voto

class Gestione():
    def __init__(self, arg):
        self._arg = arg

    def main(self):
        lista_corsi = []
        lista_studenti = []
        cod_corso = {}
        cod_studente = {}
        # LETTURA DEL FILE corsi.txt
        try:
            f = open("corsi.txt")
            line = f.readline().strip()
            while line != '':
                tok = line.split()
                codice = int(tok[0])
                tipo = tok[1]
                nome_corso = f.readline().strip()
                docente = f.readline().strip()
                cod_corso[codice] = nome_corso
                if tipo == "teoria":
                    line = f.readline().strip()
                    tok = line.split()
                    cod_aula = int(tok[0])
                    ore_settimanali = int(tok[1])
                    ore_lezione = float(tok[2])
                    c = Teoria(codice, tipo, nome_corso, docente, cod_aula, ore_settimanali, ore_lezione)
                    lista_corsi.append(c)
                if tipo == "laboratorio":
                    nome_laboratorio = f.readline().strip()
                    assistente = f.readline().strip()
                    postazioni = int(f.readline().strip())
                    c = Laboratorio(codice, tipo, nome_corso, docente, nome_laboratorio, assistente, postazioni)
                    lista_corsi.append(c)

                line = f.readline()
                line = f.readline().strip()
            f.close()
        except IOError as ex:
            print(ex)

        # LETTURA DEL FILE studenti.txt
        try:
            f = open("studenti.txt")
            line = f.readline().strip()
            while line != '':
                codice = int(line)
                nominativo_studente = f.readline().strip()
                s = Studente(codice, nominativo_studente)
                cod_studente[codice] = s
                line = f.readline()
                while line != '' and line != "\n":
                    tok = line.split()
                    codice_corso = int(tok[0])
                    valutazione = tok[1]
                    nome_corso = cod_corso.get(codice_corso)
                    s.add_voto(codice_corso, nome_corso, valutazione)
                    line = f.readline()
                lista_studenti.append(s)
                line = f.readline()
            f.close()
        except IOError as ex:
            print(ex)
        # PUNTO 3
        print("nome, codice, docente, tipo, aula, ore sett., ore/lez., lab., assistente, postazioni")
        for c in lista_corsi:
            print(c)
        # PUNTO 4
        print("\n")
        for s in lista_studenti:
            print(s)

        # PUNTO 5
        print("\n")
        studente = cod_studente.get(int(self._arg))
        libretto = []
        libretto = studente.get_libretto()
        max = 0
        for voto in libretto:
            if voto.get_voto() > max:
                max = voto.get_voto()
                corso = voto.get_corso()
        print(studente.get_nominativo() + " " + corso + " " + str(max))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('matricola')
    matr = parser.parse_args()
    g = Gestione(matr.matricola)
    g.main()
