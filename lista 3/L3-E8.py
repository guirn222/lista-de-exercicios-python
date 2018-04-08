c1=0
c2=0
c3=0
c4=0
c5=0

for x in range (15):
    x+=1
    i=int(input(f'digite a {x}º idade: ')) 
    if i >= 1 and i <= 15:
        c1+=1
    elif i >= 16 and i <= 30:
        c2+=1
    elif i >= 31 and i <= 45:
        c3+=1
    elif i >= 46 and i <= 60:
        c4+=1
    elif i >= 61:
        c5+=1
print (f'O valor de pessoas nas faixas etárias são:')
print('1º: ', c1)
print('2º: ', c2)
print('3º: ', c3)
print('4º: ', c4)
print('5º: ', c5,'\n')
t= c1+c2+c3+c4+c5
print ('aporcentagem de pessoas na primeira faixa etária é: ',(100*c1)/t)
print ('aporcentagem de pessoas na ultima faixa etária é: ',(100*c5)/t)
