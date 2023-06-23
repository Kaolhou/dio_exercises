import textwrap
"""
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.

"""
# saldo = 0
# limite = 500
# extrato = ""
# saques=0
# LIMITE_SAQUES = 3
auto_increment = 1
clientes = []

def menu():
  menu = """\n
  [d] depositar
  [s] sacar
  [e] extrato
  [nc] nova conta
  [l] listar contas
  [nu] novo usuário
  [q] sair
  => """
  return input(textwrap.dedent(menu))

def autoIncrement():
  global auto_increment
  data = auto_increment
  auto_increment+=1
  return data

def criarCliente(nome,email,cpf,endereco):
  global clientes
  for cliente in clientes:
    if cliente['cpf'] == cpf:
      print('usuário já foi criado')
      return

  clientes.append({
    'nome': nome,
    'email':email,
    'cpf':cpf,
    'endereco':endereco,
    'conta': []
  })

def imprimirExtrato(conta):
  print("==========extrato==========")
  print(f"Saldo:{conta['saldo']:.2f}")
  print(conta['extrato'])
  print("===========================")

def criarConta():
  # contaID = auto_increment()
  return {
    'agencia':'0001',
    'conta': autoIncrement(),
    'saldo': 0,
    'limite': 500,
    'saques': 0,
    'extrato': ''
  }

def log(entrada, amount,conta):
  seta = "->" if entrada else"<-"
  entrada = "entrada" if entrada else "saída"
  data = f"{seta} R${amount:.2f} ({entrada})"
  conta['extrato'] +=data+'\n'
  print(data)

def encontrarCliente(cpf):
  for cliente in clientes:
    if cliente['cpf'] == cpf:
      return cliente
  return None

def listarContas(cpf):
  cliente = encontrarCliente(cpf)
  if cliente is None or cliente['conta'] is None:
    print('Sem contas registradas')
  else:
    for i, conta in enumerate(cliente['conta']):
      print("==============")
      print(f"Conta {i+1}:")
      print(f"Agência: {conta['agencia']}")
      print(f"Saldo: {conta['saldo']}")
      print(f"Número da conta: {conta['conta']}")

def saque(conta,valor):
  if(conta['limite'] == conta['saques']):
    print("limite de saques excedidos")
    return
  if(valor>conta['saldo']):
    print("saldo insuficiente")
    return
  if(valor>conta['limite']):
    print(f"valor não pode passar de {limite} reais")
    return
  if(valor<0):
    print("valor inválido")
    
  log(False,valor,conta)
  conta['saques']+=1
  conta['saldo']-=valor

def deposito(conta, valor):
  if(valor<0):
    print("valor inválido")
  conta['saldo'] += valor
  log(True,valor,conta)

def getCpf():
  data = """
  por favor, insira o seu cpf
    => """
  return input(textwrap.dedent(data))

def getValor():
  return int(input("Insira o valor: "))

while True:
  operacao = menu()
  if(operacao == "q"):            
    break
  elif(operacao == 'd'):
    cpf = getCpf()
    cliente = encontrarCliente(cpf)
    if(cliente != None):
      if(len(cliente['conta'])==0):
        print('cliente encontrado porém sem contas vinculadas deseja criar? y/n')
        resposta = input().lower() == 'y'
        
        simnao = 'sim' if resposta else 'não'
        print(f'resposta {simnao}')
        if(not resposta): continue
        cliente['conta'].append(criarConta())
        print("conta criada com sucesso")

      listarContas(cpf)
      contaID = int(input("qual conta deseja usar? ")) - 1
      
      deposito(cliente['conta'][contaID],getValor())
    else:
      print("cliente não encontrado por favor crie um")
    
  elif(operacao=='s'):
    cpf = getCpf()
    cliente = encontrarCliente(cpf)
    if(cliente != None):
      if(len(cliente['conta'])==0):
        print('cliente encontrado porém sem contas vinculadas deseja criar? y/n')
        resposta = input().lower() == 'y'
        
        simnao = 'sim' if resposta else 'não'
        print(f'resposta {simnao}')
        if(not resposta): continue
        cliente['conta'].append(criarConta())
        print("conta criada com sucesso")

      listarContas(cpf)
      contaID = int(input("qual conta deseja usar? ")) - 1
      
      saque(cliente['conta'][contaID],getValor())
  elif(operacao=="e"):
    cpf = getCpf()
    cliente = encontrarCliente(cpf)
    if(cliente != None):
      if(len(cliente['conta'])==0):
        print('cliente encontrado porém sem contas vinculadas')
        continue

      listarContas(cpf)
      contaID = int(input("qual conta deseja usar? ")) - 1
      
      imprimirExtrato(cliente['conta'][contaID])
  elif(operacao=='nc'):
    cpf = getCpf()
    cliente = encontrarCliente(cpf)
    cliente['conta'].append(criarConta())
    print("conta criada com sucesso")

  elif(operacao=='nu'):
    nome, email, cpf, endereco = input("por favor insira os dados separados por dois espaços").split('  ') 
    criarCliente(nome,email,cpf,endereco)
    print("cliente criado com sucesso")
  elif(operacao=='l'):
    cpf = getCpf()
    listarContas(cpf)

  else:
    print('operação inválida')
