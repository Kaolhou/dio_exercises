"""
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.

"""
menu = """[d] depositar
[s] sacar
[e] extrato
[q] sair
"""
saldo = 0
limite = 500
extrato = ""
saques=0
LIMITE_SAQUES = 3

def log(entrada:bool,amount:float):
  global extrato
  seta = "->" if entrada else"<-"
  entrada = "entrada" if entrada else "saída"
  data = f"{seta} R${amount:.2f} ({entrada})"
  extrato+=data+'\n'
  print(data)

while True:
  operacao = input(menu)
  if(operacao == "q"):
    break
  elif(operacao == 'd'):
    valor = float(input("informe o valor do depósito: "))
    if(valor<0):
      print("valor inválido")
    saldo += valor
    log(True,valor)
    # print(f"depósito de {valor} realizado com sucesso")
    print(f"saldo: R${saldo:.2f}")
  elif(operacao=='s'):
    if(LIMITE_SAQUES == saques):
      print("limite de saques excedidos")
      continue
    valor = float(input("informe o valor do saque: "))
    if(valor>limite):
      print(f"valor não pode passar de {limite} reais")
      continue
    if(valor<0):
      print("valor inválido")
    saques+=1
    saldo-=valor
    log(False,valor)
    # print(f"saque de {valor} realizado com sucesso")
    print(f"saldo: R${saldo:.2f}")
  elif(operacao=="e"):
    print("==========extrato==========")
    print(f"Saldo:{saldo:.2f}")
    print(extrato)
    print("===========================")
  else:
    print('operação inválida')
