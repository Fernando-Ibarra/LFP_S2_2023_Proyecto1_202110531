# We'll make a view for the main window of the application with python using tkinter.
from tkinter import *
from tkinter import filedialog
import os

class MainMenu():
    
    mainMenu = Tk()
    
    def __init__(self) -> None:
        self.mainMenu.title("Menu Principal") # title
        self.mainMenu.geometry("1450x725") # width x height
        self.mainMenu.config(bg="#1E1E1E") # bg = background
        self.mainMenu.iconbitmap(os.path.abspath("assets/usac_logo.ico")) # icon
        self.mainMenu.resizable(0,0) # resizable(width,height) 0 = False, 1 = True
        self.mainUI()
        self.mainMenu.mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.    
    
    def openFile(self):
        print("open file")
        file = filedialog.askopenfilename(
            initialdir="./",
            title="Open File",
            filetypes=(
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            )
        )
        print(file)
    
    def mainUI(self):
        
        titleFont = ("Arial", 30, "bold")
        
        # label - title
        Label(
            self.mainMenu, 
            text="Aplicación Numérica con Análisis Léxico",
            font=titleFont,
            bg="#1E1E1E",
            fg="white"
        ).grid(
            row=0,
            column=0,
            columnspan=10,
            ipadx=300,
            pady=10
        )
        
        # Menubutton - file
        mb = Menubutton(self.mainMenu, text="Archivo")
        mb.grid(row=2, column=0)
        mb.menu = Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        mb.menu.add_command(label="Abrir", command=self.openFile)
        mb.menu.add_command(label="Guardar")
        mb.menu.add_command(label="Guardar como")
        mb.menu.add_command(label="Salir", command=self.mainMenu.quit)
        
        # Button 1 - Start to analyze the file
        Button(
            self.mainMenu,
            text="Analizar", 
            width=10,
        ).grid(
            row=2,
            column=1,
        )
        
        # Button 2 - Generate the errors
        Button(
            self.mainMenu,
            text="Errores", 
            width=10,
        ).grid(
            row=2,
            column=2,
        )
        
        # Button 3 - Generate the report Graphviz
        Button(
            self.mainMenu,
            text="Reporte", 
            width=10,
        ).grid(
            row=2,
            column=3,
        )