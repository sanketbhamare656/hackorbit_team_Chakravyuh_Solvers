import os
from flask import Flask, jsonify, request, render_template
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from chatbot import chatbot_bp
from controller import Controller
import onetimescript
from db import db
from services.phone_verification import check_phone_number
from services.sms_verification import analyze_sms
from werkzeug.utils import secure_filename
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
import pytesseract
from flask import Response
# Initialize Flask App
app = Flask(__name__, static_folder="static")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///domains.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable for performance

# Initialize Database
db.init_app(app)
with app.app_context():
    db.create_all()

controller = Controller()


@app.route('/scan_progress')
def scan_progress():

    def generate():
        # This would be called at each step of your scanning process
        yield f"data: {time.time()} Starting scan...\n\n"
        # Add more yield statements for each step

    return Response(generate(), mimetype='text/event-stream')


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


@app.route("/preview", methods=["POST"])
def preview():
    """Preview the webpage by fetching and displaying its content."""
    url = request.form.get("url")
    if not url:
        return "Error: No URL provided.", 400

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        for tag in soup.find_all(["link", "img"]):
            attr = "href" if tag.name == "link" else "src"
            if tag.get(attr):
                tag[attr] = urljoin(url, tag[attr])

        return render_template("preview.html", content=soup.prettify())
    except Exception as e:
        return f"Error fetching webpage: {e}", 500


@app.route("/source-code", methods=["POST"])
def view_source_code():
    """Fetch and display the source code of a given URL."""
    url = request.form.get("url")
    if not url:
        return "Error: No URL provided.", 400

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        return render_template("source_code.html",
                               formatted_html=soup.prettify(),
                               url=url)
    except Exception as e:
        return f"Error fetching source code: {e}", 500


@app.route("/update-db")
def update_db():
    """Update the database using the one-time script."""
    try:
        with app.app_context():
            response = onetimescript.update_db()
            print("Database updated successfully!")
            return response, 200
    except Exception as e:
        return f"Error updating database: {str(e)}", 500


@app.route("/update-json")
def update_json():
    """Update the JSON file using the one-time script."""
    try:
        with app.app_context():
            response = onetimescript.update_json()
            print("SON updated successfully!")
            return response, 200
    except Exception as e:
        return f"Error updating JSON: {str(e)}", 500


@app.route("/check_url", methods=["GET"])
def check_url():
    """Check the trust score of a given URL."""
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        result = controller.main(url)
        return jsonify({"trust_score": result.get("trust_score", "N/A")})
    except Exception as e:
        return jsonify({"error": f"Error processing URL: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
