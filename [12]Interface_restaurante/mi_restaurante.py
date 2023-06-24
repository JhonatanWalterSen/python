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
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4')
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

# Generar Items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    #crear los CheckButton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 14, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)
    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,font=('Dosis',14,'bold'),
                                     bd=1,width=6,state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)
    contador+= 1

# Generar Items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 14, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Dosis', 14, 'bold'),
                                     bd=1, width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador+= 1

# Generar Items postre
variables_postre = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 14, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postre[contador])
    postre.grid(row=contador, column=0, sticky=W)
    # crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres, font=('Dosis', 14, 'bold'),
                                     bd=1, width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_postres[contador].grid(row=contador, column=1)
    contador+= 1

#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida= Entry(panel_costos, font=('Dosis', 12, 'bold'),
                          bd=1, width=10, state='readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=50)

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida= Entry(panel_costos, font=('Dosis', 12, 'bold'),
                          bd=1, width=10, state='readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=50)

etiqueta_costo_postres = Label(panel_costos,
                              text='Costo Postres',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postres.grid(row=2, column=0)
texto_costo_postres= Entry(panel_costos, font=('Dosis', 12, 'bold'),
                          bd=1, width=10, state='readonly', textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=50)


etiqueta_costo_subtotal = Label(panel_costos,
                              text='Costo Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_subtotal.grid(row=0, column=2)
texto_costo_subtotal= Entry(panel_costos, font=('Dosis', 12, 'bold'),
                          bd=1, width=10, state='readonly', textvariable=var_subtotal)
texto_costo_subtotal.grid(row=0, column=3, padx=50)

etiqueta_costo_impuestos = Label(panel_costos,
                              text='Costo Impuestos',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_impuestos.grid(row=1, column=2)
texto_costo_impuestos= Entry(panel_costos, font=('Dosis', 12, 'bold'),
                          bd=1, width=10, state='readonly', textvariable=var_impuesto)
texto_costo_impuestos.grid(row=1, column=3, padx=50)


etiqueta_costo_total = Label(panel_costos,
                              text='Costo Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_total.grid(row=2, column=2)
texto_costo_total= Entry(panel_costos, font=('Dosis', 12, 'bold'),
                          bd=1, width=10, state='readonly', textvariable=var_total)
texto_costo_total.grid(row=2, column=3, padx=50)

# Botones
botones = ['Total', 'recibo', 'Guardar', 'Resetear']
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=('Dosis',12, 'bold'), fg='white', bg='azure4', bd=1, width=9)

    boton.grid(row=0, column=columnas)
    columnas += 1

# Área de Recibo
texto_recibo = Text(panel_recibo, font=('Dosis', 12, 'bold'), bd=1, width=42, height=10)
texto_recibo.grid(row=0, column=0)
# evitar que la pantalla se cierre
aplicacion.mainloop()