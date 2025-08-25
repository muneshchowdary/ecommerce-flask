import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename
from pymongo import MongoClient

# Option A: Hardcode the connection string (not recommended for production)
#client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority")

# Option B: Use an environment variable (recommended for security)
mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# MongoDB setup (use Atlas for free cloud hosting)
client = MongoClient("mongodb+srv://<your-username>:<your-password>@cluster0.mongodb.net/?retryWrites=true&w=majority")
db = client['ecommerce']
products = db['products']

@app.route('/')
def index():
    prod_list = list(products.find())
    return render_template('index.html', products=prod_list)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_product(id):
    prod = products.find_one({"_id": ObjectId(id)})
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
        products.update_one({"_id": ObjectId(id)}, {"$set": update})
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
        products.insert_one(prod)
        return redirect(url_for('index'))
    return render_template('edit_product.html', product=None)

@app.route('/delete/<id>')
def delete_product(id):
    products.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)