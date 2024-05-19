import random
import primeModule as pm

primeNumbers = []
n = 0
while n < 10:
    rn = random.randint(1, 1000)
    if rn not in primeNumbers:
        try:
            pm.isPrime(rn)
        except pm.NotPrimeException as e:
            print(e)
            continue

        except pm.PrimeException as e:
            print(e)
            primeNumbers.append(rn)

    else:
        print(f'{rn} is overlap number~!!')
        continue

    n += 1

print(f'primeNumbers: {primeNumbers}')