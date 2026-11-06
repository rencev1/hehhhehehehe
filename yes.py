
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Passwords accepted by the digital letter
VALID_PASSWORDS = [
    "lisudsad",
    "lisudpud",
    "lisud sad",
    "lisud pud"
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/unlock", methods=["POST"])
def unlock():
    data = request.get_json()
    password = data.get("password", "").strip().lower()

    if password in VALID_PASSWORDS:
        return jsonify({
            "success": True,
            "message": "Letter unlocked!"
        })

    return jsonify({
        "success": False,
        "message": "Wrong password. Try again!"
    })


if __name__ == "__main__":
    app.run(debug=True)
