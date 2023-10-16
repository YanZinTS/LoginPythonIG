from Modulos import *
import customtkinter as Tk
from BDTemp import *

###########   Funções   ###########

def Cadastrar():
    Login = Cx_Cad_Login.get()
    Nome = Cx_Cad_Nome.get()
    CPF = Cx_Cad_CPF.get()
    Genero = Cb_Cad_Genero.get()
    DataNasc = Cx_Cad_DataNas.get()
    Senha = Cx_Cad_Senha.get()
    Senha2 = Cx_Cad_ConfSenha.get()
    if Cx_Cad_Login.get() and Cx_Cad_Nome.get() and Cx_Cad_CPF.get() and Cb_Cad_Genero.get() != "Selecione" and Cx_Cad_DataNas.get() and Cx_Cad_Senha.get():
        if Senha == Senha2:
            CadastroBD(Login, Nome, CPF, Genero, DataNasc, Senha)
            LimparCax()
            Lb_Cad_Erro.configure(text="Cadastro efetuado com sucesso!")
        else:
            Lb_Cad_Erro.configure(text="Confira a Senha!")
    else:
        Lb_Cad_Erro.configure(text="Confira as informações!")

def AlterarTema():
    if SwTemas.get()==1:
        Tk.set_appearance_mode("dark")
    else:
        Tk.set_appearance_mode("light")

def Cadastro():
    Abas.set("Cadastro")

def Voltar():
    Abas.set("Login")

def Limpar():
    Lb_Cad_Erro.configure(text=" ")
    Lb_Erro.configure(text=" ")

def LimparCax():
    Cx_Cad_ConfSenha.delete(0,"end")
    Cx_Cad_Senha.delete(0,"end")
    Cx_Cad_Login.delete(0,"end")
    Cx_Cad_Nome.delete(0,"end")
    Cx_Cad_CPF.delete(0,"end")
    Cx_Cad_DataNas.delete(0,"end")

    caixas_texto = [Cx_Cad_ConfSenha, Cx_Cad_Senha, Cx_Cad_Login, Cx_Cad_Nome, Cx_Cad_CPF, Cx_Cad_DataNas]
    for cx in caixas_texto:
        cx.delete(0, "end")

    Cb_Cad_Genero.set("Selecione")


def Autenticar():
    Login = Cx_Login.get()
    Senha = Cx_Senha.get()
    Resposta = AutenticarBD(Login, Senha)
    match Resposta:
        case "Certo":
            TelaLogado.deiconify()
        case "Errado":
            Lb_Erro.configure(text=Resposta)
        case "Vazia":
            Lb_Erro.configure(text="Sem cadastro")





TelaLogin = CriarJanela("Login","400x500+650+150",1)
TelaLogado = CriarJanela("Login","400x500+650+150",2)
TelaLogado.withdraw()
Lb_Login = CriarLabel(TelaLogado,"Logado com Sucesso",6,6)
Abas=CriarAbas(TelaLogin,3,6,350,450, "Login","Cadastro")
Abas.configure(state="disabled")
SwTemas = CriarSwitch(TelaLogin,"Alterar Tema  ",0,0,AlterarTema)
SwTemas.grid(columnspan=13, sticky = "E")

###########   Tela de Login   ###########

#Login
Lb_Login = CriarLabel(Abas.tab("Login"),"Login:",2,6)
Lb_Login.grid(sticky = "S")
Cx_Login = CriarCaixaDeTexto(Abas.tab("Login"),150,30,3,6,"Login")
Cx_Login.grid(sticky = "N")

#Senha
Lb_Senha = CriarLabel(Abas.tab("Login"),"Senha:",4,6)
Lb_Senha.grid(sticky = "S")
Cx_Senha = CriarCaixaDeTexto(Abas.tab("Login"),150,30,5,6,"Senha",Modo='Senha')
Cx_Senha.grid(sticky = "N")

#Label de Erro
Lb_Erro = CriarLabel(Abas.tab("Login")," ",6,0)
Lb_Erro.grid(columnspan = 13)

BtnEntrar= CriarBotão(Abas.tab("Login"),"Entrar",Autenticar,7,0,100,30)
BtnEntrar.grid(columnspan=13)
BtnCadastro= CriarBotão(Abas.tab("Login"),"Cadastre-se",Cadastro,8,0,100,30)
BtnCadastro.configure(fg_color=Abas.cget("fg_color"),hover_color=Abas.cget("fg_color"),text_color="MediumBlue")
BtnCadastro.grid(columnspan=13)

###########   Tela de Cadastro   ###########
#Logi
Lb_Cad_Login = CriarLabel(Abas.tab("Cadastro"),"Login:",0,5)
Lb_Cad_Login.grid(sticky = "S")
Cx_Cad_Login = CriarCaixaDeTexto(Abas.tab("Cadastro"),150,30,0,6,"Login")
Cx_Cad_Login.grid(sticky = "S")

#Nome
Lb_Cad_Nome = CriarLabel(Abas.tab("Cadastro"),"Nome:",1,5)
Lb_Cad_Nome.grid(sticky = "S")
Cx_Cad_Nome = CriarCaixaDeTexto(Abas.tab("Cadastro"),150,30,1,6,"Nome")
Cx_Cad_Nome.grid(sticky = "S")

#CPF
Lb_Cad_CPF = CriarLabel(Abas.tab("Cadastro"),"CPF:",2,5)
Lb_Cad_CPF.grid(sticky = "S")
Cx_Cad_CPF = CriarCaixaDeTexto(Abas.tab("Cadastro"),150,30,2,6,Modo="CPF")
Cx_Cad_CPF.grid(sticky = "S")

#Gênero
Lb_Cad_Genero = CriarLabel(Abas.tab("Cadastro"),"Gênero:",3,5)
Lb_Cad_Genero.grid(sticky = "S")
Cb_Cad_Genero = CriarComboBox(Abas.tab("Cadastro"),150,30,["Masculino","Feminino","Outro"],3,6)
Cb_Cad_Genero.grid(sticky = "S")

#Data de Nascimento
Lb_Cad_DataNas = CriarLabel(Abas.tab("Cadastro"),"Data de \nNascimento:",4,5)
Lb_Cad_DataNas.grid(sticky = "S")
Cx_Cad_DataNas = CriarCaixaDeTexto(Abas.tab("Cadastro"),150,30,4,6,Modo="Data")
Cx_Cad_DataNas.grid(sticky = "S")

#Senha
Lb_Cad_Senha = CriarLabel(Abas.tab("Cadastro"),"Senha: ",5,5)
Lb_Cad_Senha.grid(sticky = "S")
Cx_Cad_Senha = CriarCaixaDeTexto(Abas.tab("Cadastro"),150,30,5,6,Modo="Senha")
Cx_Cad_Senha.grid(sticky = "S")

#Confirmar Senha
Lb_Cad_ConfSenha = CriarLabel(Abas.tab("Cadastro"),"Senha: ",6,5)
Lb_Cad_ConfSenha.grid(sticky = "S")
Cx_Cad_ConfSenha = CriarCaixaDeTexto(Abas.tab("Cadastro"),150,30,6,6,Modo="Senha")
Cx_Cad_ConfSenha.grid(sticky = "S")

# Mensagem de Erro
Lb_Cad_Erro = CriarLabel(Abas.tab("Cadastro")," ",7,0)
Lb_Cad_Erro.grid(columnspan=13)

#Botões
Btn_Cad_Cadastrar = CriarBotão(Abas.tab("Cadastro"),"Cadastrar",Cadastrar,8,0,100,30)
Btn_Cad_Cadastrar.grid(columnspan=13)
Btn_Cad_Voltar = CriarBotão(Abas.tab("Cadastro"),"Voltar",Voltar,9,0,100,30)
Btn_Cad_Voltar.grid(columnspan=13)


TelaLogin.mainloop()