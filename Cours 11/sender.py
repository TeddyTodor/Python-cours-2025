def gen_values() :
    k = 0
    while True :
        yield 2**k
        k+=1
def diplay_well (M : list[list[int]]) :
    for id in range (len(M)) :
        data = M[id]
        print(f"{id}/{data}") 

generator = gen_values()
M = [[next(generator) for _ in range (5)] for _ in range (5)]

#diplay_well (M)

with open("temp.txt", "w") as file :
    for id in range (len(M)) :
        data = M[id]
        max_amount = len(M)
        adress = "chezToi.com"
        sentence = f"{id}/{max_amount}/{adress}/{data}\n"
        file.write(sentence)