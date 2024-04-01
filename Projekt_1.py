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



    


#TODO   Zjistit, jestli zadane udaje odpovidaji nekomu z registrovanych uzivatelu
#TODO   Pokud je registrovany, pozdrav jej a umozni mu analyzovat texty
#TODO   Pokud neni registrovany, upozorni jej a ukonci program

if username in registered_users.keys():
    if password in registered_users[username]:
        print(
'''
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
'''
        )
    else:
        print('unregistered user, terminating the program..')
else:
    print('unregistered user, terminating the program..')


#TODO   Vytvorit promennou 'TEXTS', ve ktere budou ulozene jednotlive texty
#TODO   Pokud uzivatel vybere takové cislo textu, ktere neni v zadani, program jej upozorni a skonci,
#TODO   Pokud uzivatel zada jiny vstup nez cislo, program jej rovnez upozorni a skonci

selected_text = input('Enter a number btw. 1 and 3 to select: ')

if not selected_text.isdigit():
    print('You have not entered a number')
    print('Terminating the program..')
elif selected_text not in range(1, 4):
    print('You have not entered numbers between 1 to 3')
    print('Terminating the program..')
else:
    print(selected_text)



#   Pro vybraný text spočítá následující statistiky

#TODO   Pocet slov
#TODO   pocet slov zacinajicich velkym pismenem
#TODO   Pocet slov psanych velkymi pismeny
#TODO   Pocet slov psanych malymi pismeny
#TODO   Pocet cisel (ne cifer)
#TODO   Sumu vsech cisel (ne cifer) v textu

#TODO   Vytvorit jednoduchý sloupcovy graf, ktery bude reprezentovat cetnost ruznych delek slov v textu

