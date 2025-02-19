#Task 1 - math module and constants

import math
import random
import matplotlib.pyplot as plt # type: ignore #alias = plt

def task1 () :
    print (math.pi) #circonference/diametre
    print (math.tau) #circonference/rayon
    print (math.e) #nombre d'euler
    print (math.inf) #infini
    print (math.nan) #nan -> not a number (erreur)

# Task 2 - Circle with math.py

def task2 () :
    def circle (rayon) :
        print (f"La circonference du cercle est {round(2*math.pi*rayon, 3)}")
        print (f"La circonference du cercle est {round(2**rayon*math.pi, 4)}")

    circle(3)

def extra () :
    print (math.factorial(5)) #Factoriel
    print (math.sqrt) #sqrt -> square root (racine carré)
    print (math.fabs(-5)) #valeur absolue

# Task 3 - random numbers

def task3 () :
    numbers = []

    for i in range (0,100) :
        numbers.append(random.randrange(0,10,2))
    print(numbers)

# Task 4 - I thought of a number..

def task4 () :

    chances = 7
    solution = random.randint(1, 101)
    tip = 0

    def check(num : int) :
        if num > solution:
            return "I thought of a smaller number"
        elif num < solution:
            return "I thought of a greater number"
        elif num == solution:
            return "I thought of this number"

    while tip != solution and chances > 0 :
        tip = int(input("Guess a number : "))
        print(check(tip))
        chances -= 1
    if tip == solution :
        print(f"The number was indeed {solution}")
    else :
        print(f"The number was {solution}")

# Task 5 - Using a package and creating a pie chart

def task5 () :
    
    def piechart (size : int, lab : str) :
        plt.pie(size, labels = lab, autopct= '%.2f%%')
        plt.show()

    n = int(input("How many games do you like ? "))
    games = [] #games names
    likes = [] #Note out of ten
    data = [] #Note in %
    db = s = 0

    for i in range (n) :
        game_name = input("Give me the game name : ")
        like = int(input("How much do you like the game, on 1 to 10 scale "))
        db += like
        games.append(game_name)
        likes.append(like)

    for i in range (n) :
        s = likes[i]/db*100 
        s = round(s, 1) #round -> arrondir
        data.append(s)

    piechart(data, games)

# Task 6 - Body fat percentage calculator

def task6 () : 
    def bmi( weight, height) :
        m = height / 100
        h = m*m
        bmi = round( weight/2, 2)
        return bmi

    w = int(input("What is your weight ? "))
    h = int(input("What is your height ? "))

    eval = bmi(w, h)
    print(f"Your body mass index is : {eval}")