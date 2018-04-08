#verifica se um numero natural é primo
c=0
n=int(input("numero"))
for x in range (1,n+1,1):
    if n%x == 0:
        c=c+1
    if c==2:
        print("primo")
    else:
        print("nao é primo")
