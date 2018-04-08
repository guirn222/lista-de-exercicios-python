n1 = float(input ("digite a primeira nota"))
n2 = float(input ("digite a segunda nota"))
m = (n1+n2)/2
print(m)
if  m <= 4 and m >= 0  :
    print("Reprovado")
elif m > 4 and m <=7 :
    print("exame")
elif m >7 and m <=10 :
    print("Aprovado")
else:
    print("valor invalido")
