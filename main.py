from flask import Flask, request
import random

app = Flask(__name__)

respuestas = {
    "feliz": [
        "Eso se nota en tu energía 🌟",
        "Sigue brillando.",
        "Hoy el mundo te queda pequeño."
    ],
    "triste": [
        "Respira. Esto también pasa.",
        "No todo día gris es tormenta.",
        "Eres más fuerte de lo que crees."
    ],
    "cansada": [
        "Descansar también es productividad.",
        "Tu cuerpo no es una máquina.",
        "Mañana también existe."
    ]
}

@app.route("/", methods=["GET", "POST"])
def home():
    mensaje = ""
    if request.method == "POST":
        estado = request.form.get("estado").lower()
        if estado in respuestas:
            mensaje = random.choice(respuestas[estado])
        else:
            mensaje = "Interesante... cuéntame más."

    return f"""
    <html>
    <head>
        <title>Mini Diario</title>
        <link rel="stylesheet" href="/css/style.css">
    </head>
    <body>
        <div class="container">
            <h1>Mini Diario Emocional</h1>
            <form method="POST">
                <input type="text" name="estado" placeholder="Escribe: feliz, triste, cansada...">
                <button type="submit">Enviar</button>
            </form>
            <p class="respuesta">{mensaje}</p>
        </div>
    </body>
    </html>
    """

@app.route("/css/<path:filename>")
def css(filename):
    with open(f"css/{filename}") as f:
        return f.read(), 200, {"Content-Type": "text/css"}

if __name__ == "__main__":
    app.run(debug=True)