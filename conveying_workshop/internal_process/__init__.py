import csv
from random import randint


variables = None


def csv_to_dict(path: str):
    # Load the parameters from CVS file and transform it to a python dictionary
    res = {}
    with open(path) as f:
        csv_file = csv.reader(f)    # NOM,TYPE VARIABLES,TYPE DE DONNEES,ADRESSE,COMMENTAIRES
        for row in csv_file:
            res[row[0]] = {
                "value": None,
                "type": row[2],
                "address": row[3],
                "comment": row[4]
            }
    return res


def init():
    global variables
    variables = csv_to_dict("static/csv/ProductionLine-Variables-highlight2_fr.csv")
    for k in variables:
        if variables[k]["type"] == "Bool":
            if randint(0, 1) == 1:
                variables[k]["value"] = True
            else:
                variables[k]["value"] = False
        else:
            variables[k]["value"] = randint(0, 256)


def get_variables():
    return variables


def set_variable(data):
    variables[data["key"]]["value"] = data["value"]
