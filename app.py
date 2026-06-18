# Traemos las herramientas de Flask para controlar la web y enviar datos
from flask import Flask, render_template, jsonify

# Inicializamos nuestra aplicación web Flask
app = Flask(__name__)

# -------------------------------------------------------------
# BASES DE DATOS EN LISTAS (Para los juegos de Trivia y Adivinanzas)
# -------------------------------------------------------------

PREGUNTAS_TRIVIA = [
    {
        "id": 1,
        "pregunta": "¿Cuántos países organizan el Mundial 2026?",
        "opciones": ["1 país", "2 países", "3 países", "4 países"],
        "correcta": "3 países"
    },
    {
        "id": 2,
        "pregunta": "¿Cuántas selecciones jugarán en total en este torneo?",
        "opciones": ["32 selecciones", "48 selecciones", "64 selecciones", "16 selecciones"],
        "correcta": "48 selecciones"
    },
    {
        "id": 3,
        "pregunta": "¿Qué estadio tendrá el honor de albergar el partido inaugural?",
        "opciones": ["Estadio Azteca", "SoFi Stadium", "MetLife Stadium", "Estadio BBVA"],
        "correcta": "Estadio Azteca"
    }
]

DATOS_ADIVINA = [
    {
        "id": 1,
        "imagen": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=400",
        "pista": "Es el cerebro de la computadora, procesa todos los datos.",
        "opciones": ["Memoria RAM", "Procesador (CPU)", "Disco Duro", "Tarjeta de Video"],
        "correcta": "Procesador (CPU)"
    },
    {
        "id": 2,
        "imagen": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400",
        "pista": "Es el lenguaje del futuro que estás aprendiendo justo ahora.",
        "opciones": ["Python", "HTML", "Español", "C++"],
        "correcta": "Python"
    }
]

# -------------------------------------------------------------
# RUTAS DEL SERVIDOR (Controlan qué pantalla o datos enviar)
# -------------------------------------------------------------

# La ruta raíz ahora mostrará el Menú Principal con los botones de acceso directo
@app.route('/')
def inicio():
    # Renderiza la nueva plantilla del menú interactivo
    return render_template('index.html')

# Ruta para cargar el juego de Trivia dentro del menú
@app.route('/trivia')
def trivia():
    return render_template('trivia.html')

# Ruta secreta que le da las preguntas de la trivia al navegador
@app.route('/obtener_preguntas')
def obtener_preguntas():
    return jsonify(PREGUNTAS_TRIVIA)

# Ruta para cargar el juego de Memorama
@app.route('/memorama')
def memorama():
    return render_template('memorama.html')

# Ruta secreta que barajea y entrega las tarjetas del memorama
@app.route('/obtener_tarjetas')
def obtener_tarjetas():
    import random
    tarjetas_base = [
        {"id": 1, "texto": "Ciudad de México", "pareja": "México"},
        {"id": 1, "texto": "México", "pareja": "Ciudad de México"},
        {"id": 2, "texto": "Los Ángeles", "pareja": "Estados Unidos"},
        {"id": 2, "texto": "Estados Unidos", "pareja": "Los Ángeles"},
        {"id": 3, "texto": "Vancouver", "pareja": "Canadá"},
        {"id": 3, "texto": "Canadá", "pareja": "Vancouver"}
    ]
    random.shuffle(tarjetas_base)
    return jsonify(tarjetas_base)

# Ruta para cargar el juego visual de Adivinar el Hardware
@app.route('/adivina')
def adivina():
    return render_template('adivina.html')

# Ruta secreta que le da las imágenes y pistas al juego de adivinanzas
@app.route('/obtener_adivinanzas')
def obtener_adivinanzas():
    return jsonify(DATOS_ADIVINA)

# Ruta para cargar el Laboratorio interactivo de Formas y CSS
@app.route('/formas')
def formas():
    return render_template('formas.html')

# --- NUEVA RUTA: LA CRIPTA DEL CIBERESPACIO ---
@app.route('/cripta')
def cripta():
    # Le indicamos a Flask que abra la pantalla del juego de ciberseguridad
    return render_template('cripta.html')

# --- NUEVA RUTA: GENERADOR DE ARTE DIGITAL ---
@app.route('/arte')
def arte():
    # Le indicamos a Flask que abra la pantalla del lienzo de arte interactivo
    return render_template('arte.html')

@app.route('/globos')
def globos():
    return render_template('globos.html')


# Arranca el servidor local en tu computadora
if __name__ == '__main__':
    app.run(debug=True)