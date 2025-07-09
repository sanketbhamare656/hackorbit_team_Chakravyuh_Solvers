
<img src="static/phishnet-aiagent.png"  width="350" height="88">


# PhisNet

PhisNet 🔒🕵️‍♂️
A phishing domain detection tool built with Python

PhisNet is a phishing detection tool that empowers users to safely inspect suspicious URLs without directly visiting them. With an intuitive interface and robust backend checks, PhisNet helps you avoid phishing attacks and stay informed.


## Features
🚀 Features
PhisNet offers a range of powerful features to help users identify and avoid phishing websites:

✅ User-Friendly Interface
Simple, clean, and easy to navigate — no technical expertise required.

🖼️ Website Preview Without Visiting
View a snapshot of the suspicious website without opening it in your browser.

📊 Trust Score Analysis
Receive a trust score based on multiple safety metrics to assess a domain's authenticity.

🛡️ PhishTank Database Verification
Instantly check if the URL has been reported as a phishing link via PhishTank.

🌐 Domain Intelligence
Get critical information about the URL:

    - WHOIS Data – domain ownership and registration details

    - SSL Certificate Info – check if the site uses HTTPS and its certificate status

    - General Domain Insights – including IP address, hosting provider, and more



<img src="static/phishnet-logo copy.png"  width="350" height="175">
<br>

## Local Setup
If you find this project useful or interesting, please consider starring it and putting it on your watch list.

To run the application on your system, you can choose one of the following methods:



### A. Manual Setup
Alternatively, you can manually set up the project by following these steps. Note that you may encounter issues with Python libraries, depending on your Python version and the libraries already installed on your system.

1. Clone the repository: 

```shell
git clone https://github.com/sanketbhamare656/Phishnet-main.git
cd PhisNet
```

2. Install the dependencies: 

```shell
pip install -r requirements.txt
```

3. Start the Flask app: 

```shell
python app.py
```

4. Open your web browser and go to http://localhost:5000 to use the application locally.


## Learn and Contribute to the Project
  
  <details>
  <summary> <b> Learn How PhisNet Works </b> </summary>

  ### Project Functionality Overview

This section explains the functionality and inner workings of the project, detailing its key components and processes.

### API Endpoints 
- `/`: Homepage of the application where users can input a URL to assess its safety.
- `/preview`: Endpoint to view a preview of the website within PhisNet.
- `/source-code`: Endpoint to view the source code of a website.

[Detailed code documentaion of PhisNet](README-HOW-PhisNet-WORKS.md)



</details>

<details>
  <summary> <b> How to Contribute to PhisNet </b> </summary>


## Feedback

If you have any feedback or suggestions, please reach out at 

Any input is highly appreciated.
