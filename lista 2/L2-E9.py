sm = float(input("digite o saldo médio: "))

if sm >0 and sm <200:
    cr = sm*0.1
    print("seu saldo médio é:", sm ," e seu crédito é de", cr)
elif sm >=200 and sm<300:
    cr= sm*0.2
    print("seu saldo médio é:", sm ," e seu crédito é de", cr)
elif sm >=300 and sm<400:
    cr=sm*0.25
    print("seu saldo médio é:", sm ," e seu crédito é de", cr)
elif sm >=400:
    cr= sm*0.3
    print("seu saldo médio é:", sm ," e seu crédito é de", cr)
else:
    print("o valor não pode ser negativo")
