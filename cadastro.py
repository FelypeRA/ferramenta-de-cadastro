import os


def cadastro():
    os.system('clear')
    while True:
        print('-'*30)
        print(f'{"CADASTRO":^30}')
        print('-'*30)
        funcionario = dict()
        funcionario.clear()
        funcionario['nome'] = (str(input('Nome do funcionário: ')))
        funcionario['idade'] = (int(input('Qual a idade: ')))
        funcionario['função'] = (str(input('Qual a função: ')))
        funcionario['CPF'] = (str(input('CPF: ')))
        funcionario['Endereço'] = (str(input('Endereço: ')))
        print(f'{"Funcionario cadastrado com sucesso!":^60}')
        print('---'*20)
        break
    return funcionario


def listar_Funcinarios(funcionarios):
    os.system('clear')
    print('-'* 71)
    print('|ID                 NOME                          FUNÇÃO               |')
    for index,lin in enumerate(funcionarios):
        print(f'|{index:0>2}', end = '        ')
        print(f"{lin['nome']:<30}", end = '')
        print(f"{lin['função']:<30}|", end = '')
        print('') 
    print('-'* 71)

    
def exclui_Funcionario(funcionarios): 
    listar_Funcinarios(funcionarios)
    id = int(input('Digite o ID de quem deseja excluir: '))
    del funcionarios[id]
    
