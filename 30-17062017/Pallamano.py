from Squadra import Squadra

class Pallamano(Squadra):
    def __init__(self, codice, sport, nome_squadra, vittorie, sconfitte, media_goal):
        super(Pallamano, self).__init__(codice, sport, nome_squadra)
        self._vittorie = vittorie
        self._sconfitte = sconfitte
        self._media_goal = media_goal

    def __str__(self):
        return super(Pallamano, self).__str__() + " " + str(self._vittorie) + " " + str(self._sconfitte) + "\t-\t- " + \
            str(self._media_goal) + " " + super(Pallamano, self).get_sport()
