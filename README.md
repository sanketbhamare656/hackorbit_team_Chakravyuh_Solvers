# 🛡️ PhishNet — Your Cyber Guardian

PhishNet is a web-based tool designed to detect and warn users about suspicious or potentially harmful URLs. It’s part of our ongoing mission to combat phishing and online scams using intelligent automation, powered by AI and Machine Learning to analyze web content, URL behavior, and detect phishing patterns more accurately.

---

## ✅ Checkpoint 1 Progress

### 1️⃣ Built the Frontend (Homepage UI)
- Designed a clean, minimal homepage where users can input a URL.
- Integrated a form-based system to submit URLs for safety analysis.
- User-friendly interface with a clear call-to-action.

### 2️⃣ Backend Development Initiated
- Created the backend using Flask.
- Implemented our first feature
- Currently refining response structure and error handling.

### 3️⃣ Project Documentation Started
- Added this README to explain:
  - What the project is about
  - Tech stack and structure
  - Status of Checkpoint 1
  - What’s coming next

---

## 💡 Tech Stack

- **Frontend**: HTML, CSS (Basic for now)
- **Backend**: Python (Flask)
- **Database**: SQLite (used for storing analyzed domains)
- **Libraries**: BeautifulSoup, SQLAlchemy, Requests

---

## 🚧 What's Next?

- We're now working on adding our project's unique feature — stay tuned for something exciting! 
---



## Checkpoint 2 Progress


---

##  Progress Made in Checkpoint 2

1. **Backend Development**
   - Core logic integration started in `app.py` (Flask-based backend).
   

2. **UI Demo Pages**
   - Created demo HTML files for all planned features (e.g., chatbot, extension, URL scanner, etc).
   

3. **Data Integration**
   - Added required datasets such as `domain-rank.json` for domain trust scoring.
   

---
## ✅ Checkpoint 3 Progress

### 1. ✅ **First Feature Implemented: URL Scanning**
- Users can now scan any URL to check for phishing indicators or suspicious activity.
- Fully integrated frontend and backend processing pipeline.

### 2. ✅ **UI Enhancements**
- Updated `index.html` for smoother input and user flow.
- Created a new, dedicated UI page `url_scanner.html` with particle background, console-style scanning logs, and animated trust score display.

### 3. ✅ **Backend Enhancements**
- Updated `app.py` for routing and scanning logic.
- Added key backend modules:
  - `controller.py` — handles scanning logic
  - `onetimescript.py` — supports domain/IP analysis and preprocessing
- Integrated trained dataset for phishing detection.

---
## ✅ Checkpoint 4 – UI Improvements

In this checkpoint, we focused on enhancing the **user interface and user experience** 

### ✨ Updates Made:
- improve and fix UI in `url_service.html`
- Minor bug fixes in `index.html`


## ✅ Checkpoint 5 – Unique Feature Implemented

### 🌐 Website Preview Without Visiting
- Added a feature that allows users to view a snapshot of the suspicious website without opening it in their browser.
- Implemented a secure iframe-based preview system to display the website content safely.
- Enhanced backend logic to fetch and sanitize HTML content for rendering.
- Updated the UI with a dedicated preview section for better user experience.

---


## /source-code Endpoint
- Handles GET and POST requests.
- Retrieves the HTML content of the input URL using the requests library.
- Renders the `source_code.html` template with the prettified HTML content.
---


## 👥 Team Chakravyuh Solvers



