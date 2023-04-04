import os
import io
import zipfile
import glob
import traceback
from zipfile import ZipFile
import numpy as np
import pandas as pd
from PIL import Image
from flask import Flask, render_template, request
from embeddings import get_embeddings
from pstable import cursor, conn
import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/upload', methods = ["GET", "POST"])
def upload():
    file = request.files['file']
    if file.filename == '':
        return "No File Selected"

    folder_name = "uploads"
    os.makedirs(folder_name, exist_ok=True)
    with ZipFile(file, 'r') as z:
        z.extractall(folder_name)
        
        images = os.path.join(folder_name, 'test')
        list_img = os.listdir(images)
        if len(images)>0:
            for i in range(len(list_img)):
                image = os.path.join(images, list_img[i])
                print(image)
                embed =get_embeddings(image)
                img_name = image.split('\\')[-1]
                img_name =img_name.split('.')[0]

                #Adding Data to PostgreSql 
                cursor.execute("INSERT INTO image_embaddings(NAME, Embadings,Path) VALUES (%s, %s, %s)", (img_name, str(embed), image))
                conn.commit()

                # Adding data to Mongo DB (Non-Relational)
                myclient = pymongo.MongoClient("mongodb://localhost:27017")
                client = pymongo.MongoClient()
                db = client.dummy
                imagesdb = db.data

                im = Image.open('pt.png')

                image_bytes = io.BytesIO()
                im.save(image_bytes, format =('png') )

                imagej = {
                    'name': image ,
                    'data': image_bytes.getvalue()
                }

                image_id = imagesdb.insert_one(imagej).inserted_id


        return "File Uploaded Successfully!! Also Saved to Databases"





if __name__ == '__main__':
    app.run(debug=True)


#code is taking a flask Api we upload a zip folder through flask Api unzip the folder 
# take files from folder add all these files to postgre table and and its json to MongoDB