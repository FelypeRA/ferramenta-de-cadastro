import os
from cadastro import cadastro,listar_Funcinarios,exclui_Funcionario
from menu import menu


funcionarios = []
cont = 0 
continuar = ''

while True: 
    menu()
    opcao = int(input('Sua opção: '))
    os.system('clear')
  
    #Fazer novo cadastro de funcionario. 
    if opcao == 1:
        funcionarios.append(cadastro())
        os.system('clear')
        continuar = str(input('Fazer novo cadastro? '))
        while continuar in 'sS':
            funcionarios.append(cadastro())
            continuar = str(input('Fazer novo cadastro? '))
        if continuar == 'Nn':
            break
        os.system('clear')
      
    #Listar funcionarios e ver mais informaçoes. Digitando o id do funcionario aparece as informaçoes detalhadas
    elif opcao == 2:
        listar_Funcinarios(funcionarios)
        id = int(input('Digite o ID do funcionário para mais informaçoes[-1 para voltar ao menu principal]: '))
        if id == -1:
            os.system('clear')
            continue
        else:
            for key,item in funcionarios[id].items():
                print(f'{key}: {item}')
            print('')
            input('Precione qualquer tecla para voltar ao menu principal: ')
        os.system('clear')
    #Deletar um registro.
    elif opcao == 3:
        exclui_Funcionario(funcionarios)

    #Sair do programa  
    elif opcao == 4:
        break
      



 


