from tkinter import *




# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

#color de fondo
aplicacion.config(bg='#fecdd3')

# evitar ampliar pantalla
aplicacion.resizable(0, 0)

#titulo
aplicacion.title(' Senci Pizza - Sistema de facturación ')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Senci Pizza', fg='azure4',
                        font=('Dosis', 42), bg='#fecdd3', width=27)
etiqueta_titulo.grid(row=0, column=0)


#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)
#panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)
#panel Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)



#panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()


# lista
lista_comidas = ['pollo', 'cordero', 'salon', 'pizza1', 'pizza2']
lista_bebidas = ['agua', 'cerveza', 'vino', 'soda', 'alcohol']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'ados con leche']

contador = 0
for comida in lista_comidas:
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0)
    comida.grid(row=contador, column=0, sticky=W)
    contador+= 1

# evitar que la pantalla se cierre
aplicacion.mainloop()