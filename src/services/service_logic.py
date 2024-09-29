import pandas as pd
from datetime import datetime
from docx import Document
from models import trabajador as tr

"""
VARS WORD:
nomb_trab
apell_trab
fech_trab
rut_trab
tip_perm
tiempo_perm
"""

"""
MÉTODOS
"""
def consultar_bd():
    df = pd.read_csv(r'src\data\input\lista.csv', sep=';')
    return df

def instancia_automática(e=None):
    try:
        trabajadores = consultar_bd()
        for index, trab in trabajadores.iterrows():
            trabajador = tr.Trabajador(trab['nombre'], trab['apellido'], trab['rut'], trab['fecha'], trab['tipo_permiso'], trab['tiempo_permiso'])
            trabajador.armar_documento()
    except Exception as e:
        print(e)


def obtener_word():
    doc = Document(r'src\data\input\permiso.docx')
    return doc

def obtener_entrada():
    nombre = input("Ingrese nombre(s) de trabajador:")
    apellido = input("Ingrese apellido(s) de trabajador:")
    #Validar rut
    rut = input("Ingrese RUT del trabajador:")
    while True:
        try:
            fecha_ingresada = input("Ingrese la fecha con formato dd-mm-aaaa:")
            fecha =  datetime.strptime(fecha_ingresada, "%d-%m-%Y").date()
            break
        except Exception as e:
            print(f'\n***Por favor reingrese con el formato solicitado.*** {e}')
    tipo_permiso = input("Ingrese tipo de permiso:")
    tiempo_permiso = input("Ingrese tiempo de permiso:")
    #Probablemente tenga que cambiar este que viene por el def armar documento.
    trabajador = tr.Trabajador(nombre, apellido, rut, fecha, tipo_permiso, tiempo_permiso)
    trabajador.armar_documento_por_entrada()