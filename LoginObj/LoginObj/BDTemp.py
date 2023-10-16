###### Classe ######

class Pessoa:
    def __init__(self, Login, Nome, CPF, Genero, DataNasc, Senha):
        self.Login = Login
        self.Nome = Nome
        self.CPF = CPF
        self.Genero = Genero
        self.DataNasc = DataNasc
        self.Senha = Senha

###### LISTA ######

Lista = []

###### Cadastro ######

def CadastroBD(Login, Nome, CPF, Genero, DataNasc, Senha):
    obj = Pessoa (Login, Nome, CPF, Genero, DataNasc, Senha)
    Lista.append(obj)


def AutenticarBD(Login, Senha):
    if not Lista:
        return "Vazia"
    else:
        for user in Lista:
            if ((user.Login == Login) and (user.Senha == Senha)):
                return "Certo"
            else:
                return "Errado"