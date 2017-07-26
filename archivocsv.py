#!/usr/bin/env python
# encoding: utf-8

"""
<<<a.Código de preparación de los datos>>>
@author: Marylin Mattos
"""
import os, sys, io

def leer_archivo(datafile):
    """lee un archivo csv.

     Retorna  un array con el  número de tweets por categoría, además
     de su porcentaje. En su proceso llama al  método que está en el DAO

     Parámetros:
     datafile: Ruta que tiene el archivo que será leido

     Retornar:
     texto (list): Devuelve una lista de N textos que estan en la 1 posicion del archivo csv.

     Nota:Este codigo se puede reemplazar por  textos y categorias almacenadas en  base de datos

    """
    texto = []
    with open(datafile, "r") as f:
        header = f.readline().split(";")
        for line in f:
            fields = line.split(";")
            texto.append(fields[1])
        return  texto
