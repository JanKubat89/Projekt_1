# Hlavicka projektu
# -----------------
#TODO   Vytvorit hlavicku
"""
Projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Kubát
email: hanys.jan.kubat@gmail.com
discord: jankubat_13826
"""

# Vyzvani uzivatel k zadani uzivatelskeho jmena a hesla
# -----------------------------------------------------
#TODO   Vyzadani si od uzivatele prihlasovaci jmeno a heslo

username = input('Username: ')
password = input('Password: ')

# Registrovani uzivatele
# ----------------------
#TODO   Vytvorit promennou 'registered_users' jako dictationary

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

registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Zadane texty
# ------------

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

# Kontrola uzivatele a jeho hesla
# -------------------------------
#TODO   Zjistit, jestli zadane udaje odpovidaji nekomu z registrovanych
#       uzivatelu
#TODO   Pokud je registrovany, pozdrav jej a umozni mu analyzovat texty
#TODO   Pokud neni registrovany, upozorni jej a ukonci program

if username in registered_users.keys():
    if password in registered_users[username]:
        print(
'''----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------'''
        )
    else:
        print('Unregistered user, terminating the program..')
        exit()
else:
    print('Unregistered user, terminating the program..')
    exit()

# Uzivatelska volba zadani cisla textu
# ------------------------------------
 
#TODO   Pokud uzivatel vybere takové cislo textu, ktere neni v zadani,
#       program jej upozorni a skonci,
#TODO   Pokud uzivatel zada jiny vstup nez cislo, program jej rovnez
#       upozorni a skonci

text_selection_value = input('Enter a number btw. 1 and 3 to select: ')
print('----------------------------------------')

# Osetreni, ze zadany znak je cokoli jineho nez cislo a ukonceni programu
if not text_selection_value.isdigit():
    print('You have not entered a number')
    print('Terminating the program..')
    exit()

# Osetreni, ze zadany znak je mimo interval <1, 3> a ukonceni programu
elif int(text_selection_value) not in range(1, 4):  
    print('You have not entered numbers between 1 to 3')
    print('Terminating the program..')
    exit()

# Cyklus pro ocisteni textu
# -------------------------
# Metoda '.split()' bez deliciho parametru deli slova automaticky podle
# mezery
# Pomoci metody '.append()' pridavam do promenne 'text_cleaned' retezce
# znaku orezane pomoci metody '.strip()' o interpunkci ve vetach ',.:;'

text_selected = TEXTS[int(text_selection_value) - 1]
text_cleaned = list()

for word in text_selected.split():
    text_cleaned.append(
        word.strip(",.:;")
    )

# Cyklus pro vypocet statistik z textu
# ------------------------------------
    
#TODO   Pocet slov
#TODO   pocet slov zacinajicich velkym pismenem
#TODO   Pocet slov psanych velkymi pismeny
#TODO   Pocet slov psanych malymi pismeny
#TODO   Pocet cisel (ne cifer)
#TODO   Sumu vsech cisel (ne cifer) v textu

title_words = 0
upper_words = 0
lower_words = 0
digit_words = 0
digit_sum = 0

# Pouzivam funkci 'enumerate()' pro zaindexovani jednotlivych slov pro
# jednodussi vypocet poctu slov

for index, word in enumerate(text_cleaned):

    # Priradi hodnotu indexu slova do promenne 'words_sum' a pricte 1,
    # protoze indexy zacinaji na indexu 0

    words_sum = index + 1 

    # Zkontroluje, jestli slovo zacina velkym pismenem pomoci metody
    # '.istitle()'

    if word.istitle():      
        title_words += 1
    
    # Zkontroluje, jestli kazdy znak ve slove je velke pismeno pomoci
    # metody '.isupper()'

    elif word.isupper():    
        upper_words += 1

    # Zkontroluje, jestli kazdy znak ve slove je male pismeno pomoci
    # metody '.islower()' 
           
    elif word.islower():    
        lower_words += 1

    # Zkontroluje, jestli je retezec znaku pouze cislo pomoci metody
    # '.isdigit()'
    elif word.isdigit():    
        digit_words += 1
        digit_sum += int(word)  # Pricte cislo do promenne 'digit_sum'
    
print(f'There are {words_sum} words in the selected text.')
print(f'There are {title_words} titlecase words.')
print(f'There are {upper_words} uppercase words.')
print(f'There are {lower_words} lowercase words.')
print(f'There are {digit_words} numeric strings.')
print(f'The sum of all the numbers is {digit_sum}.')

# Graficke zobrazeni cetnosti vsech stejne dlouhych slov
# ------------------------------------------------------
#TODO   Vytvorit jednoduchý sloupcovy graf, ktery bude reprezentovat
#       cetnost ruznych delek slov v textu

# Pomoci cyklu program ulozi jednotlive delky vsech slov do promenne
# 'word_length' jako klice a ke kazdemu klici priradi cetnost vyskytu

word_length = dict()

for word_in_text in text_cleaned:
    if len(word_in_text) not in word_length:
        word_length[len(word_in_text)] = 1
    else:
        word_length[len(word_in_text)] += 1

# Zabezpeceni, ze text 'OCCURENCES' bude vzdy uprostred mezi znaky '|'
# podle maximalniho poctu vyskytu slov 
        
print(f'''----------------------------------------
LEN|{
    int((max(word_length.values()) + 2 - 10) / 2) * ' '
    }OCCURENCES{
        int((max(word_length.values()) + 2 - 10) / 2) * ' '
        }|NR.
----------------------------------------'''
)

# Vykresleni jednoducheho grafu, ktery zaroven overuje lichost a sudost
# maximalniho poctu vyskytu slov a na zaklade vysledku zvoli vykresleni
if int(max(word_length.values())) % 2 != 0:
    for key, value in sorted(word_length.items()):
        if key <= 9 and value <= 9:
            print(f"  {key}|{value*'*'}{
                (max(word_length.values()) - value) * ' '
                } | {value}")
        elif key <= 9 and value > 9:
            print(f"  {key}|{value*'*'}{
                (max(word_length.values()) - value) * ' '
                } |{value}")
        elif key > 9 and value > 9:
            print(f" {key}|{value*'*'}{
                (max(word_length.values()) - value) * ' '
                } |{value}")
        else:
            print(f" {key}|{value*'*'}{
                (max(word_length.values()) - value) * ' '
                } | {value}")
else:
    for key, value in sorted(word_length.items()):
        if key <= 9 and value <= 9:
            print(f"  {key}|{value*'*'}{
                (max(word_length.values()) - value) * ' '
                }  | {value}")    
        elif key <= 9 and value > 9:
            print(f"  {key}|{value*'*'}{
                (max(word_length.values()) - value) * ' '
                }  |{value}")
        elif key > 9 and value > 9:
            print(f" {key}|{value*'*'}{
                (max(word_length.values()) - value) * ' '
                }  |{value}")
        else:
            print(f" {key}|{value*'*'}{
                (max(word_length.values()) - value) * ' '
                }  | {value}")