class Segitiga():
    def __init__(self, title, alas, tinggi):
        self.title = title
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        luas = self.alas * self.tinggi / 2
        return '{}, luas={}'.format(self.title, luas)