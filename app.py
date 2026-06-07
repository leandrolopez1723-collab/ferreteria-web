from flask import Flask, render_template

app = Flask(__name__)

productos = [
    {"nombre": "Taladro", "precio": 50000, "imagen": "taladro.jpg"},
    {"nombre": "Martillo", "precio": 8000, "imagen": "martillo.jpg"},
    {"nombre": "Destornillador", "precio": 3000, "imagen": "destornillador.jpg"}
]

@app.route("/")
def tienda():
    return render_template("index.html", productos=productos)

if __name__ == "__main__":
    app.run(debug=True)

