from tkinter import *
import os
import sys
cab=3000 
mot=8000
cam=1800 
pg = 0


def bt_mot():
    global pg
    pg += mot 
    Label (janela, text="Valor TOTAL:R$%.2f \n ----------------------------------"%(pg)).place(x=180,y=180)
def bt_cab():
    global pg
    pg += cab
    Label (janela, text="Valor TOTAL:R$%.2f \n ----------------------------------"%(pg)).place(x=180,y=180)
def bt_cam():
    global pg
    pg += cam
    Label (janela, text="Valor TOTAL:R$%.2f \n ----------------------------------"%(pg)).place(x=180,y=180)


def bt_ford():
    label1 = Label (janela, text="Peças disponiveis:         ")
    label1.place(x=310,y=50)
    bt1 = Button(janela, width=20, text="Cambio = R$1800.00",command=bt_cam)
    bt1.place(x=310,y=80)
    bt2 = Button(janela, width=20, text="Cabeçote = R$3,000.00",command=bt_cab)
    bt2.place(x=310,y=115)
    bt3 = Button(janela, width=20, text="Motor = R$8,000.00",command=bt_mot)
    bt3.place(x=310,y=150)

    
def bt_chevrolet():
    label1 = Label (janela, text="Peças disponiveis:         ")
    label1.place(x=310,y=50)
    bt1 = Button(janela, width=20, text="Cambio = R$1800.00",command=bt_cam)
    bt1.place(x=310,y=80)
    bt2 = Button(janela, width=20, text="Cabeçote = R$3,000.00",command=bt_cab)
    bt2.place(x=310,y=115)
    bt3 = Button(janela, width=20, text="Motor = R$8,000.00",command=bt_mot)
    bt3.place(x=310,y=150)

def bt_volks():
    label1 = Label (janela, text="Peças disponiveis:         ")
    label1.place(x=310,y=50)
    bt1 = Button(janela, width=20, text="Cambio = R$1800.00",command=bt_cam)
    bt1.place(x=310,y=80)
    bt2 = Button(janela, width=20, text="Cabeçote = R$3,000.00",command=bt_cab)
    bt2.place(x=310,y=115)
    bt3 = Button(janela, width=20, text="Motor = R$8,000.00",command=bt_mot)
    bt3.place(x=310,y=150)

def bt_total ():
    global pg
    p = pg*0.05 
    pg = pg - p
    Label (janela, text="R$:%.2f"%(pg)).place(x=80,y=220)
       
def bt_p1 ():
    global pg
    p = pg*0.05
    pg = pg+p
    p1 = pg / 2
    Label (janela, text="R$:%.2f, em 2x de R$ %.2f"%(pg , p1)).place(x=80,y=220)

def bt_p2 ():
    global pg
    p = pg*0.05
    pg = pg + p
    p1 = pg/3
    Label (janela, text="R$:%.2f, em 3x de R$ %.2f"%(pg , p1)).place(x=80,y=220)

def bt_p3 ():
    global pg
    p = pg*0.05
    pg = pg+p
    p1=pg/4
    Label (janela, text="R$:%.2f, em 4x de R$ %.2f"%(pg , p1)).place(x=80,y=220)

def bt_p4 ():
    global pg
    p=pg*0.05
    pg = pg+p
    p1=pg/5
    Label (janela, text="R$:%.2f, em 5x de R$ %.2f"%(pg , p1)).place(x=80,y=220)

def Quit():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
janela=Tk()
janela.title("Auto Peças")
janela.geometry("720x280+250+50")


label1 = Label (janela, text="Marcas:")
label1.place(x=120,y=50)
label3=Label(janela, text="Valor total:") 
label3.place(x=10, y=220)
label4 = Label(janela, text="--Opções-- \n Esolha Forma de pagamento: \n A vista com 5% de desconto \n Em 2x(5% de juros)   \n Em 3x(5% de juros) \n  Em 4x (5% de juros)   \n Em 5x (5% de juros)")
label4.place(x=500, y = 20)


bt0 = Button(janela, width=15, text="Volkswagem",command=bt_volks)
bt0.place(x=120, y=80)
bt1 = Button(janela, width=15, text="Ford",command=bt_ford)
bt1.place(x=120,y=115)
bt2 = Button(janela, width=15, text="Chevrolet",command=bt_chevrolet)
bt2.place(x=120,y=150)
bt3 = Button(janela, width=15, text="A vista",command=bt_total)
bt3.place(x=10,y=240)
b4 = Button(janela, width=15, text="Em 2x",command=bt_p1)
b4.place(x=125, y=240)
b5 = Button(janela, width=15, text="Em 3x",command=bt_p2)
b5.place(x=240, y=240)
b6 = Button(janela, width=15, text="Em 4x",command=bt_p3)
b6.place(x=355, y=240)
b7 = Button(janela, width=15, text="Em 5x",command=bt_p4)
b7.place(x=470, y=240)
b8 = Button(janela, width=15, text="Voltar",command=Quit)
b8.place(x=595, y=240)

janela.mainloop()

