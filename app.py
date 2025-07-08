import os
from flask import Flask, jsonify, request, render_template
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from controller import Controller
import onetimescript
from db import db
from io import BytesIO
import cv2
import numpy as np
import pytesseract
from flask import Response


# Initialize Flask App
app = Flask(__name__, static_folder="static")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///domains.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Database
db.init_app(app)
with app.app_context():
    db.create_all()

controller = Controller()


@app.route("/url_service", methods=["GET", "POST"])
def url_service():
    """Render the URL verification page and handle form submissions."""
    output = {}
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            try:
                result = controller.main(url)
                output = result
            except Exception as e:
                output = {"error": str(e)}
    return render_template("url_service.html", output=output)


@app.route("/", methods=["GET", "POST"])
def home():
    """Homepage with URL checking."""
    output = {}
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            try:
                result = controller.main(url)
                output = result
            except Exception as e:
                output = {"error": str(e)}
    return render_template("index.html", output=output)


@app.route("/update-db")
def update_db():
    """Update the database using the one-time script."""
    try:
        with app.app_context():
            response = onetimescript.update_db()
            print(" Database updated successfully!")
            return response, 200
    except Exception as e:
        return f"Error updating database: {str(e)}", 500


@app.route("/update-json")
def update_json():
    """Update the JSON file using the one-time script."""
    try:
        with app.app_context():
            response = onetimescript.update_json()
            print("JSON updated successfully!")
            return response, 200
    except Exception as e:
        return f" Error updating JSON: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
