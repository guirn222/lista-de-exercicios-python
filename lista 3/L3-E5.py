print ("########################################")
for x in range (15):

    nome =input ("digite o nome do cidadão: ")
    valor = int(input("quanto ele gastou no ultimo ano? "))
    if valor < 1000:
        print ("\nvocê,", nome,"ganhou um bonus de ", valor*0.1,)
        print ("########################################\n")
    else:
        print ("\nvocê,", nome,"ganhou um bonus de ", valor*0.15,)
        print ("########################################\n")
 
