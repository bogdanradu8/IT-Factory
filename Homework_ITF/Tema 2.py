# TEME DIN CURS

# C02_EX01 (HOMEWORK): Modificati exercitiul de mai sus, astfel incat sa nu accepte stringuri de dimensiune para. Daca cumva primim
# un string de dimensiune para, sa se afiseze: "Ati introdus un string de dimensiune para!!"

while True:
    try:
        cuvant = input('Introduceti un cuvant cu un numar impar de litere: ')
        print(cuvant)

        if len(cuvant) % 2 == 0:
            raise ValueError

        break
    except ValueError:
        print('Ai introdus gresit! Incearca din nou: ')


# C02_EX02 (HOMEWORK): Given a string s1, append another string s2 in the middle of s1
# e.g.:  s1 = 'Legendary', s2 = 'wait'  => 'Legewaitndary'
#        s1 = 'mama', s2 = 'MIA'  =>  'maMIAma'

s1 = 'Fanstic'
s2 = 'ta'

rezultat = s1[:3] + s2 + s1[3:]
print(rezultat)

# TEMA 2

x = 3
y = 12
z = 8


# 1.Explicati cu propriile cuvinte, in cadrul unui comentariu, cum functioneaza un if else

    # if = executa comenzile dorite cand o conditie este adevarata.
    # else - executa anumite comenzi cand o conditie este adevarata si alte comenzi cand aceasta este falsa.

# 2. Verificati si afisati daca x este numar natural sau nu

if x == int(x):
    print(f'{x} este un numar natural')
else:
    print(f'{x} nu este un numar natural')

# 3. Verificati si afisati daca x este numar pozitiv, negativ sau neutru

if x == 0:
    print(f'{x} este neutru')
elif x < 0:
    print(f'{x} este negativ')
else:
    print(f'{x} este pozitiv')

# 4.  Verificati si afisati daca x este intre -2 si 13

if x >= -2 and x <= 13:
    print(f'{x} este intre -2 si 13')
else:
    print(f'{x} nu este intre -2 si 13')

# 5.  Verificati si afisati daca diferenta dintre x si y este mai mica de 5

if x - y < 5:
    print(f'Diferenta dintre {x} si {y} este mai mica de 5')
else:
    print(f'Diferenta dintre {x} si {y} este mai mare sau egala cu 5')

# 6.  Verificati daca x NU este intre 5 si 27. (a se folosi ‘not’)

if not(x >= 5 and x <= 27):
    print(f'{x} nu este intre 5 si 27')
else:
    print(f'{x} este intre 5 si 27')

# 7. x si y (int)
# Verificati si afisati daca sunt egale, daca nu afisati care din ele este mai mare

if x > y:
    print(f'{x} este mai mare ca {y}')
elif x == y:
    print(f'{x} este egal cu {y}')
else:
    print(f'{y} este mai mare ca {x}')

# 8.  X, y, z - laturile unui triunghi
# Afisati daca triunghiul este isoscel, echilateral sau oarecare.

if x == y == z:
    print('Triunghiul este echilateral')
elif x == y or x == z or y == z:
    print('triunghiul este isoscel')
else:
    print('Triunghiul este oarecare')

# 9.  Cititi o litera de la tastatura
# Verificati si afisati daca este vocala sau nu

litera = input('Introduceti o litera: ')

lista_vocale = ['a','e','i','o','u']

if litera in lista_vocale:
    print(f'{litera} este o vocala')
else:
    print(f'{litera} NU este o vocala')

# 10. Transformati si printati notele din sistem romanesc in  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = input('Introduceti nota obtinuta: ')
nota = float(nota)

if nota >= 9:
    print(f'Nota ta in sistemul american este: A')
elif nota >= 8:
    print(f'Nota ta in sistemul american este: B')
elif nota >= 7:
    print(f'Nota ta in sistemul american este: C')
elif nota >= 6:
    print(f'Nota ta in sistemul american este: D')
elif nota >= 4:
    print(f'Nota ta in sistemul american este: E')
elif nota < 4:
    print(f'Nota ta in sistemul american este: F')
else:
    print(f'Nu ai introdus corect')


# 11.Verificati daca x are minim 4 cifre (x e int)
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

a = 62 # voi defini x,y,z de la exercitiile optionale cu a,b,c.
b = 70
c = 50

if len(str(a)) >= 4:
    print(f'{a} are minim 4 cifre')
else:
    print(f'{a} nu are minim 4 cifre')

# 12. Verificati daca x are exact 6 cifre

if len(str(a)) == 6:
    print(f'{a} are exact 6 cifre')
else:
    print(f'{a} nu are 6 cifre')

# 13. Verificati daca x este numar par sau impar (x e int)

if a % 2 == 0:
    print(f'{a} este un numar par')
else:
    print(f'{a} este un numar impar')

# 14. x, y, z (int)
# Afisati care este cel mai mare dintre ele?

lista_numere = [a,b,c]
print(f'Cel mai mare numar dintre {a}, {b} si {c} este {max(lista_numere)}')

# 15.  X, y, z - reprezinta unghiurile unui triunghi
# Verificati si afisati daca triunghiul este valid sau nu

if a + b + c == 180:
    print('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')

# 16.  Avand stringul: 'Coral is either the stupidest animal or the smartest rock'.
# Cititi de la tastatura un int x.
# Afisati stringul fara ultimele x caractere.
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

string2 = 'Coral is either the stupidest animal or the smartest rock'
d = int(input('Introduceti un numar: '))  #notam cu d in loc de x

print(string2[0:-d])

# 17. Acelasi string.
# Declarati un string nou care sa fie format din primele 5 caractere + ultimele 5

new_string = string2[6:-6]
print(new_string)

# 18. Acelasi string.
# Salvati intr-o variabila si afiseaza indexul de start al cuvantului rock.
# (hint: este o functie care va ajuta sa faceti asta).
# Folosind aceasta variabila + slicing, afisati tot stringul pana la acest cuvant.
# output: 'Coral is either the stupidest animal or the smartest '

cuvant = string2.index('rock')
print(cuvant)
# lista_string = string2.split(' ')
print(string2[0:cuvant:])


# 19.  Cititi de la tastatura un string.
# Verificati daca primul si ultimul caracter sunt la fel.
# Se va folosi un assert.
# Atentie: se doreste ca programul sa fie case insensitive
# 'apA' e acceptat



string3 = input('Introduceti o propozitie: ')
string3low = string3.lower()
prima_litera  = string3low[0]
ultima_litera = string3low[-1]

assert prima_litera == ultima_litera



# 20.  Avand stringul '0123456789'
# Afisati doar numerele pare
# Apoi afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)

numere = '0123456789'

print(f'numerele pare sunt: {numere[0::2]}')
print(f'numerele impare sunt: {numere[1::2]}')


# Bonus la cerere:
# 21. Verificare imbarcare persoane
# Tineti urmatoarele date
# Varsta
# Insotit de mama
# Insotit de tata
# Pasaport
# Act permisiune mama
# Act permisiune tata
#
# Conditii de imbarcare
# Daca pers are varsta peste 18 ani si are pasaport
# Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte
#
# Aici vreau sa testati codul cu toate variantele posibile
# Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results
# Ex: # Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
# Etc
#

varsta = 18
cu_mama = True
cu_tata = False
pasaport = True
act_mama = True
act_tata = True

if varsta >= 18 and pasaport:
    print('Bine ai venit la bord!')

elif varsta < 18 and pasaport and cu_mama and cu_tata:
    print('Bine ai venit la bord!')

elif varsta < 18 and pasaport and cu_mama or cu_tata and act_mama or act_tata:
    print('Bine ai venit la bord!')

else:
    print('Imbarcare interzisa!')


# 22. Joc ghicit zarul
# Cautati pe net si vedeti cum se genereaza un numar random
# Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
# Luati un nr ghicit de la utilizator
# Verificati si afisati daca utilizatorul a ghicit
# 3 optiuni:
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# Felicitari! Ai ghicit. Ai ales x si zarul a fost y
#

import random
dice_roll = random.randint(0,5)
print(f' Numarul la intamplare este: {dice_roll}')

nr_ghicit = int(input('Introdu un numar de la 0 la 5: '))

if nr_ghicit == dice_roll:
    print(f'Felicitari! Ai ghicit. Ai ales {nr_ghicit} si zarul a fost {dice_roll}')
elif nr_ghicit < dice_roll:
    print(f'Ai ales un numar mai mic. Ai ales {nr_ghicit} dar a fost {dice_roll}')
elif nr_ghicit > dice_roll:
    print(f'Ai ales un numar mai mare. Ai ales {nr_ghicit} dar a fost {dice_roll}')


