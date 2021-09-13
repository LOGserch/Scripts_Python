from tkinter import *
from tkinter import messagebox
from descargar_videos import GetYoutube

root = Tk()

root.title("App para descargar videos de youtube")
#root.geometry("650x350")

miFrame=Frame(root, width=600,height=500)
miFrame.pack()

text=Entry(miFrame)
text.grid(row=1,columns=1)

label=Label(miFrame,text="introduce una URL para descargar videos de youtube:")
label.grid(row=0,columns=1)

def getDownload():
    print("Download")


button=Button(root,text="Descargar", command=getDownload)
button.pack()

    

def infoAdicional():
    messagebox.showinfo("App videotube", "Version 1.0.0")

# def avisoLicencia():
#    messagebox.showwarning("-open source license-")

def salirAplicacion():
    valor = messagebox.askokcancel("salir de la app", "estas seguro que deseas salir?")
    if valor == True:
        root.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("reintentar", "la app no pudo cerrar la aplicacion")


barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="salir", command=salirAplicacion)


buscarMenu = Menu(barraMenu, tearoff=0)
#buscarMenu.add_command(label="licencia", command=avisoLicencia)
buscarMenu.add_command(label="acerca de", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="acerca de", menu=buscarMenu)

root.mainloop()