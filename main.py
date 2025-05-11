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
    return render_template("unsubscribed.html")

@app.route("/resubscribe", methods=["GET", "POST"])
def resubscribe():
    email = request.args.get("email")
    try:
        requests.post(WEBHOOK_URL, json={"event": "resubscribe", "email": email})
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
