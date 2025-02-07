def as_deep (nb_floors : int) : 
    if nb_floors > 0 :
        print(f"I'm at level {nb_floors}")
        as_deep(nb_floors-1)
    elif nb_floors == 0 :
        print("I'm at the final floor")


def fibonacci (val1 : int, val2 : int, level_max : int, nbr : int) : # Here only nbr = 1 
    if  level_max > 0:
        nbr = val1 + val2
        print(nbr)
        fibonacci(val2, nbr, level_max-1, nbr)


def harmonic_series (n : int, nbr : int, level : int) :
    if level > 0 :
        if  nbr%2 > 0 :
            nbr = -1**n-1*1/n - nbr 
        else :
            nbr = -1**n-1*1/n - nbr
        print(nbr)
        harmonic_series(n+1, nbr, level -1)
harmonic_series(1, 0, 50)