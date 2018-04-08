fab= float(input("digite o custo de fabrica: "))
if fab < 12000:
    print ("porcentagem do distribuidor (5%):", fab*0.05,
           "\n porcentagem de impostos (0%): 0.0"
           "\n valor final:", (fab*0.05) + fab)
elif fab >=12000 and fab< 25000:
    print ("porcentagem do distribuidor (10%):", fab*0.10,
           "\n porcentagem de impostos (15%): ", fab*0.15,
           "\n valor final:", (fab*0.10) + (fab*0.15) + fab)
elif fab >= 25000 :
        print ("porcentagem do distribuidor (15%):", fab*0.15,
           "\n porcentagem de impostos (20%): ", fab*0.20,
           "\n valor final:", (fab*0.15) + (fab*0.20) + fab)
else:
    print ("valor invalido")
