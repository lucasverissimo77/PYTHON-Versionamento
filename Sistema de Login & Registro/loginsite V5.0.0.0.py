#Sistema de Registro e Login
#versão 5.0.0.0 em python
#Feito por Lucas Verissimo


import streamlit as st
if "usuarios_cadastrados" not in st.session_state:
    st.session_state.usuarios_cadastrados = {
    "lucas": "lucas777",
    "adm_joao batista": "777adm"
}
if "tentativas" not in st.session_state:
    st.session_state.tentativas = 3

st.title("Sistema de Acesso")

opcao = st.radio("Você já tem cadastro?", ["Sim", "Não"])
usuario = st.text_input("Usuário: ")
senha = st.text_input("Senha:", type="password")
if opcao == "Não":
    senha_confirmada = st.text_input("Confirme Sua Senha:", type="password")
    if st.button("Cadastrar"):
        if usuario in st.session_state.usuarios_cadastrados:
            st.error("Usuário já Existente!")
        elif senha != senha_confirmada:
            st.error("Senhas Diferentes!")
        else:
            st.session_state.usuarios_cadastrados[usuario] = senha
            st.success(f"Sucesso usuário, {usuario} já pode fazer o login em nosso Site!")
            st.session_state.tentativas = 3

elif opcao == "Sim":
    if st.button("Login"):
        if usuario not in st.session_state.usuarios_cadastrados:
            st.error("Usuário Inexistente")

        else:
            senha_salva = st.session_state.usuarios_cadastrados[usuario]

            if senha == senha_salva:
                st.success(f"Acesso concedido!! Bem-vindo {usuario}")
                st.session_state.tentativas = 3

                if usuario == "adm_joao batista":
                    st.subheader("Painel de Administrador")
                    opcao_adm = st.radio("Escolha uma Opção:",
                                         ["Ver todos os Usuários", "Deletar Usuário", "Deslogar"])

                    if opcao_adm == "Ver todos os Usuários":
                        st.write("### Lista de Usuários: ###")
                        for user in st.session_state.usuarios_cadastrados:
                            st.write(f" - {user} - ")

                    elif opcao_adm == "Deletar usuário":
                        usuario_del = st.text_input("Digite o Usuário que o senhor quer deletar:")
                        if st.button("Deletar"):
                            if usuario_del in st.session_state.usuarios_cadastrados:
                                del st.session_state.usuarios_cadastrados[usuario_del]
                                st.success(f"Usuário {usuario_del} Deletado com Sucesso!!")
                            else:
                                st.error("Usuário não encontrado.")

                    elif opcao_adm == "Deslogar":
                        st.info("Você saiu do Painel de Administrador!")

                else:
                    st.subheader("Área do Usuário")
                    st.write("Você está no painel comum. Aproveite o conteúdo deste maravilhoso site")

            else:
                st.session_state.tentativas -= 1
                if st.session_state.tentativas > 0:
                    st.error(f"Senha incorreta! Você ainda tem {st.session_state.tentativas} tentativa(s)")
                else:
                    st.error("Acesso Bloqueado! Número de Tentativas Excedido!")
                    st.session_state.tentativas = 3
