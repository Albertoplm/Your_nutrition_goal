from configuration import db, collection, collection2


def añadir_comdias_dia_total(usuario, alimentos_dia):
    """
    Function that returns all authors from the database
    """
    meal = alimentos_dia
    x = collection2.find_one_and_update({"nombre": usuario}, {"$push": {"meal": meal}}, upsert=False) 
    return x


def añadir_usuario(usuario, contraseña):
    """
    Function that returns all authors from the database
    """
    mydict = {"nombre": usuario, "contraseña": contraseña}
    x = collection2.insert_one(mydict)
    return "Useruario añadido"

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