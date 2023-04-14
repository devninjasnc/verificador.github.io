from tkinter import *
import time
import tkinter.messagebox as MessageBox

master = Tk()
master.title("Url Checker")
master.geometry("490x560+610+153")
master.resizable(width=1, height=1)


# Funções
def verificar_():
    nome=en_url.get()

    if 'www.amazon.com.br' == nome:
        MessageBox.showinfo('SITE CONFIAVEL','SITE SEGURO CONTINUE NAVEGANDO')
    elif 'www.americanas.com.br' == nome:
        MessageBox.showinfo('SITE CONFIAVEL','SITE SEGURO CONTINUE NAVEGANDO')
    elif 'www.magazineluiza.com.br' == nome:
        MessageBox.showinfo('SITE CONFIAVEL','SITE SEGURO CONTINUE NAVEGANDO')

    else:
        MessageBox.showwarning('SITE FALSO','SITE FALSO CUIDADO')



# Importar imagens
img_fundo = PhotoImage(file="imagens\\fundo.png")
img_botao = PhotoImage(file="imagens\\bt-img.png")

# Criação de labels
lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

# Criação da entrada

en_url = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
en_url.place(width=300, height=45, x=112, y=281)

# Criação de botões
bt_verificar = Button(master, bd=0, image=img_botao, command=verificar_)
bt_verificar.place(width=118, height=50, x=194, y=351)

master.mainloop()