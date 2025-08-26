import os
import urllib.parse
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename

# Encode username and password
username = urllib.parse.quote_plus("sireesha")
password = urllib.parse.quote_plus("fOEJBLnUuWJPIgEu")

# MongoDB connection
mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.gclepan.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)

# Flask app setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Database & Collection
db = client['sample_mflix']
collection = db['movies']

@app.route('/')
def index():
    docs = list(collection.find())
    return render_template('index.html', products=docs)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_product(id):
    prod = collection.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        desc = request.form['description']
        update = {"name": name, "price": price, "description": desc}

        if 'image' in request.files and request.files['image'].filename:
            image = request.files['image']
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            update["image"] = filename

        collection.update_one({"_id": ObjectId(id)}, {"$set": update})
        return redirect(url_for('index'))

    return render_template('edit_product.html', product=prod)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        desc = request.form['description']
        prod = {"name": name, "price": price, "description": desc}

        if 'image' in request.files and request.files['image'].filename:
            image = request.files['image']
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            prod["image"] = filename

        collection.insert_one(prod)
        return redirect(url_for('index'))

    return render_template('edit_product.html', product=None)

@app.route('/delete/<id>')
def delete_product(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
