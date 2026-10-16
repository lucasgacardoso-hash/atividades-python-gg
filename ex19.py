not1= float(input("Digitar nota: "))
not2= float(input("Digitar segunda nota: "))

media = (not1+not2) /2

if media>= 7.0:
    print("Aprovado")
elif media <= 5.0:
    print ("Reprovado")
else:
    print("Recuperação")
