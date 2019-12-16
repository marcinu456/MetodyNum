def met1(x):
    return pow(x**4+4, .5)-2

def met2(x):
    return (x**4) / ( pow(x**4+4, .5)+2 )

for n in range(21):
    x = 2**(-n)
    m1 = met1(x)
    m2 = met2(x)
    r = m1 - m2

    print()
    print(f"\nn = {n}   x = {x}")
    print(f"Metoda 1: {m1}")
    print(f"Metoda 2: {m2}")
    print(f"różnica:  {r}")