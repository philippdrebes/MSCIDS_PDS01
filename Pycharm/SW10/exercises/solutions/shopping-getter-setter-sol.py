#!/usr/bin/env python3
# coding=utf-8
# 2019-11, Bruno Grossniklaus, https://github.com/it-gro

# aus
#   Programmieren trainieren
#     Luigi Lo Iacono, Stephan Wiefling, Michael Schneider
#     Mit über 120 Workouts in Java und Python
#     https://www.hanser-fachbuch.de/buch/Programmieren+trainieren/9783446454866

# http://www.plantuml.com/plantuml/png/XPBDJkim48NtUOfPfgfprRj2LAKgq3T0OeEGvJf3Q-7QbJq1LS2xaybFf96eklHnvZjVCjbaCecQeo-iDpd3VI9dFS9N0HMO_g13SznXWYMuGBZ7n7Udv2osqPkFXWgOmsfb4nh2zNg4b79UzJCpVdYFfBjJEPiOFyNWy13ZEmlCuSCGtC7Yt-Acqsde45aZKt9Xpn4vyYYICnfXAiIO_BUL6kYgHwgESrrr-xoLflzlMIAOexIgcsJ8nI2_eOrDe7JMDjPuoPahBYbpZPhOIl2kkpyTukdK-Zssz7xVrYHwUONbkC0iLSH4sHMOkjOKDG-EabsU3_5JxvptvOmB1nv0LKL1cMvMtrN5hoe3tbUnmL3p3_eB

# ############################################################
# Öffentliche Klasse zur Repräsentation eines Artikels
# ############################################################
class Article(object):

    # Konstruktor, der die Artikelnummer und den Preis
    # erforderlich macht
    def __init__(self, article_number, price):
        self.__article_number = article_number
        self.__price = price

    # Getter-Methode, die den Preis zurückliefert
    def get_price(self):
        return self.__price


# ############################################################
# Öffentliche Klasse, die ein Buch repräsentiert
# Die Klasse erbt von der Klasse Artikel.
# ############################################################
class Book(Article):

    # Der Mehrwertsteuersatz für Bücher (7 %) wird durch die
    # statische Konstante VAT repräsentiert.
    vat = 0.07

    # Öffentlicher Konstruktor mit der Vorschrift
    # zum Anlegen eines Buchobjekts
    def __init__(self, article_number, price, author, title, year):
        # Aufruf des Konstruktors der Basisklasse Article
        Article.__init__(self, article_number, price)
        # super().__init__(article_number, price)

        # Zusätzlich werden die charakterisierenden
        # Eigenschaften eines Buchs gesetzt.
        self.__author = author
        self.__title = title
        self.__year = year

    # Öffentliche Methode zur Berechnung des Bruttopreises
    def get_price(self):
        # Rufe für Nettopreis die Methode in der Superklasse auf
        # und addiere die für Bücher geltende Mehrwertsteuer.
        price = super().get_price()
        price += super().get_price() * Book.vat
        # price += super().get_price() * self.vat
        return price

    # Öffentliche Methode, die einen geeigneten String generiert
    # und zurückliefert
    def __str__(self):
        output = "Buch - " + self.__author + ": "
        output += self.__title + " (" + str(self.__year) + ")"
        return output


# ############################################################
# Klasse, die eine DVD repräsentiert und von der Klasse
# Article ableitet
# ############################################################
class DVD(Article):

    # Statische Konstante für Mehrwertsteuersatz für DVDs (19 %)
    vat = 0.19

    # Öffentlicher Konstruktor der Klasse DVD. Zum Generieren eines
    # Objekts der Klasse DVD werden die angegebenen Werte verlangt.
    def __init__(self, article_number, price, name, duration, country_code):
        # Aufruf des Basisklassenkonstruktors
        Article.__init__(self, article_number, price)
        # self.__init__(article_number, price)

        # Zusätzliche Daten werden in den internen Variablen abgelegt.
        self.__name = name
        self.__duration = duration
        self.country_code = country_code

    # Öffentliche Methode zur Berechnung des Bruttopreises
    def get_price(self):
        # Rufe für Nettopreis die Methode in der Superklasse auf
        # und addiere die für Bücher geltende Mehrwertsteuer.
        price = super().get_price()
        price += super().get_price() * DVD.vat
        # price += super().get_price() * self.vat
        return price

    # Öffentliche Methode, die einen DVD-repräsentativen String
    # zurückliefert
    def __str__(self):
        return "DVD - " + self.__name


# ############################################################
# Klasse, die einen Warenkorb realisiert
# ############################################################
class ShoppingCart:

    # Öffentlicher Konstruktor, der den internen
    # Warenkorb initialisiert.
    def __init__(self):
        # Noch leerer Warenkorb
        self.__cart = []

    # Öffentliche Methode zum Hinzufügen eines Artikels
    # zum Warenkorb. Der Artikel wird in Form eines
    # Article-Objekts realisiert. Da sowohl Bücher als
    # auch DVDs von der Klasse Article erben, sind beide
    # Typen hier erlaubt und werden dafür auf die Basis-
    # Implementierung "zurückgecastet".
    def add_to_cart(self, article):
        self.__cart.append(article)

    # Öffentliche Methode, die eine Rechnung auf der
    # Konsole druckt
    def show_bill(self):
                                    # Ausrichten der Tabelle
        FORMAT_TEXT_WIDTH = 50      # Breite des Artikels als String
        FORMAT_PRICE_WIDTH = 7      # Breite des Preises
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
                  f"%{FORMAT_PRICE_WIDTH}.{FORMAT_PRICE_PRECISION}f" % article.get_price(), "%s" % "Euro")

            # Addiere zu Gesamtpreis
            sum += article.get_price()

        print("-" * (FORMAT_TEXT_WIDTH + FORMAT_PRICE_WIDTH + FORMAT_PRICE_PRECISION))
        # Gebe Gesamtpreis aus
        print(f"Gesamtpreis: %{FORMAT_PRICE_WIDTH}.{FORMAT_PRICE_PRECISION}f %s" % (sum, "Euro"))


# ############################################################
# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
# ############################################################
def main():
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
