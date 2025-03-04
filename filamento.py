from tkinter import *
from tkinter import PhotoImage

class Tela():

    def __init__(self, event):
    
        cab = PhotoImage(file="filamento.png")
        img = Label(janela, image=cab)
        img.cab = cab
        img.config(bg="white")
        img.place(x=0,y=1)

        self.t1 = Label(janela, text="Preço de 1kg:")
        self.t1["font"] = ("Calibri", "20")
        self.t1.place(x=140, y=120)

        self.e1 = Entry(janela)
        self.e1["font"] = ("Calibri", "20")
        self.e1.config(foreground="red")
        self.e1.place(x=320, y=120, width=100)

        self.t3 = Label(janela, text="Peso do modelo:")
        self.t3["font"] = ("Calibri", "17")
        self.t3.place(x=150, y=200)

        
        self.e2 = Entry(janela)
        self.e2["font"] = ("Calibri", "20")
        self.e2.config(foreground="blue")
        self.e2.place(x=320, y=200, width=100)

        bt = PhotoImage(file="bt.png")
        self.img1 = Button(janela, image=bt)
        self.img1.bt = bt
        self.img1.config(bg="white")
        self.img1.place(x=430,y=120)
        self.img1.bind("<Button-1>", self.calcular)

    def calcular(self, event):

        valor = float(self.e1.get())
        

        v_filamento = float(valor/1000)
        #print(v_filamento)

        self.t2 = Label(janela, text="Grama do filamento R$")
        self.t2["font"] = ("Calibri", "18")
        self.t2.config(foreground="green")
        self.t2.place(x=130,y=320)
        
        self.r = Label(janela, text=v_filamento)
        self.r["font"] = ("Calibri", "18")
        self.r.config(foreground="red")
        self.r.place(x=380,y=320)

        ###############################

        modelo = float(self.e2.get())

        v_modelo = int(modelo*v_filamento)

        #print(v_modelo)

        self.t4 = Label(janela, text="Preço do material R$")
        self.t4["font"] = ("Calibri", "18")
        self.t4.config(foreground="blue")
        self.t4.place(x=130,y=350)
        
        self.r2 = Label(janela, text=v_modelo)
        self.r2["font"] = ("Calibri", "18")
        self.r2.config(foreground="green")
        self.r2.place(x=380,y=350)

        
      

janela = Tk()
Tela(janela)
janela.title(">>>> CALCULAR FILAMENTO PARA IMPRESSÃO 3D <<<<")
janela.geometry("600x400")
janela.resizable(width=False, height=False)
janela.mainloop()
