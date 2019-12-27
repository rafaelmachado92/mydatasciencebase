numero = int(input("Digite um numero para ser avaliado: "))
teto = 0
x=[]
i=1

for divisor in range(1, numero):
    
    if numero % divisor == 0:
        teto = teto + 1
        
        if teto > 1:
          break
if teto > 1:
  print("não é primo")
  print("Ele é divisivel por: ",[i for i in range(1, numero) if numero%i==0])
  
else:
  print("é primo")

