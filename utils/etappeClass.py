class Etappe:
    def __init__(self, time_start, time_end):
      self.time_start = time_start
      self.time_end = time_end
      self.temp = 0
      self.low = 9999
      self.high = -9999
      self.count = 0
      self.regn = 0
      self.vind = 0

    def high_low_check(self, temperatur):
        if temperatur < self.low:
            self.low = temperatur
        if temperatur > self.high:
            self.high = temperatur

    def update_etappe(self, temperatur, regn, vind):
        self.temp += temperatur
        self.regn += regn
        self.vind += vind
        self.count += 1

        self.high_low_check(temperatur)