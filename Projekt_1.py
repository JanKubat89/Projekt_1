#TODO   Vytvorit hlavicku
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Kubát
email: hanys.jan.kubat@gmail.com
discord: jankubat_13826
"""

#TODO   Naimportovat zadane soubory
import task_template

#TODO   Vyzadani si od uzivatele prihlasovaci jmeno a heslo
username = input('username: ')
password = input('password: ')

#   Registrovani uzivatele

"""
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
"""
#TODO   Vytvorit promennou 'registered_users' jako dictationary
registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

if username in registered_users.items():
    print(username)

#for username_present in registered_users:
#    if 


#TODO   Zjistit, jestli zadane udaje odpovidaji nekomu z registrovanych uzivatelu

#TODO   Pokud je registrovany, pozdrav jej a umozni mu analyzovat texty

#TODO   Pokud neni registrovany, upozorni jej a ukonci program

#TODO   Vytvorit promennou 'TEXTS', ve ktere budou ulozene jednotlive texty

#TODO   Pokud uzivatel vybere takové cislo textu, ktere neni v zadani, program jej upozorni a skonci,

#TODO   Pokud uzivatel zada jiny vstup nez cislo, program jej rovnez upozorni a skonci

#   Pro vybraný text spočítá následující statistiky

#TODO   Pocet slov
#TODO   pocet slov zacinajicich velkym pismenem
#TODO   Pocet slov psanych velkymi pismeny
#TODO   Pocet slov psanych malymi pismeny
#TODO   Pocet cisel (ne cifer)
#TODO   Sumu vsech cisel (ne cifer) v textu

#TODO   Vytvorit jednoduchý sloupcovy graf, ktery bude reprezentovat cetnost ruznych delek slov v textu

