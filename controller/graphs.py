import graphviz as gv

from controller.parser import operationList
from model.Operation import Operation

correlative = 0

def make_graphviz():
    dot = gv.Digraph('Operaciones', format='svg') 

    for ope in operationList:
        ope.getResult()
    
    for  ope in operationList:
        traverse_graph(dot, ope)
               
            
    dot.render('graphs.gv')
    dot.view()

def traverse_graph(dot, ope):

    # declare parent
    global correlative
    parentCorrelative = correlative
    nodeDefinition(dot, correlative, f"{ ope.operation }\l{ str(ope.result) }")
    correlative += 1


    # declare value1
    leftCorrelative = correlative
    if isinstance(ope.value1, Operation):
        traverse_graph(dot, ope.value1)
        edgeDefinition(dot, parentCorrelative, leftCorrelative)
    else:
        if ope.value1 is not None:
            nodeDefinition(dot, correlative, str(ope.value1))
            correlative += 1
            edgeDefinition(dot, parentCorrelative, leftCorrelative)


    # declare val2
    rightCorrelative = correlative
    if isinstance(ope.value2, Operation):
        traverse_graph(dot, ope.value2)
        edgeDefinition(dot, parentCorrelative, rightCorrelative)
    else:
        if ope.value2 is not None:
            nodeDefinition(dot, correlative, str(ope.value2))
            correlative += 1
            edgeDefinition(dot, parentCorrelative, rightCorrelative)


def nodeDefinition(dot, correlative, label):
    dot.node(f'B{ correlative }', f'{ label }')

def edgeDefinition(dot, correlative, correlative2):
    dot.edge(f'B{ correlative }', f'B{ correlative2 }')