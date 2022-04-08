import sys
import string
from task_template import TEXTS

registrovani_uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

if __name__ == '__main__':
    print("Zadejte prosím uživatelské jméno:")
    zadane_jmeno=input()
    print("Zadejte prosím heslo:")
    heslo=input()

    print("-----------------------------------------------")
    if zadane_jmeno in registrovani_uzivatele.keys():
        print(f"Zadané jméno je spravné: {zadane_jmeno} je registrovaným uživatelem.")

        if heslo == registrovani_uzivatele[zadane_jmeno]:
            print(f"Zadané heslo je správné, Vitej {zadane_jmeno}.")
            print(f"Máme k analýze {len(TEXTS)} texty. Zadej číslo mezi 1 až {len(TEXTS)}:")
            try:
                cislo_textu = int(input())
            except:
                print("Očekáváme od Vás číselnou hodnotu v nabízeném rozmezí.")
                sys.exit(0)
                print("-----------------------------------------------")
            if cislo_textu <= len(TEXTS) and cislo_textu > 0:
                print(f"Vybral si text číslo {cislo_textu}.")
                zvoleny_text = TEXTS[cislo_textu - 1]
                print("-----------------------------------------------")
            else:
                print("Zadali jste špatné číslo textu.")
                sys.exit(0)
        else:
            print("Zadali jste špatné heslo.")
            sys.exit(0)
    else:
        print("Neznámý uživatel.")
        sys.exit(0)


    pocet_slov = 0
    pocet_slov_title = 0
    pocet_slov_capital = 0
    pocet_slov_lower = 0
    pocet_cisel = 0
    soucet_cisel = 0
    nejdelsi_slovo = 0

    upraveny_text = zvoleny_text.strip(string.punctuation)
    seznam_slov = upraveny_text.split()

    for slovo in seznam_slov:
        ciste_slovo = slovo.strip(string.punctuation)
        pocet_slov += 1

        if ciste_slovo.istitle():
            pocet_slov_title += 1
        if ciste_slovo.isupper():
            pocet_slov_capital += 1
        if ciste_slovo.islower():
            pocet_slov_lower += 1
        if ciste_slovo.isnumeric():
            pocet_cisel += 1
            hodnota_cisla = int(ciste_slovo)
            soucet_cisel = soucet_cisel + hodnota_cisla

        delka_slova = len(ciste_slovo)
        if delka_slova > nejdelsi_slovo:
            nejdelsi_slovo = delka_slova

    print(f"celkom slova: {pocet_slov}")
    print(f"title slova: {pocet_slov_title}")
    print(f"velka slova: {pocet_slov_capital}")
    print(f"lower slova: {pocet_slov_lower}")
    print(f"pocet cisel: {pocet_cisel}")
    print(f"sucet cisel: {soucet_cisel}")

    slova_ruznych_delek = {}
    pomocna_delka = 1

    while pomocna_delka <= nejdelsi_slovo:
        slova_ruznych_delek[pomocna_delka] = 0
        pomocna_delka += 1

    nejcetnejsi_delka = 0
    for slovo in seznam_slov:
        ciste_slovo = slovo.strip(string.punctuation)
        aktualni_delka = len(ciste_slovo)
        slova_ruznych_delek[aktualni_delka] = slova_ruznych_delek[aktualni_delka] + 1
        if slova_ruznych_delek[aktualni_delka] > nejcetnejsi_delka:
            nejcetnejsi_delka = slova_ruznych_delek[aktualni_delka]

    print("-----------------------------------------------")
    print("LEN|" + "{:^{width}}".format("OCCURENCES", width=(nejcetnejsi_delka + 2)) + "|NR.")
    print("-----------------------------------------------")
    pomocna_delka = 1
    while pomocna_delka <= nejdelsi_slovo:
        hvezdicky = '*' * slova_ruznych_delek[pomocna_delka]
        print("{0:3}|".format(pomocna_delka) + "{0:{width}}".format(hvezdicky, width=(nejcetnejsi_delka + 2)) + "|{}".format(slova_ruznych_delek[pomocna_delka]))
        pomocna_delka += 1
