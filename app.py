from flask import Flask, render_template
import os

app = Flask(__name__)

productos = [
    {"nombre": "Taladro", "precio": 50000},
    {"nombre": "Martillo", "precio": 8000},
    {"nombre": "Destornillador", "precio": 3000}
]

@app.route("/")
def tienda():
    return render_template("index.html", productos=productos)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)

