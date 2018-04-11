vv = 0
vp=0
for x in range (15):
    tipo = input("\ndigite V para transição a vista e P para transição a prazo: ")
    valor = float(input("digite o valor da transação: "))
    if tipo == 'v':
        vv += valor
        
    if tipo == 'p':
        vp+=valor
        print('O valor da primeira prestação será:',valor/3)
print (f'o total de transições a vista é {vv}')
print (f'o total de transições a prazo é {vp}')
print (f'o valtotalde compras é de',vv+vp)
