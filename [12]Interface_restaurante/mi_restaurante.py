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





# evitar que la pantalla se cierre
aplicacion.mainloop()