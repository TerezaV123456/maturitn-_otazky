#Důležité je, nehledat v tom složitosti. Objektovy programování je jen o tom, že v tvoříš objekt, kterým se říká Class = třída a ten má vlastnosti (parametry, properties) a metody (chování, functions)
#Z objektů můžeš dědit vlastnosti a metody do dalších objektů, to je dědičnost. Můžeš mít třídu zvíře a udělat z toho kočku a psa. Dědičnost zjednodušuje kód a redukuje práci 
#Zapouzdření znamená, že každý objekt si hlídá svoje properties a nic z venka by nemělo měnit jeho stav
#Polymorfismus nám říká, že můžeš při běhu připisovat metody a měnit tak chování objektu 


# Zapouzdření (encapsulation) - použití privátních atributů a getter/setter metod
class Zvire:
    def __init__(self, jmeno, vek):
        self.__jmeno = jmeno  # Privátní atribut
        self.__vek = vek      # Privátní atribut

    # Getter pro jmeno
    @property
    def jmeno(self):
        return self.__jmeno

    # Setter pro jmeno
    @jmeno.setter
    def jmeno(self, nove_jmeno):
        if isinstance(nove_jmeno, str) and nove_jmeno:
            self.__jmeno = nove_jmeno
        else:
            raise ValueError("Jméno musí být neprázdný řetězec")

    # Getter pro vek
    @property
    def vek(self):
        return self.__vek

    # Setter pro vek
    @vek.setter
    def vek(self, novy_vek):
        if isinstance(novy_vek, int) and novy_vek >= 0:
            self.__vek = novy_vek
        else:
            raise ValueError("Věk musí být nezáporné celé číslo")

    # Metoda pro vydání zvuku - bude přepsána v odvozených třídách (polymorfismus)
    def vydat_zvuk(self):
        return "Nějaký zvuk"

    # Obecná metoda pro popis zvířete
    def popis(self):
        return f"{self.__jmeno} je zvíře, které má {self.__vek} let."

# Dědičnost - třída Pes dědí od Zvire
class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno):
        super().__init__(jmeno, vek)  # Volání konstruktoru rodičovské třídy
        self.__plemeno = plemeno     # Dodatečný atribut

    # Polymorfismus - přepis metody vydat_zvuk
    def vydat_zvuk(self):
        return "Haf haf!"

    # Přepsání metody popis
    def popis(self):
        return f"{self.jmeno} je pes plemene {self.__plemeno}, má {self.vek} let."

# Dědičnost - třída Kočka dědí od Zvire
class Kocka(Zvire):
    def __init__(self, jmeno, vek, barva):
        super().__init__(jmeno, vek)
        self.__barva = barva

    # Polymorfismus - přepis metody vydat_zvuk
    def vydat_zvuk(self):
        return "Mňau!"

    # Přepsání metody popis
    def popis(self):
        return f"{self.jmeno} je kočka barvy {self.__barva}, má {self.vek} let."

# Ukázka použití
def main():
    # Vytvoření instancí
    pes = Pes("Rex", 5, "Německý ovčák")
    kocka = Kocka("Mourek", 3, "Černá")

    # Demonstruje zapouzdření
    print(pes.jmeno)  # Getter
    pes.jmeno = "Max"  # Setter
    print(pes.jmeno)

    try:
        pes.vek = -1  # Vyvolá výjimku
    except ValueError as e:
        print(f"Chyba: {e}")

    # Demonstruje polymorfismus a dědičnost
    zvirata = [pes, kocka]
    for zvire in zvirata:
        print(zvire.popis())        # Různé popisy podle třídy
        print(zvire.vydat_zvuk())   # Různé zvuky podle třídy

if __name__ == "__main__":
    main()