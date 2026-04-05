from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Model Running"

app.run(debug=True)