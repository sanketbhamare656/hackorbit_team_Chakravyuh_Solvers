# # import os
# # import google.generativeai as genai
# # from flask import Blueprint, request, jsonify
# # from duckduckgo_search import DDGS

# # # Configure Gemini API
# # GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# # if not GEMINI_API_KEY:
# #     raise ValueError("API key is missing. Set GEMINI_API_KEY as an environment variable.")

# # genai.configure(api_key=GEMINI_API_KEY)
# # model = genai.GenerativeModel('gemini-1.5-flash')

# # # Blueprint setup
# # chatbot_bp = Blueprint("chatbot", __name__)

# # CYBER_SECURITY_CONTEXT = """
# # You are CyberGuard, an empathetic cybersecurity expert assistant. Your role is to:
# # 1. Provide helpful, accurate cybersecurity advice.
# # 2. Show understanding and concern for users' security issues.
# # 3. Stay strictly focused on cybersecurity topics.
# # 4. Use simple language and avoid technical jargon when possible.
# # 5. For non-cybersecurity questions, politely decline to answer.
# # 6. For recent threats or unknown information, use web search.
# # """

# # def is_cybersecurity_related(query):
# #     """Check if a query is cybersecurity-related using Gemini."""
# #     prompt = f"Is this query related to cybersecurity, hacking, or digital security? Answer only yes/no. Query: {query}"
# #     try:
# #         response = model.generate_content(prompt)
# #         return "yes" in response.text.lower()
# #     except Exception as e:
# #         print(f"Error checking query: {e}")
# #         return False

# # def search_web(query):
# #     """Search DuckDuckGo and format results."""
# #     try:
# #         with DDGS() as ddgs:
# #             results = list(ddgs.text(query, max_results=3))
        
# #         if not results:
# #             return "No relevant search results found. Please try rephrasing your query."
        
# #         formatted = ["Here's what I found:"]
# #         for i, result in enumerate(results, 1):
# #             formatted.append(f"{i}. {result['title']}")
# #             formatted.append(f"   URL: {result['href']}\n")
        
# #         return "\n".join(formatted)
# #     except Exception as e:
# #         print(f"Search error: {e}")
# #         return "I encountered an error while searching. Please try again later."

# # def generate_response(query):
# #     """Generate an empathetic cybersecurity response."""
# #     try:
# #         if not is_cybersecurity_related(query):
# #             return "I'm specialized in cybersecurity. Please ask about security-related topics."
        
# #         chat = model.start_chat(history=[])
# #         response = chat.send_message(f"{CYBER_SECURITY_CONTEXT}\nUser Query: {query}\nRespond empathetically first, then provide expert advice:")

# #         if "search the web" in response.text.lower() or "recent information" in response.text.lower():
# #             search_results = search_web(query)
# #             return f"{response.text}\n\n{search_results}"
        
# #         return response.text
# #     except Exception as e:
# #         return f"Sorry, I encountered an error: {e}. Please try again."

# # @chatbot_bp.route("/respond", methods=["POST"])
# # def chatbot_respond():
# #     """API endpoint to handle chatbot responses."""
# #     data = request.get_json()
# #     user_message = data.get("message", "").strip()

# #     if not user_message:
# #         return jsonify({"response": "Please enter a valid query."}), 400

# #     response = generate_response(user_message)
# #     return jsonify({"response": response})
# # from flask import Blueprint, request, jsonify
# # from duckduckgo_search import DDGS
# # from config import model # Import configured Gemini API

# # # Blueprint setup
# # chatbot_bp = Blueprint("chatbot", __name__)

# # CYBER_SECURITY_CONTEXT = """
# # You are CyberGuard, an empathetic cybersecurity expert assistant. Your role is to:
# # 1. Provide helpful, accurate cybersecurity advice.
# # 2. Show understanding and concern for users' security issues.
# # 3. Stay strictly focused on cybersecurity topics.
# # 4. Use simple language and avoid technical jargon when possible.
# # 5. For non-cybersecurity questions, politely decline to answer.
# # 6. For recent threats or unknown information, use web search.
# # """

# # def is_cybersecurity_related(query):
# #     """Check if a query is cybersecurity-related using Gemini."""
# #     prompt = f"Is this query related to cybersecurity, hacking, or digital security? Answer only yes/no. Query: {query}"
# #     try:
# #         response = model.generate_content(prompt)
# #         return "yes" in response.text.lower()
# #     except Exception as e:
# #         print(f"Error checking query: {e}")
# #         return False

# # def search_web(query):
# #     """Search DuckDuckGo and format results."""
# #     try:
# #         with DDGS() as ddgs:
# #             results = list(ddgs.text(query, max_results=3))
        
# #         if not results:
# #             return "**No relevant search results found.**\n\nTry rephrasing your query."

# #         formatted = ["**Here's what I found:**\n"]
# #         for i, result in enumerate(results, 1):
# #             formatted.append(f"**{i}.** {result['title']}\n🔗 {result['href']}\n")

# #         return "\n".join(formatted)
# #     except Exception as e:
# #         print(f"Search error: {e}")
# #         return "**I encountered an error while searching.**\n\nPlease try again later."

# # def generate_response(query):
# #     """Generate a concise cybersecurity response."""
# #     try:
# #         if not is_cybersecurity_related(query):
# #             return "**I'm specialized in cybersecurity.**\n\nPlease ask about security-related topics."

# #         chat = model.start_chat(history=[])
# #         response = chat.send_message(
# #             f"{CYBER_SECURITY_CONTEXT}\nUser Query: {query}\nRespond empathetically and in **max 2 lines**."
# #         )

# #         return "**" + response.text.strip() + "**"
# #     except Exception as e:
# #         return "**Oops! Something went wrong.**\n\nPlease try again later."

# # @chatbot_bp.route("/respond", methods=["POST"])
# # def chatbot_respond():
# #     """API endpoint to handle chatbot responses."""
# #     data = request.get_json()
# #     user_message = data.get("message", "").strip()

# #     if not user_message:
# #         return jsonify({"response": "**Please enter a valid query.**"}), 400

# #     response = generate_response(user_message)
# #     return jsonify({"response": response})
# from flask import Blueprint, request, jsonify
# from duckduckgo_search import DDGS
# from config import model  # Import configured Gemini API
# import time

# # Blueprint setup
# chatbot_bp = Blueprint("chatbot", __name__)

# CYBER_SECURITY_CONTEXT = """
# You are CyberGuard, an empathetic cybersecurity expert assistant. Your role is to:
# 1. Provide accurate and helpful cybersecurity advice.
# 2. Guide users on banking frauds and cybercrime complaints in India.
# 3. Respond in a conversational and human-like tone.
# 4. Use simple language while maintaining clarity.
# 5. Simulate typing effect for better user experience.
# 6. Politely decline non-cybersecurity-related questions.
# """

# INDIA_CYBERCRIME_INFO = """
# In India, you can report cyber frauds by:
# 📌 Dialing the Cyber Crime Helpline: **1930**
# 📌 Filing a complaint at: **https://cybercrime.gov.in**
# """

# def is_cybersecurity_related(query):
#     """Check if a query is cybersecurity-related using Gemini."""
#     prompt = f"Is this query about cybersecurity, hacking, banking fraud, or digital security in India? Answer only yes/no. Query: {query}"
#     try:
#         response = model.generate_content(prompt)
#         return "yes" in response.text.lower()
#     except Exception as e:
#         print(f"Error checking query: {e}")
#         return False

# def search_web(query):
#     """Search DuckDuckGo and format results."""
#     try:
#         with DDGS() as ddgs:
#             results = list(ddgs.text(query, max_results=3))
        
#         if not results:
#             return "**No relevant search results found.**\n\nTry rephrasing your query."

#         formatted = ["**Here's what I found:**\n"]
#         for i, result in enumerate(results, 1):
#             formatted.append(f"**{i}.** {result['title']}\n🔗 {result['href']}\n")

#         return "\n".join(formatted)
#     except Exception as e:
#         print(f"Search error: {e}")
#         return "**I encountered an error while searching.**\n\nPlease try again later."

# def generate_response(query):
#     """Generate a human-like cybersecurity response with typing effect."""
#     try:
#         if not is_cybersecurity_related(query):
#             return "**I'm specialized in cybersecurity and banking fraud prevention.**\n\nPlease ask about security-related topics."

#         # India-specific cybercrime complaints
#         if "cybercrime complaint" in query.lower() or "bank fraud" in query.lower():
#             return INDIA_CYBERCRIME_INFO

#         chat = model.start_chat(history=[])
#         response = chat.send_message(
#             f"{CYBER_SECURITY_CONTEXT}\nUser Query: {query}\nRespond empathetically and in **max 3 lines**."
#         )

#         # Simulating typing effect
#         response_text = response.text.strip()
#         typing_effect = "💬 Typing..."
#         time.sleep(1)  # Simulating delay
#         return f"{typing_effect}\n\n**{response_text}**"
    
#     except Exception as e:
#         return "**Oops! Something went wrong.**\n\nPlease try again later."

# @chatbot_bp.route("/respond", methods=["POST"])
# def chatbot_respond():
#     """API endpoint to handle chatbot responses."""
#     data = request.get_json()
#     user_message = data.get("message", "").strip()

#     if not user_message:
#         return jsonify({"response": "**Please enter a valid query.**"}), 400

#     response = generate_response(user_message)
#     return jsonify({"response": response})
from flask import Blueprint, request, jsonify
from duckduckgo_search import DDGS
from config import model  # Import configured Gemini API
import time

chatbot_bp = Blueprint("chatbot", __name__)

CYBER_SECURITY_CONTEXT = """
You are CyberGuard, an empathetic cybersecurity expert assistant. Your role is to:
1. Help users with cybersecurity, banking frauds, and cybercrime issues in India.
2. Be friendly, simple, and human-like in replies.
3. Avoid technical words and explain in simple plain text.
4. Politely decline non-cybersecurity topics.
"""

INDIA_CYBERCRIME_INFO = """
You can report cyber frauds in India by:
Call the Cyber Crime Helpline at 1930
Or file a complaint at https://cybercrime.gov.in
"""

def is_greeting(message):
    return message.lower() in ["hi", "hello", "hey"]

def is_cybersecurity_related(query):
    prompt = f"Is this query about cybersecurity, hacking, banking fraud, or digital security in India? Answer only yes/no. Query: {query}"
    try:
        response = model.generate_content(prompt)
        return "yes" in response.text.lower()
    except Exception as e:
        print(f"Error checking query: {e}")
        return False

def search_web(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
        
        if not results:
            return "No relevant search results found. Try rephrasing your query."

        formatted = ["Here's what I found:"]
        for i, result in enumerate(results, 1):
            formatted.append(f"{i}. {result['title']}")
            formatted.append(f"URL: {result['href']}")
        return "\n".join(formatted)
    except Exception as e:
        print(f"Search error: {e}")
        return "I had trouble searching. Please try again later."

def generate_response(query):
    try:
        if is_greeting(query):
            return "Hello! I am CyberGuard, your cybersecurity assistant. How can I help you today?"

        if not is_cybersecurity_related(query):
            return "I am built to help only with cybersecurity, fraud, and scam related topics. Please ask something in this field."

        if "cybercrime complaint" in query.lower() or "bank fraud" in query.lower():
            return INDIA_CYBERCRIME_INFO

        chat = model.start_chat(history=[])
        response = chat.send_message(
            f"{CYBER_SECURITY_CONTEXT}\nUser Query: {query}\nReply in plain simple text in maximum 3 lines. Do not use any bold or markdown."
        )

        response_text = response.text.strip()
        time.sleep(1)  # Simulate typing delay
        return response_text
    
    except Exception as e:
        return "Something went wrong. Please try again later."

@chatbot_bp.route("/respond", methods=["POST"])
def chatbot_respond():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "Please enter a valid query."}), 400

    response = generate_response(user_message)
    return jsonify({"response": response})
