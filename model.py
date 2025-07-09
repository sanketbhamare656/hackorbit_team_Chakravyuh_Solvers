import ipaddress
import re
from bs4 import BeautifulSoup
import requests
import whois
import urllib
import urllib.request
from datetime import datetime
import json
import time
import socket
import ssl
from db import DomainRank   # ✅ your DB helper, if you use it for domain rank

import joblib
import pandas as pd
import tldextract

# =============================
# Load your trained ML model
# =============================
model = joblib.load("phishing_detector.pkl")

# =============================
# Globals for your rule-based
# =============================
BASE_SCORE = 50
PROPERTY_SCORE_WEIGHTAGE = {
    'domain_rank': 0.9,
    'domain_age': 0.3,
    'is_url_shortened': 0.8,
    'hsts_support': 0.1,
    'ip_present': 0.8,
    'url_redirects': 0.2,
    'too_long_url': 0.1,
    'too_deep_url': 0.5,
    'content': 0.1
}

with open('static/data/domain-rank.json', 'r') as f:
    domain_rank_dict = json.load(f)

# =============================
# ALL your rule-based functions
# (unchanged — exactly as you have)
# =============================

# (You can keep your full code here — validate_url, include_protocol, get_domain_rank, whois_data, hsts_support, etc.)

# Example: domain rank
def get_domain_rank(domain):
    rank = domain_rank_dict.get(domain, 0)
    return int(rank)

# WHOIS
def whois_age(domain):
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if creation_date:
            age = (datetime.now() - creation_date).days / 365
            return age
    except:
        return 0

# Shortened
def is_url_shortened(domain):
    with open('static/data/url-shorteners.txt') as f:
        services = f.read().splitlines()
    for s in services:
        if s in domain:
            return 1
    return 0

# HSTS
def hsts_support(url):
    try:
        r = requests.get(url, timeout=5)
        return int('Strict-Transport-Security' in r.headers)
    except:
        return 0

# IP in URL
def ip_present(url):
    try:
        ipaddress.ip_address(url)
        return 1
    except:
        return 0

# Redirects
def url_redirects(url):
    try:
        r = requests.get(url, timeout=5)
        return int(len(r.history) > 0)
    except:
        return 0

# Too long URL
def too_long_url(url):
    return int(len(url) > 75)

# Too deep
def too_deep_url(url):
    slashes = url.count('/') - 2
    return int(slashes > 5)

# Content checks
def content_check(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        result = {'onmouseover':0, 'right-click':0, 'form':0, 'iframe':0, 'login':0, 'popup':0}
        if soup.find(onmouseover=True):
            result['onmouseover'] = 1
        if soup.find_all('body', {'oncontextmenu': 'return false;'}):
            result['right-click'] = 1
        if soup.find_all('form'):
            result['form'] = 1
        if soup.find_all('iframe'):
            result['iframe'] = 1
        if soup.find_all(text=re.compile('password|email|forgotten|login')):
            result['login'] = 1
        if soup.find_all('div', {'class': 'popup'}):
            result['popup'] = 1
        return result
    except:
        return 0

# =============================
# Trust score calculation
# =============================
def calculate_trust_score(url):
    score = BASE_SCORE

    ext = tldextract.extract(url)
    domain = ext.domain + '.' + ext.suffix

    dr = get_domain_rank(domain)
    age = whois_age(domain)
    shorten = is_url_shortened(domain)
    hsts = hsts_support(url)
    ip = ip_present(url)
    redirects = url_redirects(url)
    long_url = too_long_url(url)
    deep_url = too_deep_url(url)
    content = content_check(url)

    # Adjust score with your logic
    def adjust(case, value):
        nonlocal score
        w = PROPERTY_SCORE_WEIGHTAGE[case]
        if case == 'domain_rank':
            if dr == 0: score += 0
            elif dr < 100000: score += w * BASE_SCORE
            elif dr < 500000: score += w * BASE_SCORE * 0.8
            else: score += w * BASE_SCORE * 0.6
        elif case == 'domain_age':
            if age < 5: score -= w * BASE_SCORE
            elif age >= 10: score += w * BASE_SCORE
        elif case == 'is_url_shortened' and shorten:
            score -= w * BASE_SCORE
        elif case == 'hsts_support':
            if hsts: score += w * BASE_SCORE
            else: score -= w * BASE_SCORE
        elif case == 'ip_present' and ip:
            score -= w * BASE_SCORE
        elif case == 'url_redirects' and redirects:
            score -= w * BASE_SCORE
        elif case == 'too_long_url' and long_url:
            score -= w * BASE_SCORE
        elif case == 'too_deep_url' and deep_url:
            score -= w * BASE_SCORE

    adjust('domain_rank', dr)
    adjust('domain_age', age)
    adjust('is_url_shortened', shorten)
    adjust('hsts_support', hsts)
    adjust('ip_present', ip)
    adjust('url_redirects', redirects)
    adjust('too_long_url', long_url)
    adjust('too_deep_url', deep_url)

    return score

# =============================
# ML fallback features
# =============================
def extract_ml_features(url):
    # Dummy example — use same columns you trained!
    features = {
        'qty_dot_url': url.count('.'),
        'length_url': len(url),
        # Add more...
    }
    return pd.DataFrame([features])

# =============================
# Combined hybrid check
# =============================
def hybrid_check(url):
    trust = calculate_trust_score(url)
    print(f"🔍 Rule-based Trust Score: {trust:.2f}")

    if trust >= 70:
        print("✅ Safe (Rule-based priority)")
    elif trust <= 40:
        print("🚩 Phishing (Rule-based priority)")
    else:
        print("🤖 Trust unclear — using ML fallback...")
        X = extract_ml_features(url)
        pred = model.predict(X)[0]
        if pred == 0:
            print("✅ Legitimate (ML)")
        else:
            print("🚩 Phishing (ML)")

# =============================
# Run
# =============================
if __name__ == "__main__":
    url = input("Enter URL: ")
    url = url if url.startswith('http') else 'https://' + url
    hybrid_check(url)
