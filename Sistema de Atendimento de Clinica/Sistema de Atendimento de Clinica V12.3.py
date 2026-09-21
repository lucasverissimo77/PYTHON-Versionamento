#Sistema de atendimento de uma clínica
#Feito pelo "Grupo CTRL Z na vida real"/Lucas Verissimo, Kelvens Alves, Bryan Lessa, Yuri Quites e Caio Azevedo
#Versão 12.3

import json
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(BASE_DIR, "agenda.json")
nome_completo = ""
idade = 0
cpf = ""; nome_medico = ""
dia = 0
horario = ""; chave = ""
resposta_marcar_consulta = 0; nivel_risco_atual = 0
paciente_ocupante = ""
nivel_ocupante = 0; dia_novo = 0; 
horario_novo = ""; chave_nova = ""
fila_normal = []; fila_prioridade = []; fila_emergencia = []; pacientes = []

medicos = {
    "Bernardo": {
        "especialidade": "Pediatra",
        "dias": list(range(1, 32)),
        "horarios": [
            "8:00", "9:00", "10:00", "11:00",
            "13:00", "14:00", "15:00", "16:00",
            "17:00", "18:00", "19:00",
        ],
        "agenda": {}
    },
    "João": {
        "especialidade": "Ortopedista",
        "dias": list(range(1, 32)),
        "horarios": [
            "8:00", "9:00", "10:00", "11:00",
            "13:00", "14:00", "15:00", "16:00",
            "17:00", "18:00", "19:00",
        ],
        "agenda": {}
    },
    "Samara": {
        "especialidade": "Ginecologista",
        "dias": list(range(1, 32)),
        "horarios": [
            "8:00", "9:00", "10:00", "11:00",
            "13:00", "14:00", "15:00", "16:00",
            "17:00", "18:00", "19:00",
        ],
        "agenda": {}
    },
    "Agatha": {
        "especialidade": "Cardiologista",
        "dias": list(range(1, 32)),
        "horarios": [
            "8:00", "9:00", "10:00", "11:00",
            "13:00", "14:00", "15:00", "16:00",
            "17:00", "18:00", "19:00",
        ],
        "agenda": {}
    },
    "Pietra": {
        "especialidade": "Clínico Geral",
        "dias": list(range(1, 32)),
        "horarios": [
            "8:00", "9:00", "10:00", "11:00",
            "13:00", "14:00", "15:00", "16:00",
            "17:00", "18:00", "19:00",
        ],
        "agenda": {}
    }
}

qntd_medicos = len(medicos)

nivel_risco = {
    "Sem risco": 1,
    "Prioridade": 2,
    "Emergência": 3
}

nome_fila = {
    1: "Sem risco",
    2: "Prioridade",
    3: "Emergência"
}

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

limpar_tela()

def salvar_dados():
    dados = {
        "medicos": medicos,
        "pacientes": pacientes,
        "fila_normal": fila_normal,
        "fila_prioridade": fila_prioridade,
        "fila_emergencia": fila_emergencia
    }
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print("[Dados salvos no agenda.json]")
    except OSError as erro:
        print(f"[ERRO AO SALVAR] Não foi possível salvar os dados: {erro}")

def carregar_dados():
    global medicos; global pacientes; global fila_normal ;global fila_prioridade; global fila_emergencia

    if not os.path.exists(arquivo):
        return

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        if not isinstance(dados, dict):
            print("O arquivo agenda.json possui formato inválido.")
            return

        medicos_salvos = dados.get("medicos", {})
        if isinstance(medicos_salvos, dict):
            for nome, dados_medico in medicos.items():
                if nome in medicos_salvos and isinstance(medicos_salvos[nome], dict):
                    dados_antigos = medicos_salvos[nome]
                    dados_medico["especialidade"] = dados_antigos.get("especialidade", dados_medico["especialidade"])
                    dados_medico["dias"] = dados_antigos.get("dias", list(range(1, 32)))
                    dados_medico["horarios"] = dados_antigos.get("horarios", dados_medico["horarios"])
                    dados_medico["agenda"] = dados_antigos.get("agenda", {})
                    if not isinstance(dados_medico["agenda"], dict):
                        dados_medico["agenda"] = {}

        pacientes_salvos = dados.get("pacientes", [])
        if isinstance(pacientes_salvos, list):
            pacientes = pacientes_salvos

        fila_normal_salva = dados.get("fila_normal", [])
        fila_prioridade_salva = dados.get("fila_prioridade", [])
        fila_emergencia_salva = dados.get("fila_emergencia", [])

        if isinstance(fila_normal_salva, list):
            fila_normal = fila_normal_salva
        if isinstance(fila_prioridade_salva, list):
            fila_prioridade = fila_prioridade_salva
        if isinstance(fila_emergencia_salva, list):
            fila_emergencia = fila_emergencia_salva

        print("[Dados carregados do agenda.json]")
    except json.JSONDecodeError:
        print("O arquivo agenda.json está indisponível ou corrompido.")
        print("O sistema continuará com os dados padrão.")
    except OSError as erro:
        print(f"Não foi possível abrir o agenda.json: {erro}")

def obter_nivel_por_paciente():
    global paciente_ocupante
    global nivel_ocupante

    nome_paciente = paciente_ocupante.get("nome") if isinstance(paciente_ocupante, dict) else paciente_ocupante
    nivel_ocupante = 1

    if any(p.get("nome") == nome_paciente for p in fila_emergencia):
        nivel_ocupante = 3
    elif any(p.get("nome") == nome_paciente for p in fila_prioridade):
        nivel_ocupante = 2
    elif any(p.get("nome") == nome_paciente for p in fila_normal):
        nivel_ocupante = 1

    return nivel_ocupante

def nome_risco():
    global nivel_risco_atual
    if nivel_risco_atual == 3:
        return "Emergência"
    elif nivel_risco_atual == 2:
        return "Prioridade"
    else:
        return "Sem risco"

def nome_risco_ocupante():
    global nivel_ocupante
    if nivel_ocupante == 3:
        return "Emergência"
    elif nivel_ocupante == 2:
        return "Prioridade"
    else:
        return "Sem risco"

def remover_das_filas():
    global paciente_ocupante

    for fila in (fila_normal, fila_prioridade, fila_emergencia):
        fila[:] = [p for p in fila if p.get("cpf") != cpf]

def remover_nome_das_filas(nome_paciente):
    paciente = nome_paciente.get("nome") if isinstance(nome_paciente, dict) else nome_paciente
    cpf_paciente = nome_paciente.get("cpf") if isinstance(nome_paciente, dict) else None

    for fila in (fila_normal, fila_prioridade, fila_emergencia):
        if cpf_paciente is not None:
            fila[:] = [p for p in fila if p.get("cpf") != cpf_paciente]
        else:
            fila[:] = [p for p in fila if p.get("nome") != paciente]

def adicionar_na_fila():
    global paciente_ocupante

    remover_das_filas()

    paciente = {
        "nome": nome_completo,
        "cpf": cpf
    }

    if nivel_risco_atual == 3:
        if not any(p.get("cpf") == cpf for p in fila_emergencia):
            fila_emergencia.append(paciente)
    elif nivel_risco_atual == 2:
        if not any(p.get("cpf") == cpf for p in fila_prioridade):
            fila_prioridade.append(paciente)
    elif nivel_risco_atual == 1:
        if not any(p.get("cpf") == cpf for p in fila_normal):
            fila_normal.append(paciente)

def adicionar_paciente_fila_por_risco(nome_paciente, risco):
    paciente = nome_paciente.get("nome") if isinstance(nome_paciente, dict) else nome_paciente
    cpf_paciente = nome_paciente.get("cpf") if isinstance(nome_paciente, dict) else None

    if cpf_paciente is not None:
        remover_nome_das_filas(nome_paciente)
    else:
        remover_nome_das_filas({"nome": paciente, "cpf": None})

    paciente_dict = {
        "nome": paciente,
        "cpf": cpf_paciente
    }

    if risco == 3:
        fila_emergencia.append(paciente_dict)
    elif risco == 2:
        fila_prioridade.append(paciente_dict)
    else:
        fila_normal.append(paciente_dict)

def paciente_tem_outra_consulta(nome_paciente):
    nome = nome_paciente.get("nome") if isinstance(nome_paciente, dict) else nome_paciente
    cpf_paciente = nome_paciente.get("cpf") if isinstance(nome_paciente, dict) else None

    for medico in medicos.values():
        for paciente_agendado in medico["agenda"].values():
            if isinstance(paciente_agendado, dict):
                if cpf_paciente is not None:
                    if paciente_agendado.get("cpf") == cpf_paciente and paciente_agendado.get("cpf") != "":
                        return True
                if paciente_agendado.get("nome") == nome:
                    return True
            elif paciente_agendado == nome:
                return True
    return False

def buscar_vaga_mais_proxima():
    global dia_novo; global horario_novo; global chave_nova; global dia

    encontrou_vaga = False
    for dia_novo in range(dia, 32):
        if dia_novo not in medicos[nome_medico]["dias"]:
            continue
        for horario_novo in medicos[nome_medico]["horarios"]:
            chave_nova = f"{dia_novo}|{horario_novo}"
            if chave_nova not in medicos[nome_medico]["agenda"]:
                encontrou_vaga = True
                break
        if encontrou_vaga:
            break

    if not encontrou_vaga:
        for dia_novo in range(1, dia):
            if dia_novo not in medicos[nome_medico]["dias"]:
                continue
            for horario_novo in medicos[nome_medico]["horarios"]:
                chave_nova = f"{dia_novo}|{horario_novo}"
                if chave_nova not in medicos[nome_medico]["agenda"]:
                    encontrou_vaga = True
                    break
            if encontrou_vaga:
                break

    if encontrou_vaga:
        return True

    print("Não existe outro horário disponível para este paciente.")
    return False

def fila_atendimento():
    global resposta_marcar_consulta

    while True:
        limpar_tela()
        print("===> Fila De Atendimento <===\n")
        print("Opção 0: Sair")
        print("Opção 1: Fila de Atendimento Normal")
        print("Opção 2: Fila de Atendimento Prioridade")
        print("Opção 3: Fila de Atendimento Emergência\n")

        try:
            resposta_fila = int(input("Escolha uma Opção (0-3):\n>  "))
        except ValueError:
            print("O valor inserido não é válido!")
            time.sleep(2)
            continue

        if resposta_fila == 1:
            print(f"O atendimento da fila sem risco é de {len(fila_normal)} pessoas")
        elif resposta_fila == 2:
            print(f"O atendimento da fila prioritária é de {len(fila_prioridade)} pessoas")
        elif resposta_fila == 3:
            print(f"O atendimento da fila de emergência é de {len(fila_emergencia)} pessoas")
        elif resposta_fila == 0:
            main()
        else:
            print("Fila de atendimento não encontrada!")
            time.sleep(2)
            continue

        input("Aperte Enter para sair:\n>  ")
        principal()

def cancelar_consulta():
    global nome_medico; global dia; global horario; global chave; global paciente_ocupante

    limpar_tela()
    print("\n=====================")
    print("-->Cancelar Consulta<--")
    print("=====================")

    nome_medico = input("Qual o médico ao qual você quer cancelar a consulta? (Bernardo, João, Samara...)\n>  ").strip()
    if nome_medico not in medicos:
        print("Médico não encontrado!")
        time.sleep(2)
        principal()

    try:
        dia = int(input("Dia da consulta para cancelar:\n>  "))
        if dia not in medicos[nome_medico]["dias"]:
            print("Dia inválido!")
            time.sleep(2)
            principal()

        horario = input("Horário (ex: 9:00):\n>  ").strip()
        if horario not in medicos[nome_medico]["horarios"]:
            print("Horário inválido!")
            time.sleep(2)
            principal()

        chave = f"{dia}|{horario}"
        if chave not in medicos[nome_medico]["agenda"]:
            print(f"Não achei consulta dia {dia} às {horario} com {nome_medico}")
            time.sleep(3)
            principal()

        paciente = medicos[nome_medico]["agenda"][chave]
        paciente_nome = paciente.get("nome") if isinstance(paciente, dict) else paciente
        paciente_cpf = paciente.get("cpf") if isinstance(paciente, dict) else None

        if isinstance(paciente, dict):
            if paciente.get("cpf") != cpf:
                print("Essa consulta não pertence ao seu cadastro!")
                time.sleep(2.5)
                principal()
        else:
            if paciente != nome_completo:
                print("Essa consulta não pertence ao seu cadastro!")
                time.sleep(2.5)
                principal()

        print(f"\nEncontrado: {paciente_nome} com Dr.{nome_medico} dia {dia} às {horario}")

        confirmacao = input("Tem certeza que quer cancelar a sua consulta?\n>  ").strip().lower()
        if confirmacao not in ("s", "sim"):
            print("Cancelamento abortado.")
            input("Aperte Enter para sair\n>  ")
            main()

        del medicos[nome_medico]["agenda"][chave]

        if not paciente_tem_outra_consulta({"nome": paciente_nome, "cpf": paciente_cpf}):
            remover_nome_das_filas({"nome": paciente_nome, "cpf": paciente_cpf})

        salvar_dados()
        print(f"Consulta de {paciente_nome} cancelada! Horário {dia} {horario} liberado.")
        input("Aperte Enter para sair\n>  ")
    except ValueError:
        print("Dia inválido!")
        time.sleep(2)
        principal()

def remarcar_consulta():
    global nome_medico; global dia; global horario; global chave; global dia_novo; global horario_novo
    global chave_nova; global paciente_ocupante; global nivel_ocupante; global nivel_risco_atual
    limpar_tela()
    print("\n=====================")
    print("-->Remarcar Consulta<--")
    print("=====================")
    print(f"Olá {nome_completo}! Qual o nome do médico que iria te atender? (Bernardo, Samara, João...)")

    nome_medico = input(">  ").strip()
    if nome_medico not in medicos:
        print("Médico não encontrado!")
        time.sleep(2)
        principal()

    try:
        print("\n-- Consulta ANTIGA --")
        dia = int(input("Dia Antigo:\n>  "))
        horario = input("Horário antigo (ex: 9:00):\n>  ").strip()

        if dia not in medicos[nome_medico]["dias"]:
            print("Dia antigo inválido!")
            time.sleep(2)
            principal()

        if horario not in medicos[nome_medico]["horarios"]:
            print("Horário antigo inválido!")
            time.sleep(2)
            principal()

        chave = f"{dia}|{horario}"
        if chave not in medicos[nome_medico]["agenda"]:
            print(f"Não achei consulta com {nome_medico} dia {dia} às {horario}")
            time.sleep(2)
            principal()

        paciente = medicos[nome_medico]["agenda"][chave]
        paciente_nome = paciente.get("nome") if isinstance(paciente, dict) else paciente
        paciente_cpf = paciente.get("cpf") if isinstance(paciente, dict) else None

        if isinstance(paciente, dict):
            if paciente.get("cpf") != cpf:
                print("Essa consulta não pertence ao seu cadastro!")
                time.sleep(2.5)
                principal()
        else:
            if paciente != nome_completo:
                print("Essa consulta não pertence ao seu cadastro!")
                time.sleep(2.5)
                principal()

        paciente_ocupante = paciente
        obter_nivel_por_paciente()
        nivel_risco_atual = nivel_ocupante
        risco_paciente = nivel_risco_atual

        print(f"Encontrei: {paciente_nome} com {nome_medico}")
        time.sleep(1)
        limpar_tela()

        print("---Consulta NOVA---")
        print(f"Dias disponíveis: {medicos[nome_medico]['dias']}")
        print(f"Horários disponíveis: {medicos[nome_medico]['horarios']}")

        dia_novo = int(input("Novo dia:\n>  "))
        horario_novo = input("Novo horário:\n>  ").strip()
        chave_nova = f"{dia_novo}|{horario_novo}"

        if dia_novo not in medicos[nome_medico]["dias"]:
            print("Esse médico não atende neste dia novo!")
            time.sleep(2)
            principal()

        if horario_novo not in medicos[nome_medico]["horarios"]:
            print("Horário novo inválido!")
            time.sleep(2)
            principal()

        if chave_nova == chave:
            print("A nova consulta é igual à consulta atual!")
            time.sleep(2)
            principal()

        if chave_nova not in medicos[nome_medico]["agenda"]:
            del medicos[nome_medico]["agenda"][chave]
            medicos[nome_medico]["agenda"][chave_nova] = {
                "nome": paciente_nome,
                "cpf": paciente_cpf
            }
            salvar_dados()
            print("\nRemarcado com sucesso!")
            print(f"{paciente_nome} foi de {dia} {horario} --> {dia_novo} {horario_novo} com o Dr.{nome_medico}")
            input("Aperte Enter para sair")
            main()

        paciente_ocupante = medicos[nome_medico]["agenda"][chave_nova]
        paciente_ocupante_nome = paciente_ocupante.get("nome") if isinstance(paciente_ocupante, dict) else paciente_ocupante
        paciente_ocupante_cpf = paciente_ocupante.get("cpf") if isinstance(paciente_ocupante, dict) else None

        if isinstance(paciente_ocupante, dict):
            if any(p.get("cpf") == paciente_ocupante_cpf for p in fila_emergencia):
                nivel_ocupante = 3
            elif any(p.get("cpf") == paciente_ocupante_cpf for p in fila_prioridade):
                nivel_ocupante = 2
            else:
                nivel_ocupante = 1
        else:
            if paciente_ocupante in fila_emergencia:
                nivel_ocupante = 3
            elif paciente_ocupante in fila_prioridade:
                nivel_ocupante = 2
            else:
                nivel_ocupante = 1

        print(f"\nEsse horário já está ocupado por: {paciente_ocupante_nome}")
        print(f"Situação do paciente atual: {nome_risco_ocupante()}")

        if risco_paciente > nivel_ocupante:
            print("\nA nova consulta possui prioridade maior!")
            print(f"{paciente_ocupante_nome} será direcionado para o horário mais próximo disponível")

            del medicos[nome_medico]["agenda"][chave]
            chave_ocupada = chave_nova
            dia = dia_novo
            encontrou_vaga = False

            for dia_teste in range(dia, 32):
                if dia_teste not in medicos[nome_medico]["dias"]:
                    continue
                for horario_teste in medicos[nome_medico]["horarios"]:
                    chave_teste = f"{dia_teste}|{horario_teste}"
                    if chave_teste not in medicos[nome_medico]["agenda"] and chave_teste != chave_ocupada:
                        dia_novo = dia_teste
                        horario_novo = horario_teste
                        chave_nova = chave_teste
                        encontrou_vaga = True
                        break
                if encontrou_vaga:
                    break

            if not encontrou_vaga:
                for dia_teste in range(1, dia):
                    if dia_teste not in medicos[nome_medico]["dias"]:
                        continue
                    for horario_teste in medicos[nome_medico]["horarios"]:
                        chave_teste = f"{dia_teste}|{horario_teste}"
                        if chave_teste not in medicos[nome_medico]["agenda"] and chave_teste != chave_ocupada:
                            dia_novo = dia_teste
                            horario_novo = horario_teste
                            chave_nova = chave_teste
                            encontrou_vaga = True
                            break
                    if encontrou_vaga:
                        break

            if encontrou_vaga:
                medicos[nome_medico]["agenda"][chave_nova] = {
                    "nome": paciente_ocupante_nome,
                    "cpf": paciente_ocupante_cpf
                }
                medicos[nome_medico]["agenda"][chave_ocupada] = {
                    "nome": paciente_nome,
                    "cpf": paciente_cpf
                }

                adicionar_paciente_fila_por_risco({"nome": paciente_nome, "cpf": paciente_cpf}, risco_paciente)
                adicionar_paciente_fila_por_risco({"nome": paciente_ocupante_nome, "cpf": paciente_ocupante_cpf}, nivel_ocupante)

                salvar_dados()
                print("\n========================================")
                print("      CONSULTA REORGANIZADA")
                print("========================================")
                print(f"Paciente: {paciente_nome}")
                print(f"Risco: {nome_risco()}")
                print(f"Consulta: Dia {dia_novo} às {horario_novo}")
                print("\nPaciente Deslocado:")
                print(paciente_ocupante_nome)
                print(f"Novo horário: dia {dia_novo} às {horario_novo}")
                print("\nTudo foi reorganizado com sucesso!")
            else:
                medicos[nome_medico]["agenda"][chave] = {
                    "nome": paciente_nome,
                    "cpf": paciente_cpf
                }
                print("Não foi possível encontrar uma vaga para reorganizar as consultas.")
        else:
            print("\nEsse horário pertence a uma pessoa com prioridade igual ou maior!")
            print("Vamos procurar o horário mais próximo disponível!")
            del medicos[nome_medico]["agenda"][chave]

            dia = dia_novo
            if buscar_vaga_mais_proxima():
                medicos[nome_medico]["agenda"][chave_nova] = {
                    "nome": paciente_nome,
                    "cpf": paciente_cpf
                }
                adicionar_paciente_fila_por_risco({"nome": paciente_nome, "cpf": paciente_cpf}, risco_paciente)
                salvar_dados()
                print(f"Remarcado para o horário mais próximo disponível: dia {dia_novo} às {horario_novo}.")
            else:
                medicos[nome_medico]["agenda"][chave] = {
                    "nome": paciente_nome,
                    "cpf": paciente_cpf
                }
                print("Não foi possível encontrar uma nova vaga. Sua consulta antiga foi mantida.")

        input("Aperte Enter para sair")
    except ValueError:
        print("A sua resposta é inválida (digite o dia em número). Tente novamente...")
        time.sleep(2.5)
        principal()

def marcar_consulta():
    global nome_medico; global dia; global horario; global chave; global resposta_marcar_consulta; global nivel_risco_atual
    global paciente_ocupante; global nivel_ocupante; global dia_novo; global horario_novo; global chave_nova

    limpar_tela()
    print("\n=====================")
    print("-->Marcar Consulta<--")
    print("=====================")

    if not nome_completo:
        print("Você precisa fazer login ou cadastro antes de marcar uma consulta.")
        time.sleep(2)
        main()

    if paciente_tem_outra_consulta(nome_completo):
        print("Você já possui outra consulta marcada. Remarque ou cancele antes de agendar uma nova.")
        time.sleep(2.5)
        principal()

    print(f"Olá {nome_completo}! Primeiramente precisamos saber qual a situação de risco do(a) senhor(a)")
    print("\nOpção 1: Sem risco")
    print("Opção 2: Prioridade")
    print("Opção 3: Emergência")
    print("Opção 0: Sair")

    try:
        resposta_marcar_consulta = int(input(">  "))
        if resposta_marcar_consulta == 0:
            main()
        if resposta_marcar_consulta not in [1, 2, 3]:
            print("Opção inválida, tente novamente mais tarde!")
            time.sleep(2.5)
            principal()

        nivel_risco_atual = resposta_marcar_consulta

        print("\nMédicos disponíveis:")
        for medico, dados in medicos.items():
            print(f"- {medico} — {dados['especialidade']}")

        nome_medico = input("Digite o nome do médico:\n>  ").strip()
        if nome_medico not in medicos:
            print("Médico não encontrado!")
            time.sleep(2)
            principal()

        print(f"Dias disponíveis: {medicos[nome_medico]['dias']}")

        try:
            dia = int(input("Escolha o dia:\n>  "))
        except ValueError:
            print("Digite o dia usando apenas números.")
            time.sleep(2)
            principal

        if dia not in medicos[nome_medico]["dias"]:
            print("Esse médico não atende neste dia!")
            time.sleep(2)
            principal()

        print(f"Horários disponíveis: {medicos[nome_medico]['horarios']}")

        horario = input("Escolha o horário (ex: 8:00):\n>  ").strip()
        if horario not in medicos[nome_medico]["horarios"]:
            print("Horário inválido!")
            time.sleep(2)
            principal()

        chave = f"{dia}|{horario}"
        if chave not in medicos[nome_medico]["agenda"]:
            medicos[nome_medico]["agenda"][chave] = {
                "nome": nome_completo,
                "cpf": cpf
            }
            paciente_ocupante = nome_completo
            adicionar_na_fila()
            salvar_dados()
            print(f"Consulta marcada como {nome_risco()} com {nome_medico} dia {dia} às {horario}")
            input("Aperte Enter para sair:\n>  ")
            time.sleep(2.5)
            main()

        paciente_ocupante = medicos[nome_medico]["agenda"][chave]
        paciente_ocupante_nome = paciente_ocupante.get("nome") if isinstance(paciente_ocupante, dict) else paciente_ocupante
        paciente_ocupante_cpf = paciente_ocupante.get("cpf") if isinstance(paciente_ocupante, dict) else None

        if isinstance(paciente_ocupante, dict):
            if any(p.get("cpf") == paciente_ocupante_cpf for p in fila_emergencia):
                nivel_ocupante = 3
            elif any(p.get("cpf") == paciente_ocupante_cpf for p in fila_prioridade):
                nivel_ocupante = 2
            else:
                nivel_ocupante = 1
        else:
            if paciente_ocupante in fila_emergencia:
                nivel_ocupante = 3
            elif paciente_ocupante in fila_prioridade:
                nivel_ocupante = 2
            else:
                nivel_ocupante = 1

        print(f"\nEsse horário já está ocupado por: {paciente_ocupante_nome}")
        print(f"Situação do paciente atual: {nome_risco_ocupante()}")

        if nivel_risco_atual > nivel_ocupante:
            print("\nA nova consulta possui prioridade maior!")
            print(f"{paciente_ocupante_nome} será direcionado para o horário mais próximo disponível")

            paciente_antigo = paciente_ocupante_nome
            risco_antigo = nivel_ocupante
            dia_novo = dia
            encontrou_vaga = False

            for dia_teste in range(dia, 32):
                if dia_teste not in medicos[nome_medico]["dias"]:
                    continue
                for horario_teste in medicos[nome_medico]["horarios"]:
                    chave_teste = f"{dia_teste}|{horario_teste}"
                    if chave_teste not in medicos[nome_medico]["agenda"] and chave_teste != chave:
                        dia_novo = dia_teste
                        horario_novo = horario_teste
                        chave_nova = chave_teste
                        encontrou_vaga = True
                        break
                if encontrou_vaga:
                    break

            if not encontrou_vaga:
                for dia_teste in range(1, dia):
                    if dia_teste not in medicos[nome_medico]["dias"]:
                        continue
                    for horario_teste in medicos[nome_medico]["horarios"]:
                        chave_teste = f"{dia_teste}|{horario_teste}"
                        if chave_teste not in medicos[nome_medico]["agenda"] and chave_teste != chave:
                            dia_novo = dia_teste
                            horario_novo = horario_teste
                            chave_nova = chave_teste
                            encontrou_vaga = True
                            break
                    if encontrou_vaga:
                        break

            if encontrou_vaga:
                del medicos[nome_medico]["agenda"][chave]
                medicos[nome_medico]["agenda"][chave_nova] = {
                    "nome": paciente_antigo,
                    "cpf": paciente_ocupante_cpf
                }
                medicos[nome_medico]["agenda"][chave] = {
                    "nome": nome_completo,
                    "cpf": cpf
                }

                adicionar_paciente_fila_por_risco({"nome": paciente_antigo, "cpf": paciente_ocupante_cpf}, risco_antigo)
                adicionar_paciente_fila_por_risco({"nome": nome_completo, "cpf": cpf}, nivel_risco_atual)

                salvar_dados()
                print("\n========================================")
                print("      CONSULTA REORGANIZADA")
                print("========================================")
                print("Paciente:")
                print(nome_completo)
                print(f"Risco: {nome_risco()}")
                print(f"Consulta: Dia {dia} às {horario}")
                print("\nPaciente Deslocado:")
                print(paciente_antigo)
                print(f"Novo horário: dia {dia_novo} às {horario_novo}")
                print("\nTudo foi reorganizado com sucesso!")
            else:
                print("\nNão foi possível encontrar uma vaga para reorganizar.")
        else:
            print("\nEsse horário pertence a uma pessoa com prioridade igual ou maior!")
            print("Vamos procurar o horário mais próximo disponível!")

            if buscar_vaga_mais_proxima():
                if chave_nova == chave:
                    print("Não foi possível encontrar uma vaga diferente.")
                else:
                    medicos[nome_medico]["agenda"][chave_nova] = {
                        "nome": nome_completo,
                        "cpf": cpf
                    }
                    adicionar_paciente_fila_por_risco({"nome": nome_completo, "cpf": cpf}, nivel_risco_atual)
                    salvar_dados()
                    print(f"Consulta marcada para o horário mais próximo disponível: dia {dia_novo} às {horario_novo}.")
            else:
                print("Não foi possível encontrar uma vaga para a nova consulta.")

        print("\nAperte Enter para sair:")
        input(">  ")
    except ValueError:
        print("O valor inserido não é válido.")
        print("Redirecionando de volta ao início...")
        time.sleep(2.5)
        principal()

def especialistas():
    limpar_tela()
    print("===========================")
    print("---Nossos Especialistas---")
    print("===========================")

    for medico, dados in medicos.items():
        print(f"Médico: {medico}        Especialidade: {dados['especialidade']}")
        print("---------------------------------------------------------")

    print("Aperte Enter para voltar ao menu inicial")
    input(">  ")
    principal()

def principal():
    global nome_completo

    while True:
        limpar_tela()
        print("---> Sistema de Pacientes <---\n")
        print("Opção 1: Marcar Consulta")
        print("Opção 2: Remarcar Consulta")
        print("Opção 3: Cancelar Consulta")
        print("Opção 4: Nossos Especialistas")
        print("Opção 5: Fila de Atendimento")
        print("Opção 0: Sair")
        print(f"Olá o senhor(a) {nome_completo} Precisa escolher uma Opção (0-5):")

        try:
            resposta_opcoes = int(input(">  "))
        except ValueError:
            print("O valor inserido não é válido.")
            time.sleep(2)
            continue

        if resposta_opcoes == 1:
            marcar_consulta()
        elif resposta_opcoes == 2:
            remarcar_consulta()
        elif resposta_opcoes == 3:
            cancelar_consulta()
        elif resposta_opcoes == 4:
            especialistas()
        elif resposta_opcoes == 5:
            fila_atendimento()
        elif resposta_opcoes == 0:
            main()
        else:
            print("Opção inválida!")
            time.sleep(2)

def logar():
    global nome_completo; global idade; global cpf

    limpar_tela()
    print("---Sistema de Login---\n")
    print("Para fazer login precisamos do seu nome/segundo nome/senha(CPF)/idade.")
    print("Digite seu primeiro e segundo nome")
    resposta_nome_completo = input(">  ").strip()

    print("Digite sua idade")
    try:
        resposta_idade = int(input(">  "))
    except ValueError:
        print("A idade deve ser um número.")
        time.sleep(2.5)
        logar()

    print("Digite a senha que você cadastrou (CPF)")
    resposta_senha = input(">  ").strip()
    print("\nVerificando...")
    time.sleep(1)

    for paciente in pacientes:
        if not isinstance(paciente, dict):
            continue
        if (
            paciente.get("nome") == resposta_nome_completo
            and paciente.get("idade") == resposta_idade
            and paciente.get("cpf") == resposta_senha
        ):
            nome_completo = paciente["nome"]
            idade = paciente["idade"]
            cpf = paciente["cpf"]
            print("Login realizado com sucesso!")
            print("Redirecionando você para nosso sistema de Pacientes")
            time.sleep(2)
            principal()
            return

    print("A sua resposta não corresponde aos dados reais, tente novamente ou contate o suporte.")
    input("Aperte Enter para voltar")

def cadastrar():
    global idade; global cpf; global nome_completo

    limpar_tela()
    print("---Sistema de Cadastro---")
    print("Digite Seu Primeiro nome:")
    nome = input(">  ").strip()

    print("Digite seu Segundo nome:")
    segundo_nome = input(">  ").strip()

    print("Digite Seu CPF, ele será usado como senha:")
    cpf_novo = input(">  ").strip()

    if nome == "" or segundo_nome == "":
        print("O nome e o segundo nome não podem ficar vazios.")
        time.sleep(2)
        cadastrar()

    if cpf_novo == "":
        print("O CPF não pode ficar vazio.")
        time.sleep(2)
        cadastrar()

    for paciente in pacientes:
        if isinstance(paciente, dict) and paciente.get("cpf") == cpf_novo:
            print("Esse CPF já está cadastrado.")
            time.sleep(2)
            cadastrar()

    print("Digite sua idade")
    try:
        idade = int(input(">  "))
    except ValueError:
        print("Digite apenas números para a idade.")
        time.sleep(2.5)
        logar()

    if idade < 0 or idade > 120:
        print("Digite uma idade válida entre 0 e 120.")
        time.sleep(2.5)
        logar()

    nome_completo = nome + " " + segundo_nome
    cpf = cpf_novo

    print("Seus Dados estão corretos?")
    print(f"--> Nome Completo: {nome_completo}")
    print(f"--> Idade: {idade}")
    resposta_cadastro = input(">  ").strip().lower()

    if resposta_cadastro in ("sim", "s"):
        print(f"Sua senha é {cpf} guarde ela para logar quando precisar.")
        print("Redirecionando para nosso sistema de Pacientes...")
        pacientes.append({
            "nome": nome_completo,
            "idade": idade,
            "cpf": cpf
        })
        salvar_dados()
        time.sleep(3)
        principal()
        return
    elif resposta_cadastro in ("nao", "não", "n"):
        print("Cadastro cancelado.")
        time.sleep(2)
        return
    else:
        print("A sua resposta é inválida.")
        time.sleep(2)
        return

def main():
    global idade; global cpf; global nome_completo

    carregar_dados()
    limpar_tela()
    print("\n=======================")
    print("     Clínica Vida+")
    print("=======================\n")
    print("Olá seja bem vindo ao nosso Sistema da Clínica Vida+")
    print("O Senhor(a) possui cadastro em nosso sistema?")

    while True:
        resposta_inicial = input(">  ").strip().lower()
        if resposta_inicial in ("sim", "s"):
            print("Faça seu Login em Nosso Sistema!")
            print("Redirecionando...")
            time.sleep(2.5)
            logar()
            break
        elif resposta_inicial in ("nao", "não", "n"):
            print("Faça seu cadastro pelo nosso Sistema!")
            print("Redirecionando...")
            time.sleep(2.5)
            cadastrar()
            break
        else:
            print("A sua resposta é inválida.")
            time.sleep(2)

if __name__ == "__main__":
    main()