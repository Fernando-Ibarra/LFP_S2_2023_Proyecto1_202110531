from view.mainView import MainMenu
from controller.repl import start_repl
from controller.graphs import make_graphviz
from controller.parser import operationList

def run():
    # MainMenu()
    start_repl()
    for ope in operationList:
        print(ope.traverse())
        print("")
    make_graphviz()

if __name__=='__main__':
    run()