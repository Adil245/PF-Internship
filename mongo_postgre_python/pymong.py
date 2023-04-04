import pymongo
from PIL import Image
import io
from pymongo import MongoClient

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# mydb = myclient["dummy"]
# mycoll = mydb["data"]
myclient = pymongo.MongoClient("mongodb://localhost:27017")
client = pymongo.MongoClient()
db = client.dummy
images = db.data

im = Image.open('pt.png')
formate1 = ['JPEG', 'png']
image_bytes = io.BytesIO()
im.save(image_bytes, format='JPEG , png')

image = {
    'data': image_bytes.getvalue()
}

image_id = images.insert_one(image).inserted_id

# print(myclient.list_database_names())
# print('DB created Sucessfuly..')

# dblist = myclient.list_database_names()
# if "dummy" in dblist:
#   print("The database exists.")








