# We'll make a view for the main window of the application with python using tkinter.
from tkinter import *
from tkinter import filedialog, messagebox
import os

class MainMenu():
    
    mainMenu = Tk()
    
    def __init__(self) -> None:
        self.mainMenu.title("Menu Principal") # title
        self.mainMenu.geometry("1450x725") # width x height
        self.mainMenu.config(bg="#1E1E1E") # bg = background
        self.mainMenu.iconbitmap(os.path.abspath("assets/usac_logo.ico")) # icon
        self.mainMenu.resizable(0,0) # resizable(width,height) 0 = False, 1 = True
        self.originalPath = ""
    
    def show(self):
        self.mainUI()
        self.mainMenu.mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
    
    def mainUI(self):
        
        titleFont = ("Arial", 30, "bold")

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
        mb.menu.add_command(label="Guardar", command=self.saveFile)
        mb.menu.add_command(label="Guardar como", command=self.saveFileAs)
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
        
        self.editor = Text(self.mainMenu, width=150, height=25, bg="white", fg="black", font=("Arial", 10))
        self.editor.grid(row=3, column=0, columnspan=5, padx=5)
        
        # block the console
        self.console = Text(self.mainMenu, width=150, height=10, bg="black", fg="white", state="disabled", font=("Arial", 10))
        self.console.grid(row=5, column=0, columnspan=5, padx=5)


    # set text to the console
    def setConsole(self, textIn):
        self.console.config(state="normal")
        self.console.insert(END, textIn)
        self.console.config(state="disabled")
        
    # set text to the editor
    def setEditor(self, text):
        self.editor.delete("1.0", END)
        self.editor.insert(END, text)
    
    # get text from the editor
    def getEditor(self):
        return self.editor.get("1.0", END)

    def openFile(self):
        fileSearch = filedialog.askopenfilename(
            initialdir="./",
            title="Open File",
            filetypes=(
                ("Text Files", "*.txt"),
                ("JSON Files", "*.json"),
                ("All Files", "*.*")
            )
        )
        
        filepath = os.path.abspath(fileSearch)
        self.originalPath = filepath
        # open the file and put it on the editor
        with open(filepath, "r") as file:
            file = file.read()
            self.setEditor(file)
            
        self.setConsole("File Upload: " + filepath + "\n")
        
    def saveFile(self):
        try:
            file = open(self.originalPath, "w",  encoding="utf-8", errors='ignore')
            file.write(self.getEditor())
            file.close()
            messagebox.showinfo(title="Aviso", message="Archivo guardado")
            self.setConsole("Archivo guardado correctamente: " + self.originalPath +"\n")
        except:
            messagebox.showinfo(title="Aviso", message="Ocurrio un error al guardar el archivo")
            
    
    def saveFileAs(self):
        try:
            fileSearch = filedialog.asksaveasfilename(
                initialdir="./",
                title="Save File",
                filetypes=(
                    ("Text Files", "*.txt"),
                    ("JSON Files", "*.json"),
                    ("All Files", "*.*")
                )
            )

            filepath = os.path.abspath(fileSearch)

            if os.path.exists(filepath):
                self.saveFile()
            else:
                self.originalPath = filepath
                # open the file and put it on the editor
                file = open(self.originalPath, "w",  encoding="utf-8", errors='ignore')
                file.write(self.getEditor())
                file.close()
                messagebox.showinfo(title="Aviso", message="Archivo creado y guardado")
                self.setConsole("Archivo creado correctamente: " + filepath + "\n") 
        except:
            messagebox.showinfo(title="Aviso", message="Ocurrio un error al guardar el archivo")