import os
import shutil
import csv
import random
FILE_NAME = 'students.csv'
DIRECTORIO_BASE = os.getcwd()
DIRECTORIO_ANALIZAR = os.path.join(DIRECTORIO_BASE , 'data')
DIRECTORIOS_DATA = os.listdir(DIRECTORIO_ANALIZAR)
folders_names = []


def open_file (file_name):
    folders=[]
    with open(file_name, 'r') as file:
        for line in file:
            if not 'Name' in line:
                folders.append(line.split(',')[0].lower())
    return folders

def create_folders(folders):
    for carpeta in folders:
        os.mkdir(carpeta)




def filter_files():
    for elemnt in DIRECTORIOS_DATA:
        direct_element = os.path.join(DIRECTORIO_ANALIZAR, elemnt)
        if 'game' in elemnt and os.path.isdir(direct_element):
            shutil.move(direct_element , 'games')
        if 'Python' in elemnt and '.pdf' in elemnt:
            shutil.move(direct_element , 'tutorials')




folders_names = open_file(FILE_NAME)
create_folders(folders_names)
filter_files()



