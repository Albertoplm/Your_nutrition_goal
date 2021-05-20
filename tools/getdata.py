from configuration import db, collection, collection2
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime

def meal_date(usuario):
    '''Esta función recibe el usuario y devuelve los días'''

    a = list(collection2.find({"nombre": usuario}, {"_id": 0, "meal_date": 1}))
    date_lis = a[0]['date']
    date = []
    for a in list(date_lis):
        date.append(str(a).split()[0])
    return date

def weight_date(usuario):
    '''Esta función recibe el usuario y devuelve los días'''

    a = list(collection2.find({"nombre": usuario}, {"_id": 0, "weight_date": 1}))
    date_lis = a[0]['date']
    date = []
    for a in list(date_lis):
        date.append(str(a).split()[0])
    return date

def kcal_totalesxdia(usuario):
    '''Esta función recibe el usuario y devuelve las calorías por día'''

    a = list(collection2.find({"nombre": usuario}, {"_id": 0, "meal": 1}))
    meal_lis = a[0]['meal']
    n = len(meal_lis)
    lis = []
    suma = 0
    lis2 = []
    for i in range(n):
        b = meal_lis[i]
        for j in b:
            suma = suma + j['Energia(kcal)']
        lis.append(round(suma))
    lis2.append(lis[0])
    for n in range(0,len(lis)-1):
        lis2.append(lis[n+1]-lis[n])
    return lis2

def top_alimentos(usuario):
    a = list(collection2.find({"nombre": usuario}, {"_id": 0, "meal": 1}))
    meal_lis = a[0]['meal']
    n = len(meal_lis)
    lis = []
    for i in range(n):
            b = meal_lis[i]
            lis.append(b)
    peso = []
    for i in lis:
        for i1 in range(len(i)):
            peso.append(i[i1]["Nombre"])
    peso = pd.DataFrame(peso)
    count = peso.value_counts()
    top = count.head(10)
    return top


def media_historico(usuario):
    a = list(collection2.find({"nombre": usuario}, {"_id": 0, "meal": 1}))
    meal_lis = a[0]['meal']
    n = len(meal_lis)
    energia = []
    grasas = []
    proteina = []
    carbohidratos = []
    for n2 in range(n):
        for n3 in range(len(meal_lis[n2])):
            energia.append(meal_lis[n2][n3]["Energia(kcal)"])
            grasas.append(meal_lis[n2][n3]["Grasas"])
            proteina.append(meal_lis[n2][n3]["Proteina"])
            carbohidratos.append(meal_lis[n2][n3]["Carbohidratos"])
    data = {
        'Energia(kcal)': round(np.mean(energia)),
        'Grasas': round(np.mean(grasas)),
        'Proteina': round(np.mean(proteina)),
        'Carbohidratos': round(np.mean(carbohidratos))}
    data1 = pd.DataFrame(list(data.items()), columns = ['Macronutrientes','Media'])
    return data1

def dias_comida(usuario):
    a = list(collection2.find({"nombre": usuario}, {"_id": 0, "meal": 1}))
    meal_lis = a[0]['meal']
    return len(meal_lis)

def evolucion_PyG(usuario):
    try:
        a = list(collection2.find({"nombre": usuario}, {"_id": 0, "weight": 1}))
        weight_lis = a[0]['weight']
        n = len(weight_lis)
        lis = []
        for i in range(n):
                b = weight_lis[i]
                lis.append(b)
        lis
        peso = []
        for i in lis:
            peso.append(i[1])
        return peso
    except KeyError:
        b = "No has introducido ningún dato todavia"
        return st.write(b)

        
def evolucion_peso(usuario):
    try:
        a = list(collection2.find({"nombre": usuario}, {"_id": 0, "weight": 1}))
        weight_lis = a[0]['weight']
        n = len(weight_lis)
        lis = []
        for i in range(n):
                b = weight_lis[i]
                lis.append(b)
        lis
        peso = []
        for i in lis:
            peso.append(i[0])
        return peso
    except KeyError:
        b = "No has introducido ningún dato todavia"
        return st.write(b)


def añadir_comdias_dia_total(usuario, alimentos_dia):
    """
    Function that returns all authors from the database
    """
    meal = alimentos_dia
    x = collection2.find_one_and_update({"nombre": usuario}, {"$push": {"meal": meal, "meal_date": datetime.now()}}, upsert=False) 
    return x

def añadir_peso_semanal(usuario, peso, cambio):
    """
    Function that returns all authors from the database
    """
    weight = [peso, cambio]
    x = collection2.find_one_and_update({"nombre": usuario}, {"$push": {"weight": weight, "weight_date": datetime.now()}}, upsert=False) 
    return "Sus datos han sido añadidos"


def comprobar_usuario(usuario):
    """
    Function that returns all authors from the database
    """
    x = list(collection2.find({"nombre": usuario}, {"_id": 0, "nombre": 1}))
    return x


def añadir_usuario(usuario, contraseña):
    """
    Function that returns all authors from the database
    """
    mydict = {"nombre": usuario, "contraseña": contraseña}
    x = collection2.insert_one(mydict)
    return "Useruario añadido"

def change_password(usuario, contraseña):
    """
    Function that returns all authors from the database
    """
    key = {"nombre": usuario}
    mydict = {'$set': {"contraseña": contraseña}}
    x = collection2.update(key,mydict, upsert=False)
    return "Contraseña cambiada correctamente"

def informacion_sesion(usuario, contraseña):
    """
    Function that returns all authors from the database
    """
    query = {"nombre": usuario, "contraseña": contraseña}
    informacion_usuario = list(collection2.find(query, {"_id": 0, "nombre":1, "contraseña":1}))
    return informacion_usuario

def iniciar_sesion(usuario, contraseña):
    """
    Function that returns all authors from the database
    """
    query = {"nombre": usuario, "contraseña": contraseña}
    informacion_usuario = list(collection2.find(query, {"_id": 0}))
    return informacion_usuario

def ver_usuarios():
    """
    Function that returns all authors from the database
    """
    query = {}
    usuarios = list(collection2.find(query, {"_id": 0}))
    return usuarios


def nombre_alimentos():
    """
    Function that returns all authors from the database
    """
    query = {}
    food = list(collection.find(query, {"_id": 0, "Nombre": 1}))
    return food



def buscar_comidas_usuario(alimento1, alimento2=0, alimento3=0, alimento4=0, alimento5=0, alimento6=0, alimento7=0):
    """
    Function that returns all authors from the database
    """
    query = {"$or":[{"Nombre": alimento1}, {"Nombre": alimento2}, {"Nombre": alimento3}, {"Nombre": alimento4}, {"Nombre": alimento5}, {"Nombre": alimento6}, {"Nombre": alimento7}]}
    food = list(collection.find(query, {"_id": 0, "Name": 0}))
    return food

def buscar_alimento_usuario(alimento):
    """
    Function that returns all authors from the database
    """
    query = {"Nombre": alimento}
    food = list(collection.find(query, {"_id": 0, "Name": 0}))
    return food