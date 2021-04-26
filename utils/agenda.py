#!/usr/bin/python3
# agenda
# descrip
# jaz 04/12/21

from dataclasses import dataclass
import sys
import calendar as clndr

@dataclass
class Evento:
    dono: str
    dia: int
    mes: int
    ano: int
    nome: str
    descript: str

def printarCalendario(ano, mes):
    print(clndr.month(ano, mes))

def abrirAgenda():
    agenda = open("agenda.txt", "a+")

    


argc = len(sys.argv)

comando = str(sys.argv[1])

if comando == "mostrar":
    argumento = str(sys.argv[2])
    if argumento == "calendario":
        mes = int(sys.argv[3])
        if argc < 5:
            ano = 2021
        else:
            ano = int(sys.argv[4])
        printarCalendario(ano, mes)
    elif argumento == "eventos":
        agenda.seek(0)


#agenda.seek(0) ## retorna ao comeco do arquivo



agenda.close()
