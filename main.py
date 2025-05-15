from flask import Flask,request,render_template,make_response

app=Flask(__name__)

@app.route('/buscar')
def buscar():
    producto = request.args.get('producto')
    talla = request.args.get('tamano')
    color = request.args.get('color')
    if producto is None and talla is None and color is None:
        return "Faltan datos para búsqueda"
    return f"Buscando {producto} de talla {talla} y color {color}"

listado=[]

@app.route("/registro", methods=["GET"])
def ruta_formulario():
    return render_template("formulario.html")

@app.route("/registro", methods=["POST"])
def ruta_registro():
    nombre=request.form.get("estudiante")
    email=request.form.get("correo")
    passwd=request.form.get("contrasena")
    if nombre and email and passwd:
        listado.append({"nombre":nombre,"correo":email,"passwd":passwd})
        return render_template("formulario.html",listado=listado)
    return f"Faltan datos para ingreso"

    #return f"Usuario registrado: {nombre}, {email}, {passwd}"

@app.route("/ropa/<string:producto>/<string:talla>")
def ruta_consulta(producto,talla):
    return f"el producto consultado es: {producto},{talla}"

#header, otro tipo de solicitud en http
@app.route("/ver-headers")
def ruta_headers():
    navegador=request.headers.get("User-agent")
    return f"El navegador que hace la petición es: {navegador}"

#cookies, otro tipo de solicitud
@app.route("/crear_cookie")
def crear_cookie():
    respuesta=make_response("Coookie Creada")
    respuesta.set_cookie("usuario logeado","True")
    return respuesta

@app.route("/leer_cookie")
def leer_cookie():
    valor=request.cookies.get("Usuario logeado")
    return f"El valor de la cookie es: {valor}"

#gu

if __name__=="__main__":
    app.run(debug=True)
