from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual webhook URL
WEBHOOK_URL = "https://hook.eu2.make.com/awqdudldubiobp6b7pllaomx66ttfhaj"

@app.route("/unsubscribe", methods=["POST"])
def unsubscribe():
    try:
        # Trigger the webhook
        requests.post(WEBHOOK_URL, json={"event": "unsubscribe"})
    except Exception as e:
        print("Webhook error:", e)
    return render_template("unsubscribed.html")

@app.route("/resubscribe", methods=["POST"])
def resubscribe():
    try:
        requests.post(WEBHOOK_URL, json={"event": "resubscribe"})
    except Exception as e:
        print("Webhook error:", e)
    return "<h1>You're resubscribed!</h1>"

# Optional homepage route
@app.route("/")
def home():
    return '''
        <form action="/unsubscribe" method="POST">
            <button type="submit">Unsubscribe</button>
        </form>
    '''

# Remove app.run(), as it's not needed in serverless environments.
