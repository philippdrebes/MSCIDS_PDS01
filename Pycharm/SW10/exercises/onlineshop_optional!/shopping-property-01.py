#!/usr/bin/env python3
# coding=utf-8
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro

# aus
#   Programmieren trainieren
#     Luigi Lo Iacono, Stephan Wiefling, Michael Schneider
#     Mit über 120 Workouts in Java und Python
#     https://www.hanser-fachbuch.de/buch/Programmieren+trainieren/9783446454866


class Article():
    '''
    Öffentliche Klasse zur Repräsentation eines Artikels
    '''

    def __init__(self, article_number, price):
        '''
        Konstruktor, der die Artikelnummer und den Preis
        erforderlich macht
        '''
        self.__article_number = article_number
        self.price_net = price


class Book(Article):
    '''
    Öffentliche Klasse, die ein Buch repräsentiert
    Die Klasse erbt von der Klasse Artikel.
    '''

    # Der Mehrwertsteuersatz für Bücher (7 %) wird durch die
    # statische Konstante VAT repräsentiert.
    vat = 0.07

    def __init__(self, article_number, price, author, title, year):
        '''
        Öffentlicher Konstruktor mit der Vorschrift
        zum Anlegen eines Buchobjekts
        '''

        # Aufruf des Konstruktors der Basisklasse Article
        super().__init__(article_number, price)

        # Zusätzlich werden die charakterisierenden
        # Eigenschaften eines Buchs gesetzt.
        self.__author = author
        self.__title = title
        self.__year = year

    @property
    def price(self):
        '''
        Hole den Nettopreis aus der Superklasse und addiere die für Bücher
        geltende Mehrwertsteuer.
        '''

        return self.price_net * (1 + type(self).vat)

    @price.setter
    def price(self, price):
        '''
        Setze den Nettopreis in der Superklasse
        '''

        self.price_net = price

    def __str__(self):
        '''
        Öffentliche Methode, die einen geeigneten String generiert
        und zurückliefert
        '''

        output = "Buch - " + self.__author + ": "
        output += self.__title + " (" + str(self.__year) + ")"
        return output


class DVD(Article):
    '''
    Klasse, die eine DVD repräsentiert und von der Klasse
    Article ableitet
    '''

    # Statische Konstante für Mehrwertsteuersatz für DVDs (19 %)
    vat = 0.19

    def __init__(self, article_number, price, name, duration, country_code):
        '''
        Öffentlicher Konstruktor der Klasse DVD. Zum Generieren eines
        Objekts der Klasse DVD werden die angegebenen Werte verlangt.
        '''

        # Aufruf des Basisklassenkonstruktors
        super().__init__(article_number, price)

        # Zusätzliche Daten werden in den internen Variablen abgelegt.
        self.__name = name
        self.__duration = duration
        self.__country_code = country_code

    @property
    def price(self):
        '''
        Hole den Nettopreis aus der Superklasse und addiere die für Bücher
        geltende Mehrwertsteuer.
        '''

        return self.price_net * (1 + type(self).vat)

    @price.setter
    def price(self, price):
        '''
        Setze den Nettopreis in der Superklasse
        '''

        self.price_net = price

    def __str__(self):
        '''
        Öffentliche Methode, die einen DVD-repräsentativen String
        zurückliefert
        '''

        return f"DVD - {self.__name} {self.__duration}"


class ShoppingCart:
    '''
    Klasse, die einen Warenkorb realisiert
    '''

    def __init__(self):
        '''
        Öffentlicher Konstruktor, der den internen
        Warenkorb initialisiert.
        '''

        # Noch leerer Warenkorb
        self.__cart = []

    def add_to_cart(self, article):
        '''
        Öffentliche Methode zum Hinzufügen eines Artikels
        zum Warenkorb. Der Artikel wird in Form eines
        Article-Objekts realisiert. Da sowohl Bücher als
        auch DVDs von der Klasse Article erben, sind beide
        Typen hier erlaubt und werden dafür auf die Basis-
        Implementierung "zurückgecastet".
        '''

        self.__cart.append(article)

    def show_bill(self):
        '''
        Öffentliche Methode, die eine Rechnung auf der
        Konsole druckt
        '''

        # Ausrichten der Tabelle
        FORMAT_TEXT_WIDTH = 50  # Breite des Artikels als String
        FORMAT_PRICE_WIDTH = 7  # Breite des Preises
        FORMAT_PRICE_PRECISION = 2  # davon Anzahl Nachkommastellen

        # Gesamtpreis
        sum = 0.0

        # Jeden Artikel durchgehen
        for article in self.__cart:
            # Gebe Namen und Preis aus

            # https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
            # https://docs.python.org/3.7/library/string.html#formatspec
            # https://realpython.com/python-f-strings/
            print(f"%-{FORMAT_TEXT_WIDTH}s" % article,
                  f"%{FORMAT_PRICE_WIDTH}.{FORMAT_PRICE_PRECISION}f"
                  % article.price,
                  "%s" % "Euro")

            # Addiere zu Gesamtpreis
            sum += article.price

        print("-" * (FORMAT_TEXT_WIDTH + FORMAT_PRICE_WIDTH +
                     FORMAT_PRICE_PRECISION))
        # Gebe Gesamtpreis aus
        print(f"Gesamtpreis: %{FORMAT_PRICE_WIDTH}.{FORMAT_PRICE_PRECISION}f %s"
              % (sum, "Euro"))


def main():
    '''
    Startpunkt des Hauptprogramms
    Hier werden die implementierten Klassen zu Demonstrations- und
    Testzwecken instanziiert und verwendet.
    '''

    book = Book(122767676, 32.71, "Luigi Lo Iacono", "WebSockets", 2015)
    dvd1 = DVD(122767676, 14.95, "Spiel mir das Lied vom Tod", "99:12", 1)
    dvd2 = DVD(122767676, 8.40, "Casablanca, Classic Collection", "99:12", 1)

    wk = ShoppingCart()
    wk.add_to_cart(book)
    wk.add_to_cart(dvd1)
    wk.add_to_cart(dvd2)
    wk.show_bill()


if __name__ == "__main__":
    main()
