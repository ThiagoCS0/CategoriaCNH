def Dados():
try:
  M("Dados sobre o veículo\n")
  rodas=int(input("Quantas rodas: "))
  peso=int(input("Peso: "))
  pessoas=int(input("Passageiros: "))
  Verificar(rodas,peso,pessoas)
except:
  M("\n"*2)
  M("\n[ERRO]\nDigite apenas NÚMEROS!!\n")
  Dados()

def Verificar(rodas,peso,pessoas):
if rodas<4:
  M("Categoria A")
else:
 if peso<=3500 and pessoas<=8:
  M("Categoria B")
 elif pessoas>=8:
  M("Categoria D")
 elif peso>=3500 and peso<=6000:
  M("Categoria C")
 else:
  M("Categoria E")
  
def M(mensagem):
print(mensagem)

Dados()
