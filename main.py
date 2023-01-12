import os

# fazer aparecer o menu na tela  
def menu():
  global opção
  print('-'*60)
  print(f'{"ferramenta para cadastro de funcionarios":^60}')
  print('-'*60)
  print('         [ 1 ] Para cadastrar um funcionário. ')
  print('         [ 2 ] Para ver lista de funcionários.')
  print('         [ 3 ] Para excluir um funcionario.   ')
  print('         [ 4 ] Sair do programa.              ')
  print('-' * 60)

  

# Função para cadastrar um funcionario na lista 
def cadastro():
  os.system('clear')
  while True:
    print('-'*30)
    print(f'{"CADASTRO":^30}')
    print('-'*30)

    funcionario.append(str(input('Nome do funcionário: ')))
    funcionario.append(int(input('Qual a idade: ')))
    funcionario.append(str(input('Qual a função: ')))
    funcionario.append(str(input('CPF: ')))
    funcionario.append(str(input('Endereço: ')))
      
    funcionarios.append(funcionario[:])
    funcionario.clear()
    print(f'{"Funcionario cadastrado com sucesso!":^60}')
    print('---'*20)
    
    continuar = str(input('Fazer novo cadastro? '))
    if continuar in 'Nn':
      break


# Função que lista os funcionarios 
def listarfuncinarios(): 
  print('')

# Excluir funcionario da lista
def excluifuncionario(): 
  print('')



funcionarios = []
funcionario = []
cont = 0 
opção = 0
continuar = ''

while True: 
  menu()
  opção = int(input('Sua opção: '))
  if opção == 1:
    cadastro()
  elif opção == 2:
    listarfuncinarios()
  elif opção == 3:
    excluifuncionario()
  elif opção == 4:
    break
for index,item in enumerate(funcionarios):
  print(item)

