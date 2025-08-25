# Ecommerce Flask App

This is a simple e-commerce site built with Flask and MongoDB. It allows you to add, edit, and delete products, including uploading images.

## Setup

1. Clone the repo:

    ```
    git clone https://github.com/muneshchowdary/ecommerce-flask.git
    cd ecommerce-flask
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Configure MongoDB:
    - Create a free cluster on [MongoDB Atlas](https://www.mongodb.com/atlas).
    - Replace the connection string in `app.py` with your own credentials:
      ```
      client = MongoClient("mongodb+srv://<your-username>:<your-password>@cluster0.mongodb.net/?retryWrites=true&w=majority")
      ```

4. Run the app locally:

    ```
    python app.py
    ```

## Deploy on Render.com (Free)

1. Create a free account at [Render](https://render.com/).
2. Create a new Web Service, connect to your GitHub repo.
3. Set build and start commands:
    - Build: `pip install -r requirements.txt`
    - Start: `gunicorn app:app`
4. Set environment variables if needed.
5. Add persistent disk if you want to save uploaded images.

## Features

- Product listing
- Add/Edit/Delete products
- Image upload
- Simple admin dashboard

## License

MIT