# Listas para armazenar os dados
mini_goblins = []
caixa_com_furinhos = []
caixas_com_furinhos_fechadas = []
mini_goblins_atendidos = []
total_mini_goblins_aprovados = 0
total_mini_goblins_reprovados = 0

def cadastrar_mini_goblin():
    global total_mini_goblins_aprovados, total_mini_goblins_reprovados, caixa_com_furinhos
    
    print("\n--- CADASTRAR MINIGOBLIN ---")
    
    nome = input("Nome Goblin: ")
    
    print("\nCores de Mini Goblins disponíveis:")
    print("1. Vermelho")
    print("2. Azul") 
    print("3. Verde")
    print("4. Amarelo")
    
    while True:
        opcao = input("Escolha a cor (1-4): ")
        if opcao == '1':
            cor = 'vermelho'
            break
        elif opcao == '2':
            cor = "azul"
            break
        elif opcao == '3':
            cor = "verde"
            break
        elif opcao == '4':
            cor = "amarelo"
            break
        else:
            print("Opção inválida! Escolha 1, 2, 3 ou 4.")
    
    try:
        peso = int(input("Peso (g): "))
        altura = int(input("Altura (cm): "))
    except ValueError:
        print("O valor informado deve ser um número!")
        return
    
    mini_goblin = {
        'id': len(mini_goblins_atendidos) + 1,
        'nome': nome,
        'peso': peso,
        'cor': cor,
        'altura': altura
    }
    
    # Critérios de avaliação
    peso_valido = (mini_goblin['peso'] >= 95 and mini_goblin['peso'] <= 105)
    cor_valida = (mini_goblin['cor'] in ['azul', 'verde'])
    altura_valida = (mini_goblin['altura'] >= 10 and mini_goblin['altura'] <= 20)
        
    if peso_valido and cor_valida and altura_valida:
        mini_goblin['status'] = "Aprovado"
        print("✅ Mini Goblin APROVADO!")
        total_mini_goblins_aprovados += 1
        guardar_mini_goblin_na_caixa_com_furinhos(mini_goblin)
    else:
        mini_goblin['status'] = "Reprovado"
        
        motivo = []
        if not peso_valido:
            motivo.append("Peso fora do padrão (95g-105g)")
        if not cor_valida:
            motivo.append("Cor não é verde nem azul")
        if not altura_valida:
            motivo.append("Altura fora do padrão (10cm-20cm)")
            
        mini_goblin['motivo_reprovacao'] = "; ".join(motivo)
        total_mini_goblins_reprovados += 1
        print("❌ Mini Goblin REPROVADO!")
        
    guardar_log(mini_goblin)
    mini_goblins.append(mini_goblin)

def guardar_mini_goblin_na_caixa_com_furinhos(mini_goblin):
    global caixa_com_furinhos
    
    if len(caixa_com_furinhos) < 10:
        caixa_com_furinhos.append(mini_goblin)
        print(f"📦 Mini Goblin adicionado à caixa com furinhos! ({len(caixa_com_furinhos)}/10)")
    else:
        # Fechar caixa atual e iniciar nova
        caixas_com_furinhos_fechadas.append(caixa_com_furinhos.copy())
        print("🎁 Caixa com furinhos FECHADA e iniciada nova caixa!")
        caixa_com_furinhos = [mini_goblin]
        print(f"📦 Nova caixa iniciada! ({len(caixa_com_furinhos)}/10)")

def guardar_log(mini_goblin):
    mini_goblins_atendidos.append(mini_goblin.copy())

def listar_mini_goblins():
    print("\n--- LISTA DE MINI GOBLINS ATENDIDOS ---")
    if not mini_goblins_atendidos:
        print("Nenhum Mini Goblin foi atendido ainda.")
        return
    
    for goblin in mini_goblins_atendidos:
        status_icon = "✅" if goblin['status'] == "Aprovado" else "❌"
        print(f"{status_icon} ID: {goblin['id']} | Nome: {goblin['nome']} | "
              f"Peso: {goblin['peso']}g | Cor: {goblin['cor']} | "
              f"Altura: {goblin['altura']}cm | Status: {goblin['status']}")
        if goblin['status'] == "Reprovado":
            print(f"   Motivo: {goblin.get('motivo_reprovacao', 'N/A')}")

def remover_mini_goblin():
    print("\n--- REMOVER MINI GOBLIN ---")
    listar_mini_goblins()
    
    if not mini_goblins_atendidos:
        return
    
    try:
        id_remover = int(input("ID do Mini Goblin a remover: "))
        
        for i, goblin in enumerate(mini_goblins_atendidos):
            if goblin['id'] == id_remover:
                # Remover de todas as listas
                mini_goblins_atendidos.pop(i)
                
                # Remover da lista principal
                for j, g in enumerate(mini_goblins):
                    if g['id'] == id_remover:
                        mini_goblins.pop(j)
                        break
                
                # Remover da caixa atual se estiver lá
                for k, g in enumerate(caixa_com_furinhos):
                    if g['id'] == id_remover:
                        caixa_com_furinhos.pop(k)
                        break
                
                print(f"🗑️ Mini Goblin ID {id_remover} removido com sucesso!")
                return
        
        print("Mini Goblin não encontrado!")
    except ValueError:
        print("ID deve ser um número!")

def listar_caixas_com_furinhos():
    print("\n--- CAIXAS COM FURINHOS FECHADAS ---")
    
    if not caixas_com_furinhos_fechadas and not caixa_com_furinhos:
        print("Nenhuma caixa foi fechada ainda.")
        return
    
    # Mostrar caixas fechadas
    for i, caixa in enumerate(caixas_com_furinhos_fechadas, 1):
        print(f"\n📦 CAIXA {i} (FECHADA):")
        for goblin in caixa:
            print(f"   ✅ {goblin['nome']} | Peso: {goblin['peso']}g | Cor: {goblin['cor']} | Altura: {goblin['altura']}cm")
    
    # Mostrar caixa atual
    if caixa_com_furinhos:
        print(f"\n📦 CAIXA ATUAL ({len(caixa_com_furinhos)}/10):")
        for goblin in caixa_com_furinhos:
            print(f"   ✅ {goblin['nome']} | Peso: {goblin['peso']}g | Cor: {goblin['cor']} | Altura: {goblin['altura']}cm")

def gerar_relatorio():
    print("\n" + "="*50)
    print("           RELATÓRIO FINAL - FABRICA DE GOBLINS")
    print("="*50)
    
    # Estatísticas gerais
    print(f"📊 ESTATÍSTICAS GERAIS:")
    print(f"   Total de Mini Goblins atendidos: {len(mini_goblins_atendidos)}")
    print(f"   ✅ Mini Goblins Aprovados: {total_mini_goblins_aprovados}")
    print(f"   ❌ Mini Goblins Reprovados: {total_mini_goblins_reprovados}")
    
    # Caixas utilizadas
    caixas_totais = len(caixas_com_furinhos_fechadas) + (1 if caixa_com_furinhos else 0)
    print(f"\n📦 CAIXAS COM FURINHOS:")
    print(f"   Caixas fechadas: {len(caixas_com_furinhos_fechadas)}")
    print(f"   Caixa atual: {len(caixa_com_furinhos)}/10 Mini Goblins")
    print(f"   Total de caixas utilizadas: {caixas_totais}")
    
    # Análise de reprovações
    if total_mini_goblins_reprovados > 0:
        print(f"\n🔍 ANÁLISE DE REPROVAÇÕES:")
        motivos_reprovacao = {}
        
        for goblin in mini_goblins_atendidos:
            if goblin['status'] == "Reprovado":
                motivo = goblin.get('motivo_reprovacao', 'N/A')
                if motivo in motivos_reprovacao:
                    motivos_reprovacao[motivo] += 1
                else:
                    motivos_reprovacao[motivo] = 1
        
        for motivo, quantidade in motivos_reprovacao.items():
            print(f"   • {motivo}: {quantidade} Mini Goblins")

    
    print("\n" + "="*50)
    print("           !!!!!HAHAHAHAHA - RELATÓRIO CONCLUÍDO!!!!!")
    print("="*50)

def menu():
    while True:
        print("\n" + "="*50)
        print("          SISTEMA DE REGISTRO DE MINI GOBLINS")
        print("               !!!!!HAHAHAHAHA!!!!!")
        print("="*50)
        print("1. Cadastrar novo Mini Goblin")
        print("2. Listar Goblins recebidos")
        print("3. Remover Goblin cadastrado")
        print("4. Listar caixas com furinhos fechadas")
        print("5. Gerar relatório final")
        print("0. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_mini_goblin()
        elif opcao == '2':
            listar_mini_goblins()
        elif opcao == '3':
            remover_mini_goblin()
        elif opcao == '4':
            listar_caixas_com_furinhos()
        elif opcao == '5':
            gerar_relatorio()
        elif opcao == '0':
            print("Saindo do sistema... Até a próxima aventura! 🧙‍♂️")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    menu()