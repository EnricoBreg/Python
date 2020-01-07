from Squadra import Squadra


class Pallamano(Squadra):
    def __init__(self, codice, sport, nome_squadra, n_vittorie, n_sconfitte, media_goal):
        super(Pallamano, self).__init__(codice, sport, nome_squadra)
        self._n_vittorie = n_vittorie
        self._n_sconfitte = n_sconfitte
        self._media_goal = media_goal

    def get_vittorie(self):
        return self._n_vittorie

    def __str__(self):
        return super(Pallamano, self).__str__() + " " + str(self._n_vittorie) + " " + str(self._n_sconfitte) + \
            str(self._media_goal) + "\t- " + super(Pallamano, self).get_sport()
