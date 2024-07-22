C = int(input("insira um numero de testes:"))
energias = []
for i in range(C):
    N = int(input("insira um numero:"))  
    energias.append(N)  
for i in energias:
    if i <= 8000:
        print("Inseto")
    else:
        print("Mais de 8000!")
