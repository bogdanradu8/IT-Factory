# 1. (In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila )

# variabila este un loc din memorie unde se pot stoca date

''' 2 & 3.
(Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
 string, int, float, bool
 Valorile le alegeti voi dupa preferinte)
 Utilizati functia type pentru a verifica daca au tipul de date asteptat
'''

nume_telefon = 'Samsung'
generatie_procesor = 8
diagonala_ecran = 6.57
functie_nfc = True

print(type(nume_telefon))
print(type(generatie_procesor))
print(type(diagonala_ecran))
print(type(functie_nfc))

''' 4.
Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
Verificati tipul acesteia
'''

diagonala_ecran = round(diagonala_ecran)
print(type(diagonala_ecran))

''' 5.
folositi print() si printati in consola 4 propozitii folosind cele 4 variabile. 
(rezolvati nepotrivirile de tip prin ce modalitate doriti)
'''

print(f'Am cumparat un telefon {nume_telefon}. Are generatia {generatie_procesor} de procesor.\nEcranul are dimensiunea de aproximativ {diagonala_ecran} inch.')
print(f'Are functia NFC? : ',functie_nfc)

''' 6.
citeste de la tastatura numele
citeste de la tastatura prenumele
afiseaza 'Numele complet are x caractere'
'''

nume = input('Introduceti prenumele: ')
prenume = input('Introduceti numele: ')
nume_complet = nume + ' ' + prenume

print('Numele complet este', nume_complet)
print('Numele complet are', len(nume_complet)-1, 'caractere.')

''' 7.
citeste de la tastatura lungimea
citeste de la tastatura latimea
afiseaza 'Aria dreptunghiului este x'
'''

lungime = int(input('Introduceti lungimea: '))
latime = int(input('Introduceti latimea: '))
aria = lungime * latime
print('Aria dreptunghiului este',aria)

''' 8.
Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
afisati de cate ori apare cuvantul 'the'
'''

enunt = 'Coral is either the stupidest animal or the smartest rock'
print(enunt.count('the'))

''' 9.
acelasi string
inlocuieste the cu THE peste tot
printeaza rezultatul
'''

new_enunt = enunt.replace("the", "THE")
print(new_enunt)

''' 10. 
citeste de la tastatura un string de dimensiune impara
afiseaza caracterul din mijloc
'''

string2 = input('Introdu un cuvant: ')
litera_index = len(string2) // 2
print(f'Litera din mijloc este: {string2[litera_index]}')


''' 11. Folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
si salveaza fiecare cuvant intr-o variabila
acum printeaza ambele variabile pentru verificare
'''

a,b = input('Introdu 2 cuvinte').split()
print(a)
print(b)

'''12. 
citeste un string de la tastatura (eg: alabala portocala)
salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite) 
capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
=> alAbAlA portocAla
'''

string3 = input('Introdu o propozitie: ')
primul = string3[0]

string3 = string3[0] + string3[1:-1].replace(primul, primul.upper()) + string3[-1]
print(string3)

'''13. Citeste un user de la tastatura
citeste o parola
afiseaza: 'Parola pt user x este ***** si are x caractere'
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
eg: parola abc => ***
parola abcd => ****
'''

user3 = input('Introduceti username: ')
password = input('Introduceti parola: ')

print(f"Parola pt user {user3} este {len(password) * '*'} si are {len(password)} caractere.")

'''14. TODO_1 de la curs (C01EX01)
Cum facem sa afisam valoare lui pi cu doar 2 zecimale? presupunem pi = 3.146712
'''

pi = 3.141592653589793
print(round(pi,2))

'''# 15. TODO_2 de la curs (C01EX02)
# Avand my_string = "Hello Pythonistas" , vrem sa afisam stringul: "eoyoss"
my_string = "Hello Pythonistas"
'''

my_string2 = 'Hello Pythonistas'
print(my_string2[1::3])
