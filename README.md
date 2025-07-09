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

## ✅ Checkpoint 2 Progress

### 🔧 Backend Development
- Core logic integration started in `app.py`.

### 🧪 UI Demo Pages
- Created demo HTML files for all planned features (chatbot, extension, URL scanner, etc).

### 🗃️ Data Integration
- Added required datasets such as `domain-rank.json` for domain trust scoring.

---

## ✅ Checkpoint 3 Progress

### 1. ✅ **First Feature Implemented: URL Scanning**
- Users can now scan any URL to check for phishing indicators or suspicious activity.
- Fully integrated frontend and backend pipeline.

### 2. ✅ **UI Enhancements**
- `index.html` updated for smoother flow.
- Created `url_scanner.html` with particle.js background, console-style logs, and animated trust score.

### 3. ✅ **Backend Enhancements**
- `app.py` routing + core logic.
- Added:
  - `controller.py` — scanning logic
  - `onetimescript.py` — domain/IP analysis & preprocessing

---

## ✅ Checkpoint 4 – UI Improvements

- Improved layout and responsiveness in `url_service.html`
- Minor bug fixes in `index.html`

---

## ✅ Checkpoint 5 – Unique Feature Implemented

### 🌐 Website Preview Without Visiting
- Secure iframe-based snapshot system.
- Sanitized HTML content to protect users.
- Added preview section to UI for seamless UX.

---

## 📄 `/source-code` Endpoint

- Handles GET/POST.
- Fetches and renders HTML content securely.
- Template used: `source_code.html`.

---
## ✅ Checkpoint 6 - Final Check Point From Team Chakrayvuh Solvers
## ✅ **Why Hybrid?**

Phishing websites evolve quickly — a purely rule-based system can’t always keep up. Combining **traditional security checks** with **data-driven learning** makes the detection:
- More accurate
- More adaptable
- More resilient to new phishing tactics

---

## 🌲 **Why Random Forest?**

The fallback ML model uses a **Random Forest** because:
- It’s an ensemble of many decision trees → more robust and less likely to overfit.
- It handles numerical features well (like URL length, number of dots, subdomains, special characters).
- It’s fast to train and deploy.
- It works well for small to medium tabular datasets.
- XGBoost can be used as an alternative for even better accuracy if needed.

---

## ⚙️ **How it works**

1️⃣ The **rule-based engine** calculates a **trust score** from 0 to 100:
   - Good signals ➜ score goes up (e.g., old domain, high domain rank, secure HTTPS)
   - Bad signals ➜ score goes down (e.g., IP in URL, suspicious redirects, too long, too deep)

2️⃣ Decision logic:
   | Trust Score | Result | Fallback? |
   |-------------|--------|-----------|
   | ≥ 70        | ✅ Legitimate | ❌ |
   | ≤ 40        | 🚩 Phishing   | ❌ |
   | 40–70       | 🤔 Inconclusive | ✅ ML fallback used |

3️⃣ If needed, the trained ML model classifies the URL based on extracted features.

4️⃣ The final result includes:
   - `legitimate` or `phishing`
   - Whether it was decided by **rules** or **ML fallback**
   - The trust score for transparency

---

## 📦 How to Run the Project Locally
- The latest `top-1m.csv` can be downloaded from Tranco List(https://tranco-list.eu/) (this CSV is updated every month). 
- In this `onetimescript.py`, we read the file `/static/data/top-1m.csv`, populate data, and store it into a sorted list (`sorted-top1million.txt`) and a - - JSON file (`domain-rank.json`) for easy access while assessing URLs.

- If you want to update the list and JSON on your local machine, follow these steps:
- 1. Download the `top-1m.csv` file from Tranco List (https://tranco-list.eu/)
- 2. Copy it to the `/static/data/` directory.
- 3. Execute the `onetimescript.py` file. It takes about 10-20 seconds to execute the script.

### Demo Video 
- https://youtu.be/N977gRcLIo0

### PPT (Google Slide)
- https://docs.google.com/presentation/d/1Fs-_w2i2KW8648S3k0Etsya21jRsfoJ1E6NVdWmiMPo/edit?usp=sharing
### 🔁 Step-by-step Setup

```bash
# 1. Clone the repository
git clone https://github.com/sanketbhamare656/hackorbit_team_Chakravyuh_Solvers.git
cd phishnet

# 2. Create and activate virtual environment
python -m venv venve
source venv/bin/activate   # or on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download Dataset Manually (important)
# Visit: https://tranco-list.eu/
# Download the latest top-1m.csv and place it in: /static/data/

# 5. Run one-time data processing
python onetimescript.py

# 6. Start the Flask app
python app.py

'''
### Demo Video 
- https://youtu.be/N977gRcLIo0



