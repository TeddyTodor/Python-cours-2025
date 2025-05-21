def openFile() :
    f = open("text.txt", "r", encoding = "utf-8")
    print(f.read()) # or content = f.read() -> print(content)
    f.close()


def openFileCharacters():
    f = open("text.txt", "r")
    print(f.read(6))
    f.seek(0)
    print(f.read(6))
    f.close()


def openLines() :
    f = open("text.txt", "r", encoding = "utf-8")
    lines = f.readlines()
    for line in lines : 
        print(line, end = "")
    f.close()


def openCharFromLine() :
    f = open("text.txt", "r")
    lines = f.readlines()
    for line in lines :
        print(line[2:4])
    f.close()


def findText() :
    with open("text.txt") as f :
        if "texte" in f.read():
            print("Dans le texte")
        else :
            print("Pas dans le texte")


def createFile (file_name : str) :
    f = open(file_name + ".txt", "w")
    f.close()



def writeInCreateFile () :
    f = open("Python.txt", "w+")
    f.write("Welcome to the Internet...")
    f.seek(0)
    print(f.read())
    f.close()


def nbr1_10 () :
    f = open("newFile.txt", "w+")
    for i in range (1,11) :
        f.write(str(i) + " ")
    f.seek(0)
    print(f.read())
    f.close()


def replace () :
    f = open("text.txt", "r", encoding = "utf-8")
    text = f.read().replace(" ", "")
    g = open("noSpaces.txt", "w+")
    g.write(text)
    g.seek(0)
    print(g.read)
    f.close()
    g.close()


def lastLines (n) :
    f = open("text.txt", "r", encoding = "utf-8")
    lines = f.readlines()
    while n > 0:
        print (lines[-n], end = "")
        n -= 1
        f.close()