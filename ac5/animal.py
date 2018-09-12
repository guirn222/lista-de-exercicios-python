class Animal:
    def __const__(self):
        pass
    def __init__(self, nome=None,idade=None,sexo=None):
        self.__nome=nome
        self.__idade=idade
        self.__sexo=sexo

        #if min != None:
        #    self.cmin = min
        #if max != None:
        #    self.cmax = max

    
    def getNome(self):
        return self.__nome
    def setNome(self,nome):
        self.__nome=nome

    def getIdade(self):
        return self.__idade
    def setIdade(self,idade):
        self.__idade=idade

    def getSexo(self):
        return self.__sexo
    def setSexo(self,sexo):
        self.__sexo=sexo
    
    def dormir(self):
        print(self.__nome,"está dormindo")

    def acordar(self):
        print(self.__nome,"está acordado")

jacare = Animal("jacare",26,"macho")

jacare.dormir()
