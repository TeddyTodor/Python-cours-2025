def facto (nbr : int) :
    if nbr == 0 or nbr == 1:
        print("final")
    else : 
        res = nbr*facto(nbr-1)
        return res

def exo_graph () :
    import math
    import matplotlib.pyplot as plt

    x = [i for i in range (-15, 16, 1)]
    y = [x[i]**2 for i in range (len(x))]
    plt.style.use('dark_background')
    plt.plot(x, y)
    plt.show()

def loop (nbr : int) :
    while True :
        nbr += 1 
        if nbr % 2 == 0 :
            yield nbr

for i in loop (7) :
    print(i)
    if i >= 100000 :
        break