import matplotlib.pyplot as plt

def f(x : float) :
    return x**2

def plot_f () :
    x_axe = [i for i in range(-20,21,2)]
    y_axe = [f(x_axe[i]) for i in range(len(x_axe))]
    plt.plot(x_axe, y_axe)
    plt.show()

def compute_tax (income : float) :
    threshold = 15_000
    if income < threshold :
        taxe = 0.15*income - 560
        taxe = 0 if taxe < 0 else taxe
        return taxe
    else : 
        surplus = income - threshold
        taxe = 0.15*threshold + 0.28*surplus
        return taxe