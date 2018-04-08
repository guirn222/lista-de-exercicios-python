#programa que entre 10 idades e caucule a média dos valores maiores que 20 anos

id_tot = 0
c=0
v=0
while c<=10:
    idade = int(input("digite uma idade"))
    c=c+1
    if idade >20:
        id_tot+idade
        v=v+1
if v!=0:
    print (id_tot/v)
else:
    print("valor de V nao pode ser 0")
