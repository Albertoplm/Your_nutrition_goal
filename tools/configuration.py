import os
#import dotenv
from pymongo import MongoClient
import dns

#dotenv.load_dotenv()

#dburl = os.getenv("URL")
dburl = 'mongodb+srv://dbuser:api2021@cluster0.q59hz.mongodb.net/nutrition'
print(dburl)
if not dburl:
    raise ValueError("no tienes url mongodb")

#Vamos a conectar con la base de datos
client = MongoClient(dburl)
db = client.get_database()
collection = db["alimentos"]
collection2 = db["usuarios"]
