import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "desarrollo_secret_key_123")


# Ruta Principal (Landing Page)
@app.route("/")
def index():
    # Estructuramos los servicios divididos por especialidad
    servicios_marketing = [
        {
            "nombre": "Estrategia Digital",
            "desc": "Diseño de embudos de venta (funnels) y posicionamiento de marca para captar clientes ideales.",
        },
        {
            "nombre": "Identidad de Marca",
            "desc": "Desarrollo visual y conceptual para que tu negocio destaque en el entorno digital.",
        },
    ]

    servicios_automatizacion = [
        {
            "nombre": "Integración de APIs & Sistemas",
            "desc": "Conexión de plataformas, CRM y bases de datos para un flujo de información sin fricciones.",
        },
        {
            "nombre": "Optimización de Procesos",
            "desc": "Desarrollo de scripts a medida y extracción de datos (scraping) para acelerar tu operación.",
        },
    ]

    return render_template(
        "index.html",
        mkt_servicios=servicios_marketing,
        auto_servicios=servicios_automatizacion,
    )


# Ruta para procesar el formulario de contacto
@app.route("/contacto", methods=["POST"])
def contacto():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    servicio_interes = request.form.get("servicio_interes")
    mensaje = request.form.get("mensaje")

    if not nombre or not email:
        return jsonify({"status": "error", "message": "Faltan campos requeridos"}), 400

    # Aquí se procesará el lead (almacenamiento o alerta automatizada)
    print(
        f"Nuevo Lead - Interés en [{servicio_interes}]: {nombre} ({email}) - Mensaje: {mensaje}"
    )

    return jsonify(
        {
            "status": "success",
            "message": "¡Gracias! Nuestro equipo se pondrá en contacto contigo muy pronto.",
        }
    )


@app.route("/sitemap.xml")
def sitemap():
    import os
    from flask import send_from_directory

    return send_from_directory(os.getcwd(), "sitemap.xml")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
