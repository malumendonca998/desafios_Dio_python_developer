# Lendo as três palavras de entrada
palavra1 = input()
palavra2 = input()
palavra3 = input()

# Inicializando a variável do animal como uma string vazia
animal = ""

# Verificando as palavras e identificando o animal
if palavra1 == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            animal = "aguia"
        elif palavra3 == "onivoro":
            animal = "pomba"
    elif palavra2 == "mamifero":
        if palavra3 == "onivoro":
            animal = "homem"
        elif palavra3 == "herbivoro":
            animal = "vaca"
elif palavra1 == "invertebrado":
    if palavra2 == "inseto":
        if palavra3 == "hematofago":
            animal = "pulga"
        elif palavra3 == "herbivoro":
            animal = "lagarta"
    elif palavra2 == "anelideo":
        if palavra3 == "hematofago":
            animal = "sanguessuga"
        elif palavra3 == "onivoro":
            animal = "minhoca"

# Imprimindo o animal identificado
print(animal)
