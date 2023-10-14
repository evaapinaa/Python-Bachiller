"""
------------------------------------------------------------PRESENTACIÓN----------------------------------------------------------------------------
 Vamos a realizar un programa con la finalidad de convertir las unidades de algunas magnitudes físicas en las del S.I.
 y, así, facilitar la resolución de múltiples ejercicios de Física y Química.
 Referencia, código final de la página: https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/widget-button-boton/
 ---------------------------------------------------------------------------------------------------------------------------------------------------
"""
from tkinter import *
from tkinter import messagebox as MessageBox  # Librería para poder crear un diálogo de más información.
import os    # Librería para acceder a funcionalidades dependientes del Sistema Operativo. (crear una carpeta, finalizar un proceso, etc)
import sys   # Librería que permite acceso a algunas variables usadas

root = Tk()
root.title("Unidades S.I.")   
root.iconbitmap("icono.ico") # Permite .ico o .xbm
root.resizable(0,0)    # Para que no se pueda minimizar la ventana. También sirve con (False, False)

tabla = PhotoImage(file="tabla.png")       # Admite los formatos: PNG, GIF y PGM)
label1 = Label(root, image=tabla)
label1.pack(side="top")  # Con pack(side="top") podemos situar la imagen arriba.

#def click():
    #label1.destroy()

# Creamos la función informacion. Sirve para mostrar un cuadro de diálogo informativo. Se le atribuirá a "Acerca del programa" en el menú.
def informacion():
    MessageBox.showinfo("Información", "Este programa está creado por Eva Pina Dubovtseva. "
                                       "Su finalidad es facilitar el cálculo de unidades en el S.I.")
# Código de referencia de la función resetProgram: https://python.hotexamples.com/es/examples/os/-/execl/python-execl-function-examples.html
# Sirve para volver a ejecutar el programa. (Uso del botón "Nuevo" del menú y "Reiniciar")
# Es necesario importar las librerías "os" y "sys" para su correcto funcionamiento.
def resetProgram():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# La función terminar sirve para cerrar la ventana del programa. Será atribuido al botón "Terminar" próximamente.
def terminar():
    root.destroy()

menubar = Menu(root)      # Nombramos un menú.
root.config(menu=menubar) # Lo asignamos a la base

filemenu = Menu(menubar, tearoff=0)   # Creamos un submenú.
filemenu.add_command(label="Nuevo", command=resetProgram) # Etiqueta "Nuevo" que cumple la función definida anteriormente de resetear el programa.
filemenu.add_command(label="Salir", command=root.destroy) # Etiqueta "Salir". El comando root.destroy sirve para cerrar la ventana. También sirve con root.quit.

infomenu = Menu(menubar, tearoff=0) # Creamos un segundo submenú.
infomenu.add_command(label="Acerca del programa", command=informacion)  # Agregamos un comando que cumplirá la función de "informacion" (mostrar el cuadro de diálogo).

menubar.add_cascade(label="Archivo", menu=filemenu)     # Le atribuimos la etiqueta de "Archivo" al primer submenú
menubar.add_cascade(label="Información", menu=infomenu) # Le atribuimos la etiqueta de "Información" al segundo submenú

# Asignamos como variables los números a introducir en el programa y el resultado de las operaciones que se realizarán.
n1 = StringVar()   # StringVar() declara variable de tipo cadena.
n2 = StringVar()
resultado = StringVar()

"""
-------------------------------------------FUNCIONES--BOTONES--Y--OPERACIONES----------------------------------------------------------------
 Definimos las funciones que queremos que ejecute cada botón de las magnitudes.
 Para los 5 botones que hay, prácticamente se repite el código.
 Lo que varía es la función de la operación y el texto de las etiquetas.
 ----------------------------------------------------------------------------------------------------------------------------------------------
"""
def masa():
    hectogramos = IntVar()
    decagramos = IntVar()
    gramos = IntVar()
    decigramos = IntVar()
    centigramos = IntVar()
    miligramos = IntVar()
    def kilogramos():
        if (hectogramos.get()):
            resultado.set(float(n1.get()) * 1/10)
            
        if (decagramos.get()):
            resultado.set(float(n1.get()) * 1/100)
            
        if (gramos.get()):
            resultado.set(float(n1.get()) * 1/1000)
            
        if (decigramos.get()):
            resultado.set(float(n1.get()) * 1/10000)
            
        if (centigramos.get()):
            resultado.set(float(n1.get()) * 1/100000)
            
        if (miligramos.get()):
            resultado.set(float(n1.get()) * 1/1000000)
    Label(root, text="Seleccionaste masa").pack()
    imagen = PhotoImage(file="gramos.gif")
    Label(root, image=imagen).pack()
    Label(root, text="Inserte el dato").pack()
    Entry(root, justify="center", textvariable=n1).pack()
#-----------------------------------CHECKBUTTONS------------------------------------------------------
    frame = Frame(root).pack(side=RIGHT)
    Checkbutton(frame, text="Hg", variable = hectogramos).place(x=83,y=655)
    Checkbutton(frame, text="Dag", variable = decagramos).place(x=167,y=655)
    Checkbutton(frame, text="g", variable = gramos).place(x=250,y=655)
    Checkbutton(frame, text="dg", variable = decigramos).place(x=332,y=655)
    Checkbutton(frame, text="cg", variable = centigramos).place(x=415,y=655)
    Checkbutton(frame, text="mg", variable = miligramos).place(x=498,y=655)
#------------------------------------------------------------------------------------------------------
    Label(root).pack()

    Label(root, text="Resultado (kilogramos)").pack()
    Entry(root, justify="center", textvariable=resultado, state="disabled").pack() # Con state="disabled" el texto será solo de lectura. No se puede editar.

    Label(root).pack() # Separación entre el Resultado y el botón "Convertir". Si no lo ponemos, queda muy junto.

    # Creamos botones para realizar diversas funciones que serán atribuidas con "command="
    # Fill="both": se alarga el botón y ocupa todo el espacio posible. Con expand también ocupa todo el espacio posible.
    # Con padx, pady, ipadx, ipady, podemos asignar números para la dimensión del botón. Horizontal y verticalmente.
    Button(root, text="Convertir", command=kilogramos).pack(fill="both", padx=5, pady=4, ipadx=6, ipady=5)
    Button(root, text="Reiniciar", command=resetProgram).pack(expand=1, fill="both", side="right", padx=5, pady=4, ipadx=6, ipady=5)
    Button(root, text="Terminar", command=terminar).pack(expand=1, fill="both", side="left", padx=5, pady=4, ipadx=6, ipady=5)
    root.mainloop() # Para cargar la imagen

def longitud():
    kilometros = IntVar()
    hectometros = IntVar()
    decametros = IntVar()
    decimetros = IntVar()
    centimetros = IntVar()
    milimetros = IntVar()
    def metros():
        if (kilometros.get()):
            resultado.set(float(n1.get()) * 1000)
            
        if (hectometros.get()):
            resultado.set(float(n1.get()) * 100)
            
        if (decametros.get()):
            resultado.set(float(n1.get()) * 10)
            
        if (decimetros.get()):
            resultado.set(float(n1.get()) * 1/10)
            
        if (centimetros.get()):
            resultado.set(float(n1.get()) * 1/100)
            
        if (milimetros.get()):
            resultado.set(float(n1.get()) * 1/1000)

    Label(root, text="Seleccionaste longitud").pack()
    imagen2 = PhotoImage(file="metros.gif")
    Label(root, image=imagen2).pack()
    Label(root, text="Inserte el dato").pack()
    Entry(root, justify="center", textvariable=n1).pack()

#-----------------------------------CHECKBUTTONS------------------------------------------------------
    frame = Frame(root).pack(side=RIGHT)
    Checkbutton(frame, text="Km", variable = kilometros).place(x=83,y=655)
    Checkbutton(frame, text="Hm", variable = hectometros).place(x=167,y=655)
    Checkbutton(frame, text="Dam", variable = decametros).place(x=248,y=655)
    Checkbutton(frame, text="dm", variable = decimetros).place(x=332,y=655)
    Checkbutton(frame, text="cm", variable = centimetros).place(x=415,y=655)
    Checkbutton(frame, text="mm", variable = milimetros).place(x=498,y=655)
#------------------------------------------------------------------------------------------------------
    Label(root).pack()
    Label(root, text="Resultado (metros)").pack()
    Entry(root, justify="center", textvariable=resultado, state="disabled").pack()
    Label(root).pack()
    Button(root, text="Convertir", command=metros).pack(fill="both", padx=5, pady=4, ipadx=6, ipady=5)
    Button(root, text="Reiniciar", command=resetProgram).pack(expand=1, fill="both", side="right", padx=5, pady=4, ipadx=6, ipady=5)
    Button(root, text="Terminar", command=terminar).pack(expand=1, fill="both", side="left", padx=5, pady=4, ipadx=6, ipady=5)
    root.mainloop()

def tiempo():
    años = IntVar()
    meses = IntVar()
    semanas = IntVar()
    dias = IntVar()
    horas= IntVar()
    minutos= IntVar()
    def segundos():
        if (años.get()):
            resultado.set(float(n1.get()) * 365 * 24 * 3600)
            
        if (meses.get()):
            resultado.set(float(n1.get()) * 30 * 24 * 3600)
        
        if (semanas.get()):
            resultado.set(float(n1.get()) * 7 * 24 * 3600)
            
        if (dias.get()):
            resultado.set(float(n1.get()) * 24 * 3600)
            
        if (horas.get()):
            resultado.set(float(n1.get()) * 3600)
            
        if (minutos.get()):
            resultado.set(float(n1.get()) * 60)

    Label(root, text="Seleccionaste tiempo").pack()
    Label(root, text="Inserte el dato").pack()
    Entry(root, justify="center", textvariable=n1).pack()
#-----------------------------------CHECKBUTTONS------------------------------------------------------
    frame = Frame(root).pack()
    Checkbutton(frame, text="años", variable = años).place(x=45,y=501)
    Checkbutton(frame, text="meses", variable = meses).place(x=130,y=501)
    Checkbutton(frame, text="semanas", variable = semanas).place(x=225,y=501)
    Checkbutton(frame, text="dias", variable = dias).place(x=330,y=501)
    Checkbutton(frame, text="horas", variable = horas).place(x=415,y=501)
    Checkbutton(frame, text="minutos", variable = minutos).place(x=500,y=501)
#------------------------------------------------------------------------------------------------------
    Label(root).pack()
    Label(root, text="Resultado (segundos)").pack()
    Entry(root, justify="center", textvariable=resultado, state="disabled").pack()
    Label(root).pack()

    Button(root, text="Convertir", command=segundos).pack(fill="both", padx=5, pady=4, ipadx=6, ipady=5)
    Button(root, text="Reiniciar", command=resetProgram).pack(expand=1, fill="both", side="right", padx=5, pady=4, ipadx=6, ipady=5)
    Button(root, text="Terminar", command=terminar).pack(expand=1, fill="both", side="left", padx=5, pady=4, ipadx=6, ipady=5)

def temperatura():
    def kelvin():
        resultado.set(float(n1.get()) + 273.15)

    Label(root, text="Seleccionaste temperatura").pack()
    Label(root, text="Inserte el dato (grados Celsius)").pack()
    Entry(root, justify="center", textvariable=n1).pack()
    Label(root, text="Resultado (Kelvin)").pack()
    Entry(root, justify="center", textvariable=resultado, state="disabled").pack()

    Label(root).pack()

    Button(root, text="Convertir", command=kelvin).pack(fill="both", padx=5, pady=4, ipadx=6, ipady=5)
    Button(root, text="Reiniciar", command=resetProgram).pack(expand=1, fill="both", side="right", padx=5, pady=4, ipadx=6, ipady=5)
    Button(root, text="Terminar", command=terminar).pack(expand=1, fill="both", side="left", padx=5, pady=4, ipadx=6, ipady=5)

def intensidad():
    def amperios():
        resultado.set(float(n1.get()) / float(n2.get()))  # Aquí empleamos la segunda variable (n2) definida anteriormente

    Label(root, text="Seleccionaste intensidad").pack()
    Label(root, text="Inserte el dato (voltaje)").pack()
    Entry(root, justify="center", textvariable=n1).pack()
    Label(root, text="Inserte el dato (resistencia)").pack()
    Entry(root, justify="center", textvariable=n2).pack()
    Label(root, text="Resultado (amperios)").pack()
    Entry(root, justify="center", textvariable=resultado, state="disabled").pack()

    Label(root).pack()

    Button(root, text="Convertir", command=amperios).pack(fill="both", padx=5, pady=4, ipadx=6, ipady=5)
    Button(root, text="Reiniciar", command=resetProgram).pack(expand=1, fill="both", side="right", padx=5, pady=4, ipadx=6, ipady=5)
    Button(root, text="Terminar", command=terminar).pack(expand=1, fill="both", side="left", padx=5, pady=4, ipadx=6, ipady=5)
"""
--------------------------------------------------BOTONES---------------------------------------------------------------------------
 Creamos los botones de las diferentes magnitudes y con "command" le asociamos su función correspondiente, definida anteriormente.
 Para el color de los botones, se usa bg="color", referencia: https://pythonexamples.org/python-tkinter-button-background-color/
 También se pueden escribir los códigos de color hex (v.gr. #31EC1E), página usada: https://htmlcolorcodes.com/es/
 -----------------------------------------------------------------------------------------------------------------------------------
"""
Button(root, text="Masa", command=masa, bg="red").pack(fill="both", padx=5, pady=4, ipadx=6, ipady=5)
Button(root, text="Longitud", command=longitud, bg="#31EC1E").pack(fill="both", padx=5, pady=4, ipadx=6, ipady=5)
Button(root, text="Tiempo", command=tiempo, bg="blue").pack(fill="both", padx=5, pady=4, ipadx=6, ipady=5)
Button(root, text="Temperatura", command=temperatura, bg="orange").pack(fill="both", padx=5, pady=4, ipadx=6, ipady=5)
Button(root, text="Intensidad Corriente", command=intensidad, bg="yellow").pack(fill="both", padx=5, pady=4, ipadx=6, ipady=5)

root.mainloop()
