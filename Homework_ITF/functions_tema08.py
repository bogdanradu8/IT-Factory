# 1. Creati-va 2 fisiere separate, unul numit functions_tema08.py, in care sa adaugati implementarea, iar altul numit test_functions_tema08.py in care sa aveti clasa de test.
# a) Scrieti o functie care primeste un numar natural si returneaza daca e prim sau nu
#  e.g.: is_prime(13) => True
#          is_prime(24) => False
# b) Scrieti 2 teste unitare (unul pentru True si unul pentru False) pentru functia is_prime
# c). Scrieti o functie care are 2 parametrii nr naturale a,b cu a<b. Functia returneaza lista numerelor prime din intervalul [a,b].
# e.g.: list_of_primes_in_interval(3, 31) => [3,5,7,11,13,17,19,23,29,31]
# d) Scrieti 2 teste unitare pentru functia list_of_primes_in_interval

def is_prime(num = 0):
           
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
        
    else:
        return False

print(is_prime(15))