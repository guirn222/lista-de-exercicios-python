#programa que leia um valor N inteiro e positivo
#calcule e mostre a seguinte soma:
# S = 1 + 1/2 + 1/3 . . . 1/N

n=int(input("digite um numero natural e positivo "))
while n <= 0 :
    n=int(input("numero invalido, digite outro numero "))
    
total= 0
for x in range (1,n+1,1):
    total = total+(1/x)
        
print (total)
