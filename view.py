view.py
#importando SQLite
import sqlite3 as lite 

# Criando conexao 
con = LIte.connect('dados.db')

#funcoes de insercao----------------------

# Inserir categoria
def inserir_categoria(i):
with con: 
	cur = con.cursor()
	query = "INSERT INTO Categoria (nome) VALUES (?)"
	cur.execute(query,i)


# Inserir Receitas
def inserir_categoria(i):
with con: 
	cur = con.cursor()
	query = "INSERT INTO Receitas (categoria, adicionando_em,valor) VALUES (?,?,?)"
	cur.execute(query,i)

# Inserir Gastos
def inserir_gastos(i):
with con: 
	cur = con.cursor()
	query = "INSERT INTO Gastos (categoria, retirando_em,valor) VALUES (?,?,?)"
	cur.execute(query,i)

#funcoes para deletar ----------------------------

#Deletar Receitas
def deletar_receitas(i):
with con:
	cur = con.cursor()
	query = "DELETE FROM Receitas WHERE id=?"
	cur.execute(query, i)


#Deletar Gastos
def deletar_gastos(i):
with con:
	cur = con.cursor()
	query = "DELETE FROM Gastos WHERE id=?"
	cur.execute(query, i)


#funcoes para ver dados ----------------------------

#ver categoria
def ver_categoria():
	lista_itens = []

	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM Categoria")
		linha = cur.fetchall()
		for 1 in linhas:
		lista_itens.append(1)
	return lista_itens



#ver Receitas
def ver_categoria():
	lista_itens = []

	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM Receitas")
		linha = cur.fetchall()
		for 1 in linhas:
		lista_itens.append(1)

	return lista_itens



#ver Gastos
def ver_categoria():
	lista_itens = []

	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM Gastos")
		linha = cur.fetchall()
		for 1 in linhas:
		lista_itens.append(1)

	return lista_itens

#funcao para dados da tabela
def tabela():
	gastos = ver_gastos()
	receitas = ver_receitas()

	tabela_lista = []

	for i in gastos:
		tabela_lista.append(i)

	for i in receita:
		tabela_lista.append(i)

	return lista_itens

# funcao para dados do grafico de barra
def bar_valores():
	#receitas Total ----------------
	receitas = ver_receitas()
	receitas_lista = []

	 for i in receitas:
	 	receitas_lista.append(i[3])
