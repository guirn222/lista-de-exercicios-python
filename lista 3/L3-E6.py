c=0
alto = 0
valor = 0
for x in range(50,5,-5):
    x=x/10
    vl=(120+(c*26))*x-200
    print ("pelo valor de R$", x , "o locro estimado e de R$", vl)
    c=c+1
    if vl > alto :
        alto = vl
        valor = x
        

print ("\no valor mais alto conseguido com o espetaculo e: R$", alto , "\ncom o valor de : R$", valor, "por ingresso")
