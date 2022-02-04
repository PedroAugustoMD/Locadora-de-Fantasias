import pickle
import random

clientes = {}
try:
  arqClientes = open("clientes.dat", "rb")
  clientes = pickle.load(arqClientes)
  arqClientes.close()
except IOError:
  print("Erro ao abrir o arquivo")
  print("Base de dados está vazia!")

fantasias = {}
try:
  arqFantasias = open("fantasias.dat", "rb")
  fantasias = pickle.load(arqFantasias)
  arqFantasias.close()
except IOError:
  print("Erro ao abrir o arquivo")
  print("Base de dados está vazia!")

def validaCPF(cpf):
  tam = len(cpf)
  soma = 0
  d1 = 0
  d2 = 0
  if tam != 11:
    return False
  for i in range(0,10):
    if (int(cpf[i]) < 0 or int(cpf[i]) > 9):
      return False
  for i in range(0,9):
    soma += (int(cpf[i]) * (10 - i))
  d1 = 11 - (soma % 11)
  if (d1 == 10 or d1 == 11):
    d1 = 0
  if d1 != int(cpf[9]):
    return False
  soma = 0
  for i in range(0,10):
    soma += (int(cpf[i]) * (11 - i))
  d2 = 11 - (soma%11)
  if (d2 == 10 or d2 == 11):
    d2 = 0
  if d2 != int(cpf[10]):
    return False

  return True

resp = 15
while resp != 0:
  print()
  print(" = = = = = = = = = = = = = = = == = = = = = = = = = = = = = = =")
  print(" = = = PyFantasie - Alugue suas fantasias por uma semana  = = =")
  print(" = = = = = = = = = = = = = = = == = = = = = = = = = = = = = = =")
  print("1. Cadastro")
  print("2. Consultar")
  print("3. Alterar")
  print("4. Excluir")
  print("5. Alugar fantasia")
  print("6. Devolver fantasia")

  print("0. Encerrar programa")
  resp = int(input("Escolha sua opção: "))

  if resp == 1:
    escolha = int(input("Digite 1 para cadastrar uma fantasia ou 2 para cadastrar um cliente: "))
    if escolha == 1:
      id = input("Qual o id da fantasia a cadastrar? ")
      if id not in fantasias:
        nome = input("Qual o nome da fantasia? ")
        aluguel = float(input("Qual o valor do aluguel? "))
        fantasias[id] = [nome, aluguel, True, 0]
        print("Fantasia %s cadastrada com sucesso"%id)
      else:
        print("ID já cadastrado")
    elif escolha == 2:
      cpfInt = int(input("Qual o cpf do cliente? "))
      cpf = str(cpfInt)
      if (validaCPF(cpf)):
        if cpf not in clientes:
          nome = input("Qual o nome do cliente? ")
          email = input("Qual o email do cliente? ")
          telefone = input("Qual o telefone do cliente ")
          clientes[cpf] = [nome, email, telefone, 0.0, 0]
          print("Cliente %s cadastrado com sucesso"%cpf)
        else:
          print("CPF já cadastrado!")
      else:
        print("CPF inválido!")
    else:
      print("Escolha Inválida!")

  elif resp == 2:
    escolha = int(input("Digite 1 para consultar uma fantasia ou 2 para consultar um cliente: "))
    if escolha == 1:
      id = input("Qual o id da fantasia a consultar? ")
      if id in fantasias:
        print()
        print('ID  :', id)
        print('Nome  :', fantasias[id][0])
        print('Aluguel : R$ %.2f'%fantasias[id][1])
        print('Alugada %d vezes'%fantasias[id][3])
        if fantasias[id][2]:
          print('Status: Fantasia disponível')
        else:
          print('Status: Fantasia não disponível')
      else:
        print('Fantasia %s não está cadastrada!'%id)
    elif escolha == 2:
      cpf = input("Qual o cpf do cliente a consultar? ")
      if cpf in clientes:
        print()
        print('CPF  :', cpf)
        print('Nome  :', clientes[cpf][0])
        print('Email  :', clientes[cpf][1])
        print('Telefone  :', clientes[cpf][2])
        print('Deve : R$ %.2f'%clientes[cpf][3])
        print('Alugou %d fantasias'%clientes[cpf][4])
      else:
        print('Cliente %s não está cadastrado!'%cpf)
    else:
      print("Escolha Inválida!")
  
  elif resp == 3:
    escolha = int(input("Digite 1 para alterar uma fantasia ou 2 para alterar um cliente: "))
    if escolha == 1:
      id = input("Qual o id da fantasia a alterar? ")
      if id in fantasias:
        print()
        print("Qual item deseja alterar?")
        print("a. Nome")
        print("b. Valor do aluguel")
        print("c. Disponibilidade")
        item = input("Escolha um item: ")
        item = item.lower()
        if item == 'a':
          nome = input("Qual o nome da fantasia? ")
          fantasias[id][0] = nome
        elif item == 'b':
          aluguel = float(input("Qual valor do aluguel? "))
          fantasias[id][1] = aluguel
        elif item == 'c':
          fantasias[id][2] = not(fantasias[id][2])
        else:
          print("Item informado não é válido")
        print("Fantasia %s alterada com sucesso"%id)
      else:
        print('Fantasia %s não está cadastrada!'%id)
    if escolha == 2:
      cpf = input("Qual o cpf do cliente a alterar? ")
      if cpf in clientes:
        print()
        print("Qual item deseja alterar?")
        print("a. Nome")
        print("b. Email")
        print("c. Telefone")
        item = input("Escolha um item: ")
        item = item.lower()
        if item == 'a':
          nome = input("Qual o nome do cliente? ")
          clientes[cpf][0] = nome
        elif item == 'b':
          email = input("Qual o email do cliente? ")
          clientes[cpf][1] = email
        elif item == 'c':
          telefone = input("Qual o telefone do cliente? ")
          clientes[cpf][2] = telefone
        else:
          print("Item informado não é válido")
        print("Cliente %s alterado com sucesso"%cpf)
      else:
        print('Cliente %s não está cadastrado!'%cpf)
    else:
      print("Escolha Inválida!")
  elif resp == 4:
    escolha = int(input("Digite 1 para excluir uma fantasia ou 2 para excluir um cliente: "))
    if escolha == 1:
      id = input("Qual o id da fantasia que você deseja excluir? ")
      if id in fantasias:
        print()
        print('ID  :', id)
        print('Nome  :', fantasias[id][0])
        print('Aluguel : R$ %.2f'%fantasias[id][1])
        print('Alugada %d vezes'%fantasias[id][3])
        if fantasias[id][2]:
          print('Status: Fantasia disponível')
        else:
          print('Status: Fantasia não disponível')
        confirma = input("Confirma a exclusão da fantasia (s/n)? ")
        confirma = confirma.lower()
        if confirma == 's':
          del fantasias[id]
          print("Fantasia %s excluída com sucesso"%id)
        else:
          print("Fantasia %s continua no cadastro"%id)
      else:
        print('Fantasia %s não está cadastrada!'%id)
    elif escolha == 2:
      cpf = input("Qual o cpf do cliente que você deseja excluir? ")
      if cpf in clientes:
        print()
        print('CPF  :', cpf)
        print('Nome  :', clientes[cpf][0])
        print('Email  :', clientes[cpf][1])
        print('Telefone  :', clientes[cpf][2])
        print('Deve : R$ %.2f'%clientes[cpf][3])
        print('Alugou %d fantasias'%clientes[cpf][4])
        confirma = input("Confirma a exclusão do cliente (s/n)? ")
        confirma = confirma.lower()
        if confirma == 's':
          del clientes[cpf]
          print("Cliente %s excluído com sucesso"%cpf)
        else:
          print("Cliente %s continua no cadastro"%cpf)
      else:
        print('Cliente %s não está cadastrado!'%cpf)
    else:
      print("Escolha Inválida!")

arqFantasias = open("fantasias.dat", "wb")
pickle.dump(fantasias, arqFantasias)
arqFantasias.close()

arqClientes = open("clientes.dat", "wb")
pickle.dump(clientes, arqClientes)
arqClientes.close()

  