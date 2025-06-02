#NOME: GABRIELA QUEIROGA COCUZZA DA SILVA RM 560035
#NOME: MARIA EDUARDA FERRÉS RM 560418

# Cria um dicionário para armazenar as informações de monitoramento
bueiros = {
    'id': [],
    'localizacao': [],
    'nivel_agua': [],
    'status_tampa': [],
    'obstrucao': [],
    'prioridade': []
}

indices = {bueiros['id'][i] : i for i in range(len(bueiros['id']))}


# Atualiza os indices
def atualiza_indices():
  indices = {bueiros['id'][i] : i for i in range(len(bueiros['id']))}
  return indices


# Função para forçar o usuário a escolher uma opções de uma lista
def forca_opcao(msg, lista_opcoes, msg_erro='Inválido'):
    opcoes = '\n'.join(lista_opcoes)                         # junta as opções em uma string, uma por linha
    opcao = input(f"{msg}\n{opcoes}\n-> ")                   # solicita a escolha do usuário
    while opcao not in lista_opcoes:                          # enquanto a escolha não for válida
        print(msg_erro)                                       # exibe mensagem de erro
        opcao = input(f"{msg}\n{opcoes}\n-> ")               # pede a escolha novamente
    return opcao                                              # retorna a opção válida escolhida

# Função para ver se o número é real
def checa_numero(msg):
    try:
        num = int(input(msg))                                 # tenta converter a entrada para inteiro
        return num
    except ValueError:                                       # erro para se falhar na conversão
        print("Deve ser um número inteiro válido!")
        return checa_numero(msg)                              # chama a função dnv

# Função para cadastrar um novo bueiro
def cadastrar_bueiro():
    try:
        for key in bueiros.keys():                                                                #valida as informaçoes
          if key == 'nivel_agua':
            info = checa_numero(f'Qual o nível da água(cm): ')
          elif key == 'status_tampa':
            info = forca_opcao(f'Qual o status da tampa: ', ['Fechada','Aberta','Quebrada'])
          elif key == 'obstrucao':
            info = forca_opcao(f'Obstrução presente: ', ['Sim','Não'])
          elif key == 'prioridade':
            info = forca_opcao(f'Nível de prioridade: ', ['Baixa', 'Média', 'Alta'])
          else:
            info = input(f"Diga o/a {key}: ")
          bueiros[key].append(info)
        print("Bueiro cadastrado com sucesso!")               # confirma cadastro
    except Exception as e:                                     # erros genéricos
        print(f"Erro ao cadastrar bueiro: {e}")               # exibe mensagem de erro

# Função para atualizar dados de um bueiro
def atualizar_bueiro():
    try:
        if not bueiros['id']:                                # se não tem bueiros cadastrados
            print("Nenhum bueiro cadastrado.")
            return
        bueiro_id = forca_opcao("Informe o ID do bueiro para atualizar:", bueiros['id'])  # pede o ID válido
        indices = atualiza_indices()
        indice_bueiro = indices[bueiro_id]
        for key in bueiros.keys():
            novo = input(f"Novo {key} (enter para não atualizar): ")  # pede novo valor (ou enter para manter)
            if novo:
                if key == 'nivel_agua':                        # se for nível de água, converte para int
                    bueiros[key][indice_bueiro] = int(novo)
                else:
                    bueiros[key][indice_bueiro] = novo               # atualiza o valor

        print("Bueiro atualizado com sucesso!")               # confirma atualização
    except ValueError:
        print("Erro: valor inválido para o nível de água.")  # erro específico para valor inválido no nível
    except Exception as e:
        print(f"Erro ao atualizar bueiro: {e}")              # erro genérico

# Função para remover um bueiro
def remover_bueiro():
    try:
        if not bueiros['id']:                                # verifica se há bueiros cadastrados
            print("Nenhum bueiro cadastrado.")
            return
        bueiro_id = forca_opcao("Informe o ID do bueiro para remover:", bueiros['id'])  # pede ID válido
        indices = atualiza_indices()
        indice_bueiro = indices[bueiro_id]            # pega o índice do bueiro
        for key in bueiros.keys():                   # remove o bueiro em todas as listas
            bueiros[key].pop(indice_bueiro)

        print("Bueiro removido!")                             # confirma remoção
    except ValueError:
        print("Erro: ID não encontrado.")                    # erro caso ID não exista
    except Exception as e:
        print(f"Erro ao remover bueiro: {e}")                # erro genérico

# Função para consultar e mostrar dados de um bueiro
def consultar_bueiro():
    try:
        if not bueiros['id']:                                # verifica se há bueiros cadastrados
            print("Nenhum bueiro cadastrado.")
            return
        bueiro_id = forca_opcao("Informe o ID do bueiro para consultar:", bueiros['id'])  # pede ID válido
        indices = atualiza_indices()
        indice_bueiro = indices[bueiro_id]            # obtém índice do bueiro
        print("\n Dados do bueiro:")
        for key in bueiros.keys():                           # mostra cada campo e seu valor correspondente
            print(f"{key}: {bueiros[key][indice_bueiro]}")
    except ValueError:
        print("Erro: ID não encontrado.")                    # erro caso ID inválido
    except Exception as e:
        print(f"Erro ao consultar bueiro: {e}")              # erro genérico

# Função que gera um relatório listando todos os bueiros que foram cadastrados
def relatorio_bueiros():
    try:
        if not bueiros['id']:                                # verifica se há bueiros cadastrados
            print("Nenhum bueiro cadastrado.")
            return
        print("\n Relatório de todos os bueiros:")
        for i in range(len(bueiros['id'])):                  # para cada bueiro
            print(f"\nBueiro {bueiros['id'][i]}:")
            for key in bueiros.keys():                       # imprime cada campo
                print(f"  {key}: {bueiros[key][i]}")
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")               # erro genérico

# Cria dicionário para acoes que o usuário(técnico) possa fazer
acoes_tecnico = {
    'cadastrar': cadastrar_bueiro,
    'atualizar': atualizar_bueiro,
    'remover': remover_bueiro,
    'consultar': consultar_bueiro,
    'relatorio': relatorio_bueiros
}

# Cria dicionário para acoes que o usuário(cidadão) possa fazer
acoes_cidadao = {
    'consultar': consultar_bueiro
}

# Função principal do sistema
def sistema_bueiros():
    print("Bem-vindo ao Sistema de Monitoramento de Bueiros!")
    
    tipo_usuario = forca_opcao("Qual seu papel?", ['técnico', 'cidadão'])  # pede papel do usuário

    if tipo_usuario == 'técnico':
        while True:                                               # laço para ações do técnico
            acao = forca_opcao("O que deseja fazer?", list(acoes_tecnico.keys()) + ['sair'])
            if acao == 'sair':                                    # sai do perfil técnico
                print("Encerrando perfil técnico.")
                break
            acoes_tecnico[acao]()                                 # executa a ação escolhida
    else:  # Cidadão
        while True:                                               # laço para ações do cidadão
            acao = forca_opcao("O que deseja fazer?", list(acoes_cidadao.keys()) + ['sair'])
            if acao == 'sair':                                    # sai do perfil cidadão
                print("Encerrando perfil cidadão.")
                break
            acoes_cidadao[acao]()                                 # executa a ação escolhida

# Laço principal
# Chama a função principal
# Pergunta se o usuário quer continuar
# Se não, encerra o programa
while True:
    sistema_bueiros()
    continuar = forca_opcao("Deseja continuar no sistema?", ['sim', 'não'])
    if continuar == 'não':
        print(" Sistema finalizado. Até logo!")
        break
