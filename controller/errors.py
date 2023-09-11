import json
from controller.lexer import ErrorList

# create a json file with the errors from array

def processErrors():
    # create a dictionary
    error_dict = dict()
    error_dict['errors'] = []

    # create a json file
    with open('errors.json', 'w') as error_file:
        for index, error in enumerate(ErrorList):
            error_dict['errors'].append({
                "No.": index + 1,
                "descripcion": {
                    "lexema": error._lexema,
                    "tipo": "Error Lexico",
                    "fila": error._row,
                    "columna": error._column
                }
            })
        json.dump(error_dict, error_file, indent=4)