def gen_values () :
    k = -10
    while True :
        yield 16**k %18
        k += 1


class Human () :
    def __init__(self, name:str, age:int):
        self.my_name = name
        self.my_age = age

        self.my_health_points = 100
        self.is_alive = True

    def introduce(self) :
        sentence = f"Hello, my name is {self.my_name} and I'm {self.my_age} years old"
        print(sentence)

    def touched(self) :
        self.my_health_points -=10
        if self.my_health_points <= 0 :
            self.is_alive = False
    
    def live(self) : 
        while self.is_alive :
            pass