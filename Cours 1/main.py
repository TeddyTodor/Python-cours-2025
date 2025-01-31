lst = [62, 37, 6, 14, 8, 9, 6, 120, 7, 3, 64, 61, 20, 7, 34 ,6]

def sorting_list(lst : list) :
    print(f"Before the swap : {lst}")
    for i in range (len(lst)-1) :
        for j in range(len(lst)-1) :
            if lst[i] > lst[j] :
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

    print(f"After the sort : {lst}")

def compute_the_sum_and_value(lst : list) :
    """
        Cette fonction prend en paramètre une liste afin d'en calculer la somme des éléments
        ainsi que la moyenne.
        
        Après ces savants calculs, la fonction RETURN ses réponses
    """
    somme = 0
    moyenne = 0
    for i in range (len(lst)) :
        somme += lst[i]
    moyenne = somme/len(lst)
    sentence = f"""Après de savant calcul je me rend compte que :
        -Pour la liste : {lst}
        -La somme vaut : {somme}
        -La moyenne vaut : {moyenne}"""
    print(sentence)
    return moyenne, somme

#mean_value, sum_value = compute_the_sum_and_value(lst)

def find_first_even_number(lst : list) :
    i = -1
    for i in range (len(lst)) :
        if lst[i] % 2 == 0 :
            print(f"{i} : {lst[i]}")
            return i
    return i

current_even_number_index = find_first_even_number(lst)
while (current_even_number_index != -1) :
    lst.pop(current_even_number_index)
    current_even_number_index = find_first_even_number(lst)
    #lst.pop(current_even_number_index)
    print(lst)