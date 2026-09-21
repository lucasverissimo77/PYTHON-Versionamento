#Sistema de atendimento de uma clínica
#Feito pelo "Grupo CTRL Z na vida real"/Lucas Verissimo, Kelvens Alves, Bryan Lessa, Yuri Quites e Caio Azevedo
#Versão 8.0

import json
import os
import time


arquivo = "agenda.json"

nome_completo = ""
idade = 0
cpf = ""

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()

fila_normal  = []
fila_prioridade = []
fila_emergencia = []

pacientes = []
medicos = {
    "Bernado" : {
    "especialidade" : "Pediatra",
    "dias" : list(range(1, 32)),
    "horarios" : ["8:00", "9:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "agenda": {}
    },
    "João" : {
    "especialidade" : "Ortopedista",
    "dias" : list(range(1, 32)),
    "horarios" : ["8:00", "9:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "agenda": {}
    },
    "Samara" : {
    "especialidade" : "Ginecologista",
    "dias" : list(range(1, 32)),
    "horarios" : ["8:00", "9:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "agenda": {}
    },
    "Agatha" : {
    "especialidade" : "Cardiologista",
    "dias" : list(range(1, 32)),
    "horarios" : ["8:00", "9:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "agenda": {}
    },
    "Pietra" : {
    "especialidade" : "Clínico Geral",
    "dias" : list(range(1, 32)),
    "horarios" : ["8:00", "9:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "agenda": {}
    }
}

qntd_medicos = len(medicos)

nivel_rico = {
    "Sem risco" : 1,
    "Prioridade" : 2,
    "Emergência" : 3
}

nome_fila = {
    1: "Sem risco",
    2: "Prioridade",
    3: "Emergência"
}

def salvar_dados():
    dados = {
    "medicos" : medicos,
    "pacientes" : pacientes,
    "fila_normal": fila_normal,
    "fila_prioridade" : fila_prioridade,
    "fila_emergencia" : fila_emergencia
    }
    with open(arquivo, "w", encoding = "utf-8") as f:
        json.dump(dados, f, indent = 4, ensure_ascii = False)
    print("[Salvo no arquivo]")

def carregar_dados():
    global medicos, pacientes, fila_normal, fila_prioridade, fila_emergencia
    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

            medicos = dados.get("medicos", medicos)
            pacientes = dados.get("pacientes", [])
            fila_normal = dados.get("fila_normal", [])
            fila_prioridade = dados.get("fila_prioridade", [])
            fila_emergencia = dados.get("fila_emergencia", [])
            for medico in medicos.values():
                medico.setdefault("agenda", {})
                medico.setdefault("dias", list(range(1, 32)))
            print("[Dados carregados do agenda.json]")
        except json.JSONDecodeError:
            print("O arquivo agenda.json está indisponivel ou corrompido")
            print("O sistema continuará com seus dados padrões")

def obter_nivel_por_paciente(nome):
    if nome in fila_emergencia:
        return 3
    if nome in fila_prioridade:
        return 2
    if nome in fila_normal:
        return 1
    return 1

def nome_risco(nivel):
    return nome_fila.get(nivel, "Sem risco")

def adicionar_na_fila(nome, nivel):
    remover_das_filas(nome)
    
    if nivel == 3:
        fila_emergencia.append(nome)
    elif nome == 2:
        fila_prioridade.append(nome)
    elif nome == 3:
        fila_normal.append(nome)

def remover_das_filas(nome):
    while nome in fila_normal:
        fila_normal.remove(nome)
    while nome in fila_prioridade:
        fila_prioridade.remove(nome)
    while nome in fila_emergencia:
        fila_emergencia.remove(nome)

def chave_dia_horario(chave):
    try:
        dia, horario = chave.split("|", 1)
        return int(dia), horario
    except (ValueError, AttributeError):
        return 999, ""

def buscar_vaga_mais_proxima(nome_medico, dia_inicial, ignorar_chaves=None):
    ignorar_chaves = ignorar_chaves or set()
    dados = medicos[nome_medico]

    dias_ordenados = [d for d in dados["dias"] if d >= dia_inicial]

    dias_ordenados += [d for d in dados["dias"] if d < dia_inicial]

    for dia in dias_ordenados:
        for horario in dados["horarios"]:
            chave = f"{dia}|{horario}"
            if chave in ignorar_chaves:
                continue
            if chave not in dados["agenda"]:
                return chave
    return None

def buscar_vagas_sem_pular(nome_medico, dia_inicial, ignorar_chaves=None):
    return buscar_vaga_mais_proxima(nome_medico, dia_inicial, ignorar_chaves)

def remarcar_paciente_expulso(nome_medico, paciente, nivel, dia_origem, chave_ocupada):
    nova_chave = buscar_vaga_mais_proxima(
        nome_medico,
        dia_origem,
        ignorar_chaves = {chave_ocupada}
    )
    if nova_chave is None:
        return False, None
    medicos[nome_medico]["agenda"][nova_chave] = paciente
    adicionar_na_fila(paciente, nivel)
    return True, nova_chave

def agendar_com_prioridade(nome_medico, dia, horario, paciente, nivel):
    agenda = medicos[nome_medico]["agenda"]
    chave = f"{dia}|{horario}"

    if chave not in agenda:
        agenda[chave] = paciente
        adicionar_na_fila(paciente, nivel)
        return True, None
    paciente_ocupante = agenda[chave]
    nivel_ocupante = obter_nivel_por_paciente(paciente_ocupante)

    if nivel <= nivel_ocupante:
        nova_chave = buscar_vaga_mais_proxima(
            nome_medico,
            dia,
            ignorar_chaves = {chave}
        )
        if nova_chave is None:
            return False, (
                f"Não há outro horário disponível para {paciente}."
                f"O paciente que já estava nesse horário é {paciente_ocupante}"
            )
        agenda[nova_chave] = paciente
        adicionar_na_fila(paciente, nivel)

        return True, (
            f"Horário original ocupado por {paciente_ocupante}"
            f"{paciente} foi direcionado automaticamente para {nova_chave}"
        )
    del agenda[chave]
    remover_das_filas(paciente_ocupante)

    conseguiu_remarcar, nova_chave = remarcar_paciente_expulso(
        nome_medico,
        paciente_ocupante,
        nivel_ocupante,
        dia,
        chave
    )

    if not conseguiu_remarcar:
        agenda[chave] = paciente_ocupante
        adicionar_na_fila(paciente_ocupante, nivel_ocupante)

        return False, (
            f"{paciente} é {nome_risco(nivel)} e teria prioridade sobre "
            f"{paciente_ocupante}, porém não existe outra vaga para "
            f"remanejar o paciente que já estava agendado"
        )
    agenda[chave] = paciente
    adicionar_na_fila(paciente, nivel)

    return True, (
        f"{paciente} ({nome_risco(nivel)}) passou na frente de "
        f"{paciente_ocupante} ({nome_risco(nivel_ocupante)}) \n"
        f"{paciente_ocupante} foi automaticamente remarcado para {nova_chave}."
    )



def fila_atendimento():
    limpar_tela()
    resposta_fila = -1
    while resposta_fila != 0:
        print("===> Fila De Atendimento <===\n")
        print("Opção 0: Sair: ")
        print("Opção 1: Fila de Atendimento Normal")
        print("Opção 2: Fila de Atendimento Prioridade")
        print("Opção 3: Fila de Atendimento Emergencia\n")
        print("Escolha uma Opção (0-3): ")
        try:
            resposta_fila = int(input(">  "))
        except ValueError:
            print("O valor inserido não é válido!")
            print("Voltando ao inicio...")
            time.sleep(2.5)
            fila_atendimento()
        if resposta_fila == 1:
            print(f"O atendimento da fila de sem risco é de {len(fila_normal)} pessoas")
            print("Aperte Enter para sair: ")
            input(">  ")
        elif resposta_fila == 2:
            print(f"O atendimento da fila de Prioritária é de {len(fila_prioridade)} pessoas")
            print("Aperte Enter para sair: ")
            input(">  ")
        elif resposta_fila == 3:
            print(f"o atendimento da fila de emergência é de {len(fila_emergencia)} pessoas")
            print("Aperte Enter para sair: ")
            input(">  ") 
        else:
            print("Fila de atendimento não encontrada")
            print("Redirecionando você ao inicio...")
            time.sleep(2.5)
            return


def cancelar_consulta():
    limpar_tela()
    print("\n=====================")
    print("-->Cancelar Consulta<--")
    print("=====================")

    nome_medico = input("Qual o médico a qual você quer cancelar a consulta (Bernado, João, Samara...) \n>  ")
    if nome_medico not in medicos:
        print("Médico não encontrado!")
        time.sleep(2)
        return
    try: 
        dia = int(input("Dia da consulta para cancelar: "))
        if dia < 1 or dia > 31:
            print("Dia inválido!")
            print("Carregando")
            time.sleep(2.5)
            return
        horario = input("Horário (ex: 9:30): \n>  ")
        if horario not in medicos[nome_medico]["horarios"]:
            print("Horário Inválido")
            print("Carregando")
            time.sleep(2.5)
            return
        chave = f"{dia}|{horario}"

        if chave not in medicos[nome_medico]["agenda"]:
            print(f"Não achei consulta dia {dia} às {horario} com {nome_medico}")
            print(f"Consultas desse médico: {medicos[nome_medico]['agenda']}")
            time.sleep(3)
            return
        
        paciente = medicos[nome_medico]['agenda'][chave]

        if paciente != nome_completo:
            print("Essa consulta não pertence ao seu cadastro!")
            print("Carregando...")
            time.sleep(2.5)
            return

        print(f"\nEncontrado: {paciente} com Dr.{nome_medico} dia {dia} às {horario}")
        confirmacao = input("Tem certeza que quer cancelar a sua consulta? \n>  ").strip().lower()
        tem_outra_consulta = False
        if confirmacao == 's' or confirmacao == 'sim':
            del medicos[nome_medico]["agenda"][chave]
            for medico in medicos.values():
                        for paciente_agendado in medico["agenda"].values():
                            if paciente_agendado == paciente:
                                tem_outra_consulta = True
            if not tem_outra_consulta:
                if paciente in fila_normal:
                    fila_normal.remove(paciente)
                if paciente in fila_prioridade:
                    fila_prioridade.remove(paciente)
                if paciente in fila_emergencia:
                    fila_emergencia.remove(paciente)

            salvar_dados()

            print(f"Consulta de {paciente} cancelada! Horário {dia} {horario} liberado.")
        else:
            print("Cancelamento abortado.")
        input("Aperte Enter para sair \n>  ")
    except ValueError:
        print("Dia inválido!")
        time.sleep(2)
        return


def remarcar_consulta():
    print("\n=====================")
    print("-->Remarcar Consulta<--")
    print("=====================")
    print(f"Olá {nome_completo} qual o nome do médico que iria te atender? (Bernado, Samara, João...)")
    nome_medico = input(">  ")
    if nome_medico not in medicos:
        print("Médico não encontrado!")
        time.sleep(2)
        return
    
    try:
        print("\n-- Consulta ANTIGA --")
        dia_antigo = int(input("Dia Antigo: \n>  "))
        horario_antigo = input("Horário antigo (ex: 9:30): \n>  ")
        chave_antiga = f"{dia_antigo}|{horario_antigo}"
        if chave_antiga not in medicos[nome_medico]["agenda"]:
            print(f"Não achei consulta  com {nome_medico} dia {dia_antigo} às {horario_antigo}")
            time.sleep(2)
            return
        paciente = medicos[nome_medico]["agenda"][chave_antiga]
        if paciente != nome_completo:
            print("Essa Consulta não pertence ao seu cadastro!")
            print("Carregando...")
            time.sleep(2.5)
            return
        print(f"Econtrei: {paciente} com {nome_medico}")
        time.sleep(5)
        limpar_tela()
        print(f"---Consulta NOVA---")
        print(f"Dias disponíveis: {medicos[nome_medico]["dias"]}")
        print(f"Horários disponíveis: {medicos[nome_medico]['horarios']}")
        dia_novo = int(input("Novo dia: \n>  "))
        horario_novo = input("Novo horário: \n>  ")
        chave_nova = f"{dia_novo}|{horario_novo}"
        if dia_novo not in medicos[nome_medico]["dias"]:
            print("Esse médico não atende neste dia novo!")
            time.sleep(2)
            return
        if horario_novo not in medicos[nome_medico]["horarios"]:
            print("Horário novo inválido!")
            return
        if horario_antigo not in medicos[nome_medico]["horarios"]:
            print("Horário antigo inválido!")
            time.sleep(2)
            return
        if chave_nova in medicos[nome_medico]["agenda"]:
            print(f"Erro: Dia {dia_novo} às {horario_novo} já está ocupado por {medicos[nome_medico]['agenda'][chave_nova]}")
            time.sleep(3)
            return
        if chave_nova == chave_antiga:
            print("A nova consulta é igual a consulta atual! ")
            print("Carregando...")
            time.sleep(2.5)
            return
        
        del medicos[nome_medico]["agenda"][chave_antiga]
        medicos[nome_medico]["agenda"][chave_nova] = paciente

        salvar_dados()

        print(f"\nRemarcado com sucesso!")
        print(f"{paciente} foi de {dia_antigo} {horario_antigo} --> {dia_novo} {horario_novo} com o Dr.{nome_medico}")
        print("Aperte Enter para Sair")
        input(">  ")

    except ValueError:
        print("A sua resposta é inválida (digite o dia em número), Tente Novamente...")
        print("Redirecionando você de volta ao inicio...")
        time.sleep(2.5)
        return
        
def marcar_consulta():
    limpar_tela()
    print("\n=====================")
    print("-->Marcar Consulta<--")
    print("=====================")
    print(f"Olá {nome_completo} primeiramente precisamos saber qual a situação de risco do(a) senhor(a)")
    print("\nOpção 1: Sem risco")
    print("Opção 2: Prioridade")
    print("Opção 3: Emergência")
    print("Opção 0: Sair")
    try:
        resposta_marcar_consulta = int(input(">  "))
        if resposta_marcar_consulta == 0:
            return
        if resposta_marcar_consulta not in [1, 2, 3]:
            print("Opção Inválida, Tente novamente mais tarde!")
            print("Carregando...")
            time.sleep(2.5)
            return
        print(f"\nMédicos Disponiveis: {list(medicos.keys())}")
        nome_medico = input("Digite o nome do médico: \n>  ")

        if nome_medico not in medicos:
            print("Médico não encontrado!")
            time.sleep(2)
            marcar_consulta()
            return
        print(f"Dias disponíveis: {medicos[nome_medico]['dias'][:15]}...")
        try:
            dia = int(input("Escolha o dia: \n>  "))
        except ValueError:
            print("Digite o dia usando apenas números")
            print("Carregando...")
            time.sleep(2.5)
            return
        if dia not in medicos[nome_medico]["dias"]:
            print("Esse médico não atende neste dia!")
            time.sleep(2.5)
            return
        print(f"Horários disponíveis: {medicos[nome_medico]['horarios']}")
        horario = input("Escolha o horário (ex: 8:00): \n>  ")
        if horario not in  medicos[nome_medico]["horarios"]:
            print("Horário Inválido!")
            time.sleep(2.5)
            return

        chave = f"{dia}|{horario}"
        if chave in medicos[nome_medico]["agenda"]:
            print(f"Erro: Esse horário já está ocupado por {medicos[nome_medico]['agenda'][chave]}")
            time.sleep(3)
            return
        
        if resposta_marcar_consulta == 1:
            fila_normal.append(nome_completo)
            medicos[nome_medico]["agenda"][chave] = nome_completo
            print(f"Consulta marcada sem risco com {nome_medico} dia {dia} às {horario}")
            
            
        elif resposta_marcar_consulta == 2:
            fila_prioridade.append(nome_completo)
            medicos[nome_medico]["agenda"][chave] = nome_completo
            print(f"Consulta marcada prioridade com {nome_medico} dia {dia} às {horario}")
            
            
        elif resposta_marcar_consulta == 3:
            fila_emergencia.append(nome_completo)
            medicos[nome_medico]["agenda"][chave] = nome_completo
            print(f"Consulta marcada Emergência com {nome_medico} dia {dia} às {horario}")

        salvar_dados()

        print("Aperte Enter para sair: ")
        input(">  ")
            
    except ValueError:
        print("O valor Inserido não é válido")
        print("Redirecionando de volta ao início...")
        time.sleep(2.5)
        return
    
def especialistas():
    limpar_tela()
    print("===========================")
    print("---Nossos Especialistas---")
    print("============================")
    for medico, dados in medicos.items():
        print(f"Médico: {medico}        Especialidade: {dados['especialidade']}")
        print("---------------------------------------------------------")
    print("Aperte Enter para Voltar ao menu inicial")
    input(">  ")
    return

def principal():
    limpar_tela()
    print("---> Sistema de Pacientes <---\n")
    print("Opção 1: Marcar Consulta")
    print("Opção 2: Remarcar Consulta")
    print("Opção 3: Cancelar Consulta")
    print("Opção 4: Nossos Especialistas")
    print("Opção 5: Fila de Atendimento")
    print("Opção 0: Sair")
    print(f"Olá o senhor(a) {nome_completo} Precisa escolher uma Opção (0-5):")
    resposta_opcoes = -1
    while resposta_opcoes != 0:
        try:
            resposta_opcoes = int(input(">  "))
        except ValueError:
            print("O valor inserido não é válido")
            print("Carregando...")
            time.sleep(2.5)
            return
        if resposta_opcoes == 1:
            print("Carregando...")
            time.sleep(2.5)
            marcar_consulta()
        elif resposta_opcoes == 2:
            print("Carregando...")
            time.sleep(2.5)
            remarcar_consulta()
        elif resposta_opcoes == 3:
            print("Carregando...")
            time.sleep(2.5)
            cancelar_consulta()
        elif resposta_opcoes == 4:
            print("Carregando...")
            time.sleep(2.5)
            especialistas()
        elif resposta_opcoes == 5:
            print("Carregando...")
            time.sleep(2.5)
            fila_atendimento()
        else:
            print("Opção Inválida!")
            print("Carregando...")
            time.sleep(2.5)


def logar():
    global nome_completo; global idade; global cpf
    limpar_tela()
    print("---Sistema de Login---\n")
    print("Para Fazer login precisamos do Seu nome/segundo nome/senha(CPF)/idade (A senha é dada quando você se cadastra)\n")
    print("Digite seu primeiro e segundo nome")
    resposta_nome_completo = input(">  ")
    print("Digite sua idade")
    try:
        resposta_idade = int(input(">  "))
    except ValueError:
        print("A idade deve ser um número")
        time.sleep(2.5)
        return
    print("Digite a senha que você cadastrou (CPF)")
    resposta_senha = input(">  ").strip()
    print("\nVerificando...")
    time.sleep(2)
    for paciente in pacientes:
        if (
            paciente["nome"] == resposta_nome_completo
            and paciente["idade"] == resposta_idade
            and paciente["cpf"] == resposta_senha
        ):
            nome_completo = paciente["nome"]
            idade = paciente["idade"]
            cpf = paciente["cpf"]


            print("Redirecionando você para nosso sistema de Pacientes")
            time.sleep(2.5)
            principal()
            return
        
    print("A sua resposta não corresponde aos dados reais, tente novamente ou contate o suporte.")
    

def cadastrar():
    global idade; global cpf; global nome_completo; global nome; global segundo_nome;
    limpar_tela()
    print("---Sistema de Cadastro---")
    print("Digite Seu nome: ")
    nome = input(">  ")
    print("Digite seu Segundo nome: ")
    segundo_nome = input(">  ")
    print("Digite Seu CPF, ele será usado como senha:")
    cpf = input(">  ").strip()
    print("Digite sua idade: ")
    nome_completo = nome + " " + segundo_nome
    try:
        idade = int(input(">  "))
        print("Seus Dados estão corretos ?")
        print(f"--> Nome Completo: {nome_completo}")
        print(f"--> Idade: {idade}")
        resposta_cadastro = input(">  ").strip().lower()
        if resposta_cadastro == "sim" or resposta_cadastro == "s":
            print(f"Sua senha é {cpf} guarde ela para logar quando precisar.")
            print("Redirecionando para nosso sistema de Pacientes...")
            pacientes.append({
                "nome" : nome_completo,
                "idade" : idade,
                "cpf" : cpf
            })

            salvar_dados()

            time.sleep(4.5)
            principal()
            return
        elif resposta_cadastro == "nao" or resposta_cadastro == "n":
            print("Resetando")
            time.sleep(2.5)
            cadastrar()
        else:
            print("A sua resposta é inválida")
    except ValueError:
        print("Digite apenas caracteres válidos!")
        print("voltando...")
        time.sleep(3.0)
        limpar_tela()
        return

def main():
    global idade; global cpf; global nome_completo;

    carregar_dados()

    limpar_tela()
    print("\n=======================")
    print("     Clínica Vida+   ")
    print("=======================\n")
    print("Olá seja bem vindo ao nosso Sistema da Clínica Vida+")
    print("O Senhor(a) possui cadastro em nosso sistema? ")
    resposta_inicial = input(">  ").strip().lower()
    if resposta_inicial == "sim" or resposta_inicial == "s":
        print("Faça seu Login em Nosso Sistema!")
        print("Redirecionando...")
        time.sleep(2.5)
        logar()
    elif resposta_inicial == "nao" or resposta_inicial == "n":
        print("Faça seu cadastro pelo nosso Sistema!")
        print("Redirecionando...")
        time.sleep(2.5)
        cadastrar()
    else:
        print("A sua resposta é inválida")
main()



