
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
aldair = Pessoa(1, "Aldair Frederico")
print(aldair)

#Quero mostrar só o nome
print(aldair.nome)

print("Daqui pra frente é so alegria")


#Chama o objeto do banco de dados
db = Database()


PessoaDAO = PessoaDAO( db.conexao, db.cursor)


pessoas = PessoaDAO.getAll()
for pessoa in pessoas:
 print(pessoa)



