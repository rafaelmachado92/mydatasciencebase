print(" O CPF deverá conter 11 dígitos. Exclusivamente números deverão ser digitados")
while True:
    try:
        CPF = int(input("Digite o numero do CPF: "))
    
    except ValueError:
        print("Oops!  Digite apenas números...")

tam =(len(str(CPF)))
calc=str(CPF)
if  tam!=11 : print("Número inválido para análise")

else:


    p1= int(calc[0:1])
    p2= int(calc[1:2])
    p3= int(calc[2:3])
    p4= int(calc[3:4])
    p5= int(calc[4:5])
    p6= int(calc[5:6])
    p7= int(calc[6:7])
    p8= int(calc[7:8])
    p9= int(calc[8:9])
    p12= int(calc[9:10])
    p13= int(calc[10:11])

    soma =p1*10+p2*9+p3*8+p4*7+p5*6+p6*5+p7*4+p8*3+p9*2
    digito = soma % 11
    if digito <2:
        p10=0
    else:
        p10= 11-digito
    print(" Primero digito verificador esperado ",p10)
    
    soma2 =p1*11+p2*10+p3*9+p4*8+p5*7+p6*6+p7*5+p8*4+p9*3+p10*2
       
    
    digito2 = soma2 % 11
    if digito2 <2:
        p11=0
    else:
        p11= 11-digito2
    print("Segundo digito verificador esperado",p11)
    if p12==p10 and p13==p11:
        print("O CPF ",CPF, " é válido")
    else:
        print(" CPF inválido")

