dico = {}
my_adress = "chezToi.com"

with open ("temp.txt", "r") as file :
    #sentence = f"{id}/{max_amount}/{adress}/{data}\n"
    lines = file.readlines()
    for line in lines :
        [id, max_amount, adress, data] = line.split("/")

        if my_adress.lower() == adress.lower() :
            dico[id] = data

key = "0"
current_data = dico[key]
print(f"""Sinece my adress is {my_adress}
        -key : {key}
        -current data : {current_data}""")