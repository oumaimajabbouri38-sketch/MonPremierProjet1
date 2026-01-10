a = float(input("Entrez un nombre: "))
b = float(input("Entrez un nombre: "))

operation = input("Entrez l'operation (+ - * /): ")

if operation == "+":
    resultat = a + b

elif operation == "-":
    resultat = a - b

elif operation == "*":
    resultat = a * b

elif operation == "/":
    if b != 0:
        resultat = a / b
    else:
        print("Division par 0 impossible")
        resultat = None

else:
    print("Operation invalide")
    resultat = None

if resultat is not None:
    print("Le resultat est :", resultat)