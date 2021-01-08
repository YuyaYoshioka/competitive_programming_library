import math
Eratosthenes = [p for p in range(2,N)]
number = Eratosthenes[0]
sosuu = []
while number < N ** 0.5:
    sosuu.append(number)
    n_Eratosthenes = []
    for n in Eratosthenes:
        if n % number == 0:
            pass
        else:
            n_Eratosthenes.append(n)
    if len(n_Eratosthenes) == 0:
        break
    number = n_Eratosthenes[0]
    Eratosthenes = n_Eratosthenes
numbers=sosuu+Eratosthenes
