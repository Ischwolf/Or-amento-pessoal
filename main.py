main.py
 from tkinter import *
 from tkinter import Tk, ttk
 from tkinter import messagebox 

 # importando Pillow
 from PIL import image, imageTk

#importando barra de progresso do Tlinter
from tkinter.ttk import rogressbar


#importando Metaplotlib
from matplotlib.backend_tkagg import FigureCanvasTkAgg
from matlotlib.pyplot as plt
from matplotlib.figure import Figure

# tkcalendar 
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando funcoes de view
from view import bar_valores, inserir_categotia,ver_categoria, inserir_receitas, inserir_gastos,tabela,deletar_gastos,deletar_receita
 #cores
 co0 = "#2e2d2b" #preta
 co1 = "#feffff" #branca
 co2 = "#4fa882" #verde
 co3 = "#38576b" #valor
 co4 = "#403d3d" #letras
 co5 = "#e06636"
 co6 = "#030cfc"
 co7 = "#3fbfb9"
 co8 = "#263238"
 co9 = "#e9edf5"

 colors = ['#5588b','#66bbbb','#99bb55','#ee9944','#444466','#bb5555']

#criando janela
janela = Tk ()
janela.title()
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE,height=FALSE)

style= ttk.Style(janela)
style.theme_use("clam")


#criando frames para divisao de tela
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0,column=0)

frameMeio = Frame(janela, width=1043, height=361, bg=co1,pady=20, relief="raised")
frameMeio.grid(row=1,column=0,pady=1,padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2,column=0,pady=0,padx=10, sticky=NSEW)



# Trabalhando no frame acima

# acessando a imagem
app_img = image.open('log.png')
app_img = app_img.resize((45,45))
app_img = imageTk.PhontoImage(app_img)

app_logo = Label(frameCima, image=app_img, text="Orçamento pessoal",width=900,compound=LEFT,padx=5,relief=RAISED,anchor=NW,font=('Verdana 20 bold'),bg=c01,fg=co4,)
app_logo.place(x=0, y=0)

#defini do tree como global
global Tree

# funcao inserir categoria
def inserir_categoria_b():
    nome = e_categoria.get()

    lista_inseir = [nome]

    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro','Preencha todos os campos')
            return
        # passando para a funcao inserir gastos presentes na view
    inserir_categoria(list_inserir)

    messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso')

    e_categoria.delete(0,'end')

    # Pegando os valores de categoria

    categorias_funcao = ver_categoria()
    categoria = []

    for i in categorias_funcao:
        categoria.append(i[1])

    # atualizar a lista a lista de categoria
    combo_categoria_despesas['values'] = (categoria)


# funcao inserir Despesas
def inserir_receitas_b():
    nome = combo_categoria_despesas.get()
    data = e_cal_despesas.get()
    quantia = e_valores_despesas.get()

    lista_inserir = [nome, data , quantia]

     for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro','Preencha todos os campos')
            return
    # chamando a funcao inserir Despesas presentes na view
    inserir_gastos(lista_inserir)

    messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso')

    combo_categoria_despesas.delete(0,'end')
    e_cal_despesas.delete(0,'end')
    e_valor_despesas.delete(0,'end')

    # atualizando dados
    mostrar_renda()
    porcentagem()
    grafico_bar()
    resumo()
    grafico_pie()



# funcao deletar 
def deletar_dados():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        nome = treev_lista[1]

        if nome =='Receita':
            deletar_receitas([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            # atualizando dados  

            mostrar_renda()
            porcentagem()
            grafico_bar()
            resumo()
            grafico_pie()
   
        else:
            deletar_gastos([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            # atualizando dados  
            mostrar_renda()
            porcentagem()
            grafico_bar()
            resumo()
            grafico_pie()

    except IndexError:
        messagebox.showerror('Erro','Selecionar um dos dados na tabela')





#percetagem -------------------------------

def percentagem():
	1_nome = Label(frameMeio, text="Porcentagem da Receita gasta", height=1,anchor=NW, font=('Verdana 12'),bg=co1, fg=co4)
	1_nome.place(x=7, y=5)

	style = ttk.Style()
	style.theme_use('default')
	style.configure("black.Horizontal.TProgressbat", background='#daed6b')
	style.configure("TProgressbar", thickness=25)

	bar = Progressbar(frameMeio, length=180)
	bar.place(x=10, y=35)
	bar['value'] = 50 

	valor = 50

	1_percentagem = Label(frameMeio, text="{:,.2f}".format(valor),anchor=NW, font={'verdana 12'}, bg=co1, fg=co4)
	1_percentagem.place(x=200, y=35)



#funcao para grafico bars ------------------------

def grafico_bar():
    lista_categorias = ['Renda','Despesas','Saldo']
    lista_valores = [3000,2000,6236]

# faça figura e atribua objetos de eixo --------------------

    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    # ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)

    # create a list to collect the plt.patches data ---------------

    c = 0
    # set individual bar lables using above list --------------------

    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)



# funcao de resumo total
def resumo():
    valor = [500,600,420]

    1_linha = Label(frameMeio, text="", width=125, height=1, anchor=NW,font=('Arial 1'), bg='#545454')
    1_linha.place(x=309, y=52)
    1_linha = Label(frameMeio, text="Total Renda Mensal      ".upper(),anchor=NW,font=('Verdana 1'), bg=co1, fg='#83a9e6')
    1_linha.place(x=309, y=35)
    1_linha = Label(frameMeio, text="R$ {:,.2f}".format(valor[0]),anchor=NW,font=('Arial 17'), bg=co1, fg='#545454')
    1_linha.place(x=309, y=70)

    1_linha = Label(frameMeio, text="", width=125, height=1, anchor=NW,font=('Arial 1'), bg='#545454')
    1_linha.place(x=309, y=132)
    1_linha = Label(frameMeio, text="Total Despesas Mensais     ".upper(),anchor=NW,font=('Verdana 1'), bg=co1, fg='#83a9e6')
    1_linha.place(x=309, y=115)
    1_linha = Label(frameMeio, text="R$ {:,.2f}".format(valor[0]),anchor=NW,font=('Arial 17'), bg=co1, fg='#545454')
    1_linha.place(x=309, y=150)

    1_linha = Label(frameMeio, text="", width=125, height=1, anchor=NW,font=('Arial 1'), bg='#545454')
    1_linha.place(x=309, y=207)
    1_linha = Label(frameMeio, text="Total Saldo da Caixa     ".upper(),anchor=NW,font=('Verdana 1'), bg=co1, fg='#83a9e6')
    1_linha.place(x=309, y=190)
    1_linha = Label(frameMeio, text="R$ {:,.2f}".format(valor[0]),anchor=NW,font=('Arial 17'), bg=co1, fg='#545454')
    1_linha.place(x=309, y=220) 


frame_gra_pie = frame(frameMeio, width=580, height=250, bg=co2)
frame_gra_pie.place(x=415, y=5)

# funcao grafico pie
def grafico_pie():
    frame_gra_pie = Frame(frameMeio, width=580, height=250, bg=co2)
frame_gra_pie.place(x=415, y=5)

# funcao grafico pie
def grafico_pie():
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    # only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, colum=0)


percentagem():
grafico_bar()
resumo()
grafico_pie()



#criando frames dentro do Frame Baixo
frame_renda = Frame(frameBaixo, width=300, height=250, bg=co1,)
frame_renda.grid(row=0,column=0)

frame_operacoes = Frame(frameBaixo, width=220, height=250, bg=co1,)
frame_operacoes.grid(row=0,column=1, padx=5)


frame_configuracao = Frame(frameBaixo, width=220, height=250, bg=co1,)
frame_configuracao.grid(row=0,column=2, padx=5)


# Tabela Renda mensal ---------------------------------------------
app_tabela = Label(frameMeio,text="Tabela Receitas e Despesas",anchor=NW,font=('Verdana 12'),bg=c01,fg=co4)
app_tabela.place(x=5, y=309)


# funcao para mostrar_renda
def mostrar_renda():
    # creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = tabela()
    
    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)


mostrar_renda():
 

# configuracoes Despesas --------------------------------------- 
1_info = Label(frame_operacoes, text='Insiras novas despesas', height=1, anchor=NW, font=('verdana 10 bold'), bg=co1, fg=co4)
1_info.place(x=10, y=10)

# categoria -------------
1_categoria= Label(frame_operacoes, text='Categoria', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
1_categoria.place(x=10, y=40)

# Pegando categorias 
categoria_funcao = ver_categoria()
categoria = []

for i in categoria_funcao:
    categoria.append(i[1])


combo_categoria_despesas = ttk.combobox(frame_operacoes,width=10, font=('Ivy10'))
combo_categoria_despesas['values'] = (categoria)
combo_categoria_despesas.place(x=110, y=41)

# despesas ------------
1_cal_despesas= Label(frame_operacoes, text='Data', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
1_cal_despesas.place(x=10, y=70)
e_cal_despesas = DataEntry(frame_operacoes,  width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
e_cal_despesas.place(x=110, y=71)

# valor -------------
1_valor_despesas= Label(frame_operacoes, text='Quantia Total', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
1_valor_despesas.place(x=10, y=100)
e_valor_despesas = Entry(frame_operacoes, width=14, justify='left', relief='solid')
e_valor_despesas.place(x=110, y=101)


# Botao Inserir
img_add_despesas = Image.open('add.png')
img_add_despesas = img_add_despesas.resize((17,17))
img_add_despesas = ImageTk.PhontoImage(img_add_despesas)
botao_inserir_despesas = Label(frame_operacoes,command=inserir_receitas_b,  image=img_add_receitas, text="Adicionar".upper(),width=80,compound=LEFT,anchor=NW,font=('Ivy 7 bold'),bg=co1,fg=co0, overrelief=RIDGE)
botao_inserir_despesas.place(x=110, y=131)


# Botao Excluir
1_add_excluir= Label(frame_operacoes, text='Excluir ação', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
1_add_excluir.place(x=10, y=190)

img_delete = Image.open('add.png')
img_delete = delete.resize((17,17))
img_delete = ImageTk.PhontoImage(delete)
botao_deletar = Label(frame_operacoes, command=deletar_dados, image=img_delete, text="Deletar".upper(),width=80,compound=LEFT,anchor=NW,font=('Ivy 7 bold'),bg=co1,fg=co0, overrelief=RIDGE)
botao_deletar.place(x=110, y=190)


# configuracoes Receitas ------------------------------------
1_info = Label(frame_configuracao, text='Insiras novas receitas', height=1, anchor=NW, font=('verdana 10 bold'), bg=co1, fg=co4)
1_info.place(x=10, y=10)

# calendario ------------
1_cal_receitas= Label(frame_configuracao, text='Data', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
1_cal_receitass.place(x=10, y=70)
e_cal_receitas = DataEntry(frame_configuracao,  width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
e_cal_receitas.place(x=110, y=41)

# valor -------------
1_valor_receitas= Label(frame_configuracao, text='Quantia Total', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
1_valor_receitas.place(x=10, y=70)
e_valor_receitas = Entry(frame_configuracao, width=14, justify='left', relief='solid')
e_valor_receitas.place(x=110, y=71)

# Botao Inserir
img_add_receitas = Image.open('add.png')
img_add_receitas = img_add_despesas.resize((17,17))
img_add_receitas = ImageTk.PhontoImage(img_add_receitas)
botao_inserir_receitas = Label(frame_configuracao, image=img_add_receitas, text="Adicionar".upper(),width=80,compound=LEFT,anchor=NW,font=('Ivy 7 bold'),bg=co1,fg=co0, overrelief=RIDGE)
botao_inserir_receitas.place(x=110, y=111)


# Operacao Nova Categoria ------------------------------------

1_info = Label(frame_configuracao, text='Categoria', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
1_info.place(x=10, y=160)

e_categoria = Entry(frame_configuracao, width=14, justify='left', relief='solid')
e_categoria.place(x=110, y=160)

# Botao Inserir
img_add_categoria = Image.open('add.png')
img_add_categoria = img_add_despesas.resize((17,17))
img_add_categoria = ImageTk.PhontoImage(img_add_receitas)
botao_inserir_categoria = Label(frame_configuracao, image=img_add_categoria, text="Adicionar".upper(),width=80,compound=LEFT,anchor=NW,font=('Ivy 7 bold'),bg=co1,fg=co0, overrelief=RIDGE)
botao_inserir_categoria.place(x=110, y=190)



janela.mainloop()
