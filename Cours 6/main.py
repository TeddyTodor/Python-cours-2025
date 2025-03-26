def exo1 () :  
    def tax_calcultor (income) :
        if income < 1 :
            tax = 0.0
        elif income > 0 and income < 1000:
            tax = income
        elif income > 999 and income < 10000 :
            tax = income
        else :
            tax = income
    incomes = [ [1000, 10000, 6549, 22334, 98654],
                [8436, 98731, 9853, 7585, 43665],
                [6453, 52532, 96649, 4214, 560],
                [12, 965, 4568, 986, 123]]

    taxes = []
    for list in incomes:
        for person in list:
            tax = tax_calcultor(person)
            taxes.append(tax)
    for i in range (len(taxes)) :
        print (f"Tax of peson {i} is {taxes[i]}.")

def listComprehension():
    list1 =[]
    for i in range(4,27) :
        list1.append(i)
    print(list1)

    list2 = [x for x in range (4, 27)]
    print(list2)

def evenNumbers () : 
    list3 = [x for x in range (0,100) if x%2 == 0]
    print (list3)

def matrixComprehension () :
    matrix = [[i for i in range(10)] for j in range(10)]
    matrix2 = [[j for i in range(10)] for j in range(10)]
    print(matrix)
    print(matrix2)

def matrixCreation () :
        num = [[i**4 + j for i in range(10)] for j in range(3)]
        for item in num :
            print(item, end = "\n")

import random
#import numpy as np

def weatherCalculator ():
    
    month = [[random.randint(-5, 32) for i in range(24)] for j in range(30)]

    for item in month : 
        print(item) 
    
    avg_temp = []
    for day in month :
        avg_temp.append(round(np.mean(day), 2))
    print(f"The averge temperature of the days : \n {avg_temp}")
    max = np.max(avg_temp)
    index = avg_temp.index(max) + 1
    print(f"The highest average temperature of the mont was {max} and it was on day {index}")
    avg_temp_month = np.mean(avg_temp)
    print(f"The average temperature of the whole month was {avg_temp_month}")

def cubes() : 
    cube_1 = []
    for building in range(3) :
        list2 = []
        for floor in range(3) :
            list1 = []
            for room in range(3) :
                list1.append(random.randint(0, 1))
            list2.append(list1)
        cube_1.append(list2)
    print(cube_1)

cube_2 = [[[random.randit(0, 1) for room in range(3)]for floor in range(3)]for building in range(3)]