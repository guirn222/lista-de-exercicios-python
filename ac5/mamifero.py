from animal import Animal

class Mamifero(Animal):

    def __const__(self):
        pass

    def __init__(self,possuiPelos=None,qntGldMam=None,estaAmamentando=None):
        self.__possuiPelos=possuiPelos
        self.__qntGldMam=qntGldMam
        self.__estaAmamentando=estaAmamentando

    def getPossuiPelos(self):
        return self.__possuiPelos
    def setPossuiPelos(self,possuiPelos):
        self.__possuiPelos=possuiPelos

    def getQntGldMam(self):
        return self.__qntGldMam
    def setQntGldMam(self,qntGldMam):
        self.__qntGldMam=qntGldMam
    
    def getEstaAmamentando(self):
        return self.__estaAmamentando
    def setEstaAmamentando(self,estaAmamentando):
        self.__estaAmamentando=estaAmamentando


    def amamentar(self, filhote):
        if self.__sexo == "macho":
            print ("O mamífero é macho, portanto não pode amamentar")
        else:
            print("está amamentando ", filhote,"filhotes")

    def imprimeDadosMamifero(self):
        #print(self.__nome)
        #print(self.__idade)
        #print(self.__sexo)
        print(self.getPossuiPelos)
        #print(self.__qntGldMam)
        #print(self.__estaAmamentando)

cachorro = Mamifero(True,3,"sim")
print(cachorro.imprimeDadosMamifero())
        