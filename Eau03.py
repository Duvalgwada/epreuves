# Suite de FIBONACCI (Je ne sais pas ce que c'est)

# Histoire que je soit moins con
# La suite de Fibonacci est une séquence de nombres dans 
# laquelle chaque nombre est la somme des deux nombres précédents, 
# à partir des deux premiers nombres 0 et 1. Elle commence généralement 
# par 0, 1, puis continue comme suit : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
# F(n)=F(n-1)+f(n-2)

n = int(input("Entrez la valeur de N : "))

# Formule de Fibonacci
def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(n)

# Condition si valeur negative
if result == -1:
    print("Négatif ou mauvais paramètre.")
else:
    print(f"Le {n}-ème élément de la suite de Fibonacci est : {result}")

# Sincerement, je n'ai pas compris