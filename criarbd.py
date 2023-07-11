criarbd.py
# importando SDLite
import sqlite3 as lite

# Criando conexao
con  = lite.connect('dados.db')

#criando tabale de categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMET,nome TEXT)")


#criando tabela de receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMET, categoria TEXT, adicionando_em DATE, valor DECIMAL)")


#criando tabela de gastos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMET, categoria TEXT, retirando_em DATE, valor DECIMAL)")

    
