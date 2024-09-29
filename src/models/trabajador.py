import pandas as pd
from datetime import datetime
from docx import Document
from services import service_logic
import os

"""
VARS WORD:
nomb_trab
apell_trab
fech_trab
rut_trab
tip_perm
tiempo_perm
"""

class Trabajador:
    def __init__(self, nombre, apellido, rut, fecha, tipo_permiso, tiempo_permiso):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.fecha = fecha
        self.tipo_permiso = tipo_permiso
        self.tiempo_permiso = tiempo_permiso

    def armar_documento(self):
        try:
            trabajadores = service_logic.consultar_bd()
            doc = service_logic.obtener_word()
            for index, trabajador in trabajadores.iterrows():
                for paragraph in doc.paragraphs:
                    if 'nomb_trab' in paragraph.text:
                        paragraph.text = paragraph.text.replace('nomb_trab', self.nombre)
                    elif 'apell_trab' in paragraph.text:
                        paragraph.text = paragraph.text.replace('apell_trab', self.apellido)
                    elif 'rut_trab' in paragraph.text:
                        paragraph.text = paragraph.text.replace('rut_trab', self.rut)
                    elif 'fech_trab' in paragraph.text:
                        paragraph.text = paragraph.text.replace('fech_trab', self.fecha)
                    elif 'tip_perm' in paragraph.text:
                        paragraph.text = paragraph.text.replace('tip_perm', self.tipo_permiso)
                    elif 'tiempo_perm' in paragraph.text:
                        paragraph.text = paragraph.text.replace('tiempo_perm', self.tiempo_permiso)
            output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'output')
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_path = os.path.join(output_dir, f'permiso_{self.nombre}_{self.apellido}_{self.tiempo_permiso}.docx')
            doc.save(output_path)
            print(f'Documento generado: permiso_{self.nombre}_{self.apellido}_{self.tiempo_permiso}.docx')
        except Exception as e:
            print(e)

    def armar_documento_por_entrada(self):
        try:
            doc = service_logic.obtener_word()
            for paragraph in doc.paragraphs:
                if 'nomb_trab' in paragraph.text:
                    paragraph.text = paragraph.text.replace('nomb_trab', self.nombre)
                elif 'apell_trab' in paragraph.text:
                    paragraph.text = paragraph.text.replace('apell_trab', self.apellido) #REV
                elif 'rut_trab' in paragraph.text:
                    paragraph.text = paragraph.text.replace('rut_trab', self.rut)
                elif 'fech_trab' in paragraph.text:
                    paragraph.text = paragraph.text.replace('fech_trab', self.fecha) #REV
                elif 'tip_perm' in paragraph.text:
                    paragraph.text = paragraph.text.replace('tip_perm', self.tipo_permiso)
                elif 'tiempo_perm' in paragraph.text:
                    paragraph.text = paragraph.text.replace('tiempo_perm', self.tiempo_permiso)
            # doc.save(f'permiso_{self.nombre}_{self.apellido}_{self.tiempo_permiso}.docx')
            # print(f'Documento generado. Nombre documento: permiso_{self.nombre}_{self.apellido}.docx')

            output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'output')
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_path = os.path.join(output_dir, f'permiso_{self.nombre}_{self.apellido}_{self.tiempo_permiso}.docx')
            doc.save(output_path)
            print(f'Documento generado. Nombre documento: {output_path}')

        except Exception as e:
            print("")

    def imprime_trabajador(self):
        print(f'Tabajador instanciado:\nNombre: {self.nombre}\nApellido: {self.apellido}\n')