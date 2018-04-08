op = int(input("DIGITE UMA OPÇÃO\n\n"
               "1-Média entre os números digitados\n"
               "2-Diferença do maior pelo menor\n"
               "3-Produto entre os números digitados\n"
               "4-Divisão do primeiro pelo segundo\n"))

n1= float(input("Digite o primeiro valor para o cálculo: "))
n2= float(input("Digite o segundo valor para o cálculo: "))

if op == 1:

    print( (n1+n2)/2 )
    
elif op == 2:

    if n1 > n2:
        print (n1 - n2)
    else:
        print (n2 - n1)

elif op == 3:

    print (n1*n2)

elif op == 4 and n2 != 0:

    print(n1/n2)

else:
    print("opção invalida")
