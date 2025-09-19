from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_rates():
    url = "https://open.er-api.com/v6/latest/INR"
    data = requests.get(url).json()
    return data["rates"]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            from_curr = request.form["from_curr"]
            to_curr = request.form["to_curr"]

            rates = get_rates()
            if from_curr in rates and to_curr in rates:
                in_base = amount / rates[from_curr]   # convert to INR
                converted = in_base * rates[to_curr]  # convert INR → target
                result = f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}"
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
