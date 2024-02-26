from utils.etappeClass import Etappe

class Dag :
    def __init__(self, date_isoformat, ukedag, bruker_variabler):
      self.total_temp = 0
      self.date_isoformat = str(date_isoformat)[0: 10]
      self.ukedag = ukedag
      self.count = 0
      self.total_regn = 0
      self.total_vind = 0
      self.bruker_variabler = bruker_variabler
      self.etapper = [
          Etappe(0, 8),
          Etappe(8, 12),
          Etappe(12, 18),
          Etappe(18, 24),
      ]

    def update_day(self, tid, temperatur, vind, regn):

        self.total_temp += temperatur
        self.count += 1
        self.total_vind += vind
        self.total_regn += regn

        for i in range(len(self.etapper)):
            if tid >= self.etapper[i].time_start and tid < self.etapper[i].time_end:
                self.etapper[i].update_etappe(temperatur, regn, vind)

