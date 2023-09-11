import graphviz as gv

from controller.parser import operationList, configurationSettings
from model.Operation import Operation

correlative = 0

def make_graphviz():
    dot = gv.Digraph('Operaciones', format='svg')
    dot.attr(label=f'{ configurationSettings.title }', fontcolor='black', fontsize='30', fontname='arial', style='filled', fillcolor='white', rankdir='TB', size='5,8')

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
    nodeDefinition(dot, correlative, f"{ ope.operation }\l{ str(ope.result) }", f"{ configurationSettings.getBackgroundColor() }", f"{ configurationSettings.getFontStyle() }", f"{ configurationSettings.getStyle() }")
    correlative += 1


    # declare value1
    leftCorrelative = correlative
    if isinstance(ope.value1, Operation):
        traverse_graph(dot, ope.value1)
        edgeDefinition(dot, parentCorrelative, leftCorrelative)
    else:
        if ope.value1 is not None:
            nodeDefinition(dot, correlative, str(ope.value1), f"{ configurationSettings.getBackgroundColor() }",  f"{ configurationSettings.getFontStyle() }", f"{ configurationSettings.getStyle() }")
            correlative += 1
            edgeDefinition(dot, parentCorrelative, leftCorrelative)


    # declare val2
    rightCorrelative = correlative
    if isinstance(ope.value2, Operation):
        traverse_graph(dot, ope.value2)
        edgeDefinition(dot, parentCorrelative, rightCorrelative)
    else:
        if ope.value2 is not None:
            nodeDefinition(dot, correlative, str(ope.value2), f"{ configurationSettings.getBackgroundColor() }",  f"{ configurationSettings.getFontStyle() }", f"{ configurationSettings.getStyle() }")
            correlative += 1
            edgeDefinition(dot, parentCorrelative, rightCorrelative)


def nodeDefinition(dot, correlative, label, fillcolor, fontcolor, shape):
    dot.node(f'B{ correlative }', f'{ label }', fillcolor=f'{ fillcolor }', style='filled', fontcolor=f'{ fontcolor }', shape=f'{ shape }')

def edgeDefinition(dot, correlative, correlative2):
    dot.edge(f'B{ correlative }', f'B{ correlative2 }')