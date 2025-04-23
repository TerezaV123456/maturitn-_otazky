import math

class Geometricky_utvar:
    def __init__(self, nazev=None):
        self.nazev = nazev
        self.obvod = self.vypocti_obvod()
        self.obsah = self.vypocti_obsah()
        self.params = self.params()

    def vypocti_obvod(self):
        return None

    def vypocti_obsah(self):
        return None

    def params(self):
        return None


class Ctverec(Geometricky_utvar):
    def __init__(self, strana):
        self.strana = strana
        super().__init__('Ctverec')

    def vypocti_obvod(self):
        return 4 * self.strana

    def vypocti_obsah(self):
        return self.strana ** 2

    def params(self):
        return 'a = ' + str(self.strana)


class Obdelnik(Geometricky_utvar):
    def __init__(self, strana_a, strana_b):
        self.strana_a = strana_a
        self.strana_b = strana_b
        super().__init__('Obdelnik')

    def vypocti_obvod(self):
        return 2 * self.strana_a + 2 * self.strana_b

    def vypocti_obsah(self):
        return self.strana_a * self.strana_b

    def params(self):
        return 'a = ' + str(self.strana_a) + ', b = ' + str(self.strana_b)


class Kruh(Geometricky_utvar):
    def __init__(self, polomer):
        self.polomer = polomer
        super().__init__('Kruh')

    def vypocti_obvod(self):
        return 2 * math.pi * self.polomer

    def vypocti_obsah(self):
        return math.pi * (self.polomer ** 2)

    def params(self):
        return 'r = ' + str(self.polomer)


def main():
    utvary = [Ctverec(5), Kruh(4), Obdelnik(5,2)]
    for u in utvary:
        print(u.nazev, 's parametry', u.params, 'ma obvod', u.obvod, 'a obsah', u.obsah, '.')


if __name__ == '__main__':
    main()