import requests
from flask import Flask, render_template, request

api = open("API_KEY.txt").read().strip()

def chat_with_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api}"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": api
    }
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        try:
            return result['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError):
            return "Tidak ada respon dari AI."
    else:
        return f"Error: {response.status_code} - {response.text}"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        user_input = request.form["prompt"]
        reply = chat_with_gemini(user_input)
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)

