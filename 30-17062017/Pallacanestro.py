from Squadra import Squadra

class Pallacanestro(Squadra):
    def __init__(self, codice, sport, nome_squadra, vittorie, sconfitte, media_falli, punti_totali):
        super(Pallacanestro, self).__init__(codice, sport, nome_squadra)
        self._vittorie = vittorie
        self._sconfitte = sconfitte
        self._media_falli = media_falli
        self._punti_totali = punti_totali

    def __str__(self):
        return super(Pallacanestro, self).__str__() + " " + str(self._vittorie) + " " + str(self._vittorie) + \
            str(self._punti_totali) +  " " + str(self._media_falli) + " " + super(Pallacanestro, self).get_sport()
