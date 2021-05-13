from configuration import db, collection


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

def buscar_alimentos(nombre):
    """
    Function that returns all authors from the database
    """
    query = {"Nombre": {"$regex":f"{nombre}"} and {"$regex":f"{nombre.capitalize()}"}}
    food = list(collection.find((query)))
    return food

def buscar_kcal(kcal):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": kcal}
    food = list(collection.find((query)))
    return food

def buscar_kcalup(kcal):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": {"$gte": kcal}}
    food = list(collection.find((query)))
    return food

def buscar_kcallow(kcal):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": {"$lte": kcal}}
    food = list(collection.find((query)))
    return food

def buscar_grasas(grasa):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": grasa}
    food = list(collection.find((query)))
    return food

def buscar_grasasup(grasa):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": {"$gte": grasas}}
    food = list(collection.find((query)))
    return food

def buscar_grasaslow(grasa):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": {"$lte": grasas}}
    food = list(collection.find((query)))
    return food

def buscar_proteina(proteina):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": proteina}
    food = list(collection.find((query)))
    return food

def buscar_proteinaup(proteina):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": {"$gte":proteina}}
    food = list(collection.find((query)))
    return food

def buscar_proteinalow(proteina):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": {"$lte":proteina}}
    food = list(collection.find((query)))
    return food

def buscar_carbohidratos(carbohidratos):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": carbohidratos}
    food = list(collection.find((query)))
    return food

def buscar_carbohidratosup(carbohidratos):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": {"$gte":carbohidratos}}
    food = list(collection.find((query)))
    return food

def buscar_carbohidratoslow(carbohidratos):
    """
    Function that returns all authors from the database
    """
    query = {"Energia(kcal)": {"$lte":carbohidratos}}
    food = list(collection.find((query)))
    return food
