from animal import Animal
from mamifero import Mamifero
from zoologico import Zoologico

escolha = 0
print ("escolha uma opção:")
print ("1 - adcionar um animal")
print ("2 - remover um animal")
print ("3 - mostrar lista de animais")
escolha = int(input())

if escolha == 1 : 
    animal1 = str(input("digite o animal para adcionar: "))
    Zoologico.adcionaAnimal(animal1)
elif escolha == 2: 
    animal2 = str(input("digite o animal para remover"))
    Zoologico.removeAnimal(animal2)
else:
    Zoologico.imprimeAnimais(lista)
