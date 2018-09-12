from animal import Animal
from mamifero import Mamifero

class Zoologico(Mamifero):
    
    
    def __init__(self):
        self.__lista=[]

    def adcionaAnimal(self):
        self.__lista.append(self.__nome)



    def removeAnimal(self):
        for x in self.__lista:
            if x == self:
                self.__lista.remove(x)
            else:
                print("Animal não enctontrado.")

    def imprimeAnimais(self):
        for x in self.__lista:
            print (x.getNome)