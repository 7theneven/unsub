from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual webhook URL
WEBHOOK_URL = "https://hook.eu2.make.com/awqdudldubiobp6b7pllaomx66ttfhaj"

@app.route("/unsubscribe", methods=["GET", "POST"])
def unsubscribe():
    email = request.args.get("email")
    try:
        requests.post(WEBHOOK_URL, json={"event": "unsubscribe", "email": email})
    except Exception as e:
        print("Webhook error:", e)
    return render_template("unsubscribed.html", message="You've been unsubscribed.", message2="We're sorry to see you go. You can resubscribe anytime.")

@app.route("/resubscribe", methods=["GET", "POST"])
def resubscribe():
    email = request.args.get("email")
    try:
        requests.post(WEBHOOK_URL, json={"event": "resubscribe", "email": email})
    except Exception as e:
        print("Webhook error:", e)
    return render_template("unsubscribed.html", message="You've been resubscribed.", message2="Welcome back!", email=email)


# Optional homepage route
@app.route("/")
def home():
    return '''
        <form action="/unsubscribe" method="POST">
            <button type="submit">Unsubscribe</button>
        </form>
    '''

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
