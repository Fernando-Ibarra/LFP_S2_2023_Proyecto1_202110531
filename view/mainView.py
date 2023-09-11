from tkinter import *
from tkinter import filedialog, messagebox
import os

from controller.repl import start_repl
from controller.errors import processErrors
from controller.graphs import make_graphviz
from controller.parser import operationList

class MainMenu():
    
    mainMenu = Tk()
    
    def __init__(self) -> None:
        self.mainMenu.title("Menu Principal") # title
        self.mainMenu.geometry("1150x740") # width x height
        self.mainMenu.config(bg="#1E1E1E") # bg = background
        self.mainMenu.iconbitmap(os.path.abspath("assets/usac_logo.ico")) # icon
        self.mainMenu.resizable(0,0) # resizable(width,height) 0 = False, 1 = True
        self.originalPath = ""
        self.mainUI()
        self.mainMenu.mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.

    def mainUI(self):
        
        titleFont = ("Arial", 30, "bold")

        Label(
            self.mainMenu, 
            text="Aplicación Numérica con Análisis Léxico",
            font=titleFont,
            bg="#1E1E1E",
            fg="white",
        ).grid(
            row=0,
            column=0,
            columnspan=10,
            ipadx=200,
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
            command=self.analyzeFile
        ).grid(
            row=2,
            column=1
        )
        
        # Button 2 - Generate the errors
        Button(
            self.mainMenu,
            text="Errores", 
            width=10,
            command=self.generateErrors
        ).grid(
            row=2,
            column=2,
        )
        
        # Button 3 - Generate the report Graphviz
        Button(
            self.mainMenu,
            text="Reporte", 
            width=10,
            command=self.generateGraphviz
        ).grid(
            row=2,
            column=3,
        )
        
        self.emptyRow2 = Label(self.mainMenu, text="", bg="#1E1E1E", fg="white")
        self.emptyRow2.grid(row=3, column=0, columnspan=10, ipadx=5, ipady=5)
        
        
        self.editor = Text(self.mainMenu, width=150, height=25, bg="white", fg="black", font=("Arial", 10))
        self.editor.grid(row=4, column=0, columnspan=10, padx=5, ipadx=5, ipady=5)
        
        self.emptyRow = Label(self.mainMenu, text="", bg="#1E1E1E", fg="white")
        self.emptyRow.grid(row=5, column=0, columnspan=10, ipadx=5, ipady=5)
        
        # block the console
        self.console = Text(self.mainMenu, width=150, height=7, bg="black", fg="white", state="disabled", font=("Arial", 10))
        self.console.grid(row=6, column=0, columnspan=10, padx=5, ipadx=5, ipady=5)


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
        return str(self.editor.get("1.0", END))

    def analyzeFile(self):
        try:
            jsonString = self.getEditor()
            tokens = start_repl(jsonString)
            for token in tokens:
                self.setConsole(str(token))
                self.setConsole("\n")

            for ope in operationList:
                self.setConsole(str(ope.traverse()))
                self.setConsole("\n")
        except:
            messagebox.showinfo(title="Aviso", message="Ocurrio un error al analizar el archivo")
            
    def generateErrors(self):
        try:
            processErrors()
            dir_path = os.path.dirname(os.path.realpath(__file__))
            self.setConsole("Archivo de errores generado correctamente: " + dir_path.replace("\\view", '') + "\errors.json" + "\n")
        except:
            messagebox.showinfo(title="Aviso", message="Ocurrio un error al generar el archivo de errores")
        
    def generateGraphviz(self):
        # try:
        #     make_graphviz()
        #     dir_path = os.path.dirname(os.path.realpath(__file__))
        #     self.setConsole("Archivo de reporte generado correctamente: " + dir_path.replace("\\view", '') + "\graphs.gv" + "\n")
        # except:
        #     messagebox.showinfo(title="Aviso", message="Ocurrio un error al generar el reporte")
        make_graphviz()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.setConsole("Archivo de reporte generado correctamente: " + dir_path.replace("\\view", '') + "\graphs.gv" + "\n")

    def openFile(self):
        try:
            fileSearch = filedialog.askopenfilename(
                initialdir="./",
                title="Open File",
                filetypes=(
                    ("JSON Files", "*.json"),
                    ("Text Files", "*.txt"),
                    ("All Files", "*.*")
                )
            )

            filepath = os.path.abspath(fileSearch)
            self.originalPath = filepath
            # open the file and put it on the editor
            with open(filepath, "r") as file:
                file = file.read()
                self.setEditor(file)

            self.setConsole("Archivo cargado correctamente: " + filepath + "\n")
        except:
            messagebox.showinfo(title="Aviso", message="Ocurrio un error al abrir el archivo")
        
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