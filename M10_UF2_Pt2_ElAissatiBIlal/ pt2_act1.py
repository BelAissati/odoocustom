def esPrimer(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Prova la funció amb els nombres del 1 al 20
for n in range(1, 21):
    if esPrimer(n):
        print(n)
