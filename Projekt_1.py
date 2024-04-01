#TODO   Vytvorit hlavicku
"""
Projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Kubát
email: hanys.jan.kubat@gmail.com
discord: jankubat_13826
"""

#TODO   Naimportovat zadane soubory

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

TEXTS = [
'''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.
''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#TODO   Zjistit, jestli zadane udaje odpovidaji nekomu z registrovanych uzivatelu
#TODO   Pokud je registrovany, pozdrav jej a umozni mu analyzovat texty
#TODO   Pokud neni registrovany, upozorni jej a ukonci program

if username in registered_users.keys():
    if password in registered_users[username]:
        print(
'''----------------------------------------
Welcome to the app, bob
e have 3 texts to be analyzed.
----------------------------------------'''
        )
    else:
        print('Unregistered user, terminating the program..')
        exit()
else:
    print('Unregistered user, terminating the program..')
    exit()

#TODO   Vytvorit promennou 'TEXTS', ve ktere budou ulozene jednotlive texty
#TODO   Pokud uzivatel vybere takové cislo textu, ktere neni v zadani, program jej upozorni a skonci,
#TODO   Pokud uzivatel zada jiny vstup nez cislo, program jej rovnez upozorni a skonci

text_selection_value = input('Enter a number btw. 1 and 3 to select: ')
print('----------------------------------------')

if not text_selection_value.isdigit():
    print('You have not entered a number')
    print('Terminating the program..')
    exit()
elif int(text_selection_value) not in range(1, 4):
    print('You have not entered numbers between 1 to 3')
    print('Terminating the program..')
    exit()

text_selected = TEXTS[int(text_selection_value) - 1]
text_cleaned = list()
title_words = 0
upper_words = 0
lower_words = 0
digit_words = 0
digit_sum = 0

# Cyklus pro ocisteni textu
# metoda '.split()' bez deliciho parametru deli slova automaticky podle mezery
# Pomoci metody '.append()' pridavam do promenne 'text_cleaned' retezce znaku
# orezane pomoci metody '.strip()' o interpunkci ve vetach ',.:;'
for word in text_selected.split():
    text_cleaned.append(
        word.strip(",.:;")
    )

# Cyklus pro praci s jednotlivymi slovy textu
# Pouzivam funkci 'enumerate()' pro zaindexovani jednotlivych slov pro jednodussi vypocet poctu slov

for index, word in enumerate(text_cleaned):
    words_sum = index + 1   # Priradi hodnotu indexu slova do promenne 'words_sum' a pricte 1
    if word.istitle():      # Zkontroluje, jestli slovo zacina velkym pismenem
        title_words += 1
    elif word.isupper():    # Zkontroluje, jestli je kazdy znak ve slove je velke pismeno
        upper_words += 1
    elif word.islower():    # Zkontroluje, jestli je kazdy znak ve slove je male pismeno
        lower_words += 1
    elif word.isdigit():    # Zkontroluje, jestli je slovo cislo, ale pouze cislo
        digit_words += 1
        digit_sum += int(word)
    
#TODO   Pocet slov
print(f'There are {words_sum} words in the selected text.')
print(f'There are {title_words} titlecase words.')
print(f'There are {upper_words} uppercase words.')
print(f'There are {lower_words} lowercase words.')
print(f'There are {digit_words} numeric strings.')
print(f'The sum of all the numbers is {digit_sum}.')

#   Pro vybraný text spočítá následující statistiky


#TODO   pocet slov zacinajicich velkym pismenem
#TODO   Pocet slov psanych velkymi pismeny
#TODO   Pocet slov psanych malymi pismeny
#TODO   Pocet cisel (ne cifer)
#TODO   Sumu vsech cisel (ne cifer) v textu

#TODO   Vytvorit jednoduchý sloupcovy graf, ktery bude reprezentovat cetnost ruznych delek slov v textu

