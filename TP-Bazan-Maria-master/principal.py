#!/usr/bin/env python
from flask_bootstrap import Bootstrap
from flask import Flask, render_template,session, redirect, url_for, request, flash
from formulario import Login, Registro, ConsultaCliente, ConsultaProducto, Consulta
import archivo

app = Flask(__name__)
app.config["SECRET_KEY"] = "clave"
bootstrap = Bootstrap(app)

""" Permite el deslogueo del usuario 
si ya tiene una sesión iniciada en el sistema y regresa 
a la página de  inicio """ 

@app.route("/logout")
def logout():
    session.pop('nombre', None)
    return redirect(url_for('index'))

""" Permite consultar los archivos cargados en el sistema"""

@app.route("/users", methods = ('GET', 'POST'))
def user():
    if session.get("nombre"):
        users = archivo.leer("baseDeDatos/passws.csv")
        return render_template('users.html', users = users)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))

""" Valida usuario y contraseña para el login. Chequea los datos ingresados por
 el usuario con el contenido del archivo passws.csv """


@app.route("/login", methods = ('GET', 'POST'))
def login():

    user2 = archivo.leer("baseDeDatos/passws.csv")
    form2 = Login()
    if form2.validate_on_submit():
        for l in user2:
            if l['usuario'] == form2.usu.data.strip():
                if l['login'] == form2.passw.data.strip():
                    session["nombre"] = form2.usu.data.strip()
                    if session["nombre"] == "admin":
                        return redirect(url_for('ventas'))
                    else:
                        return redirect(url_for('usuario'))
                else:
                    form2.passw.data = ""
                    return render_template('login.html', form = form2, msj = "ok")
        form2.passw.data = ""
        form2.usu.data = ""
        return render_template("login.html", form=form2, msj="mal")
    return render_template("login.html", form = form2)

""" Se muestra la página principal del sistema. Con la opción de login de usuario """

@app.route("/")
@app.route("/index", methods = ('GET', 'POST'))
def index():
    if not session.get("nombre"):
       return render_template('index.html')
    return redirect(url_for('login'))


""" se da de alta a nuevos usuarios"""

@app.route("/registro", methods = ('GET', 'POST'))
def registro():

    def limpiar():
        form.passw1.data = " "
        form.usu1.data = " "
        form.passw.data = " "
        form.usu.data = " "
    user = archivo.leer("baseDeDatos/passws.csv")
    form = Registro()
    registrado = True
    if form.validate_on_submit():
        for l in user:
            if l['usuario'] == form.usu.data.strip():
                limpiar()
                return render_template('registro.html', form = form, msj="reg")
            else:
                 registrado = False
        if form.passw1.data.strip() == form.passw.data.strip():
            if form.usu1.data.strip() == form.usu.data.strip():
                if registrado == False:
                    archivo.grabar("baseDeDatos/passws.csv", form.passw.data.strip(), form.usu.data.strip())
                    limpiar()
                    return render_template('registro.html', form = form, msj = "ok")
            else:
                return render_template('registro.html', form=form, msj="usu")
        else:
            return render_template('registro.html', form=form, msj="pass")
    return render_template('registro.html', form  = form)

""" Se muestra el contenido principal para el usuario logueado (admin) 
por defecto redirige a la sección "ventas" """

@app.route("/ventas")
def ventas():
    if session.get("nombre"):
        clientes = archivo.leer("baseDeDatos/archivo.csv")
        return render_template('ventas.html', clientes = clientes, usuario = session.get('nombre'), ff = True)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))

    """Se da de alta a nuevos usuarios"""

@app.route("/usuario")
def usuario():
    usuario = session['nombre']
    return render_template('usuario.html', usuario = usuario)

""" Función con lógica para filtrar y mostrar información sobre un determinado cliente en base
 a caracteres que componen su nombre. Se solicita y valida el ingreso de 3 caracteres """ 


@app.route("/cliente", methods = ('GET', 'POST'))
def cliente():
    if session.get("nombre"):
        form = ConsultaCliente()
        lista_busqueda = archivo.lista_clientes("baseDeDatos/archivo.csv")
        ff = False
        msg = ""
        if form.validate_on_submit():
            lista = []
            if form.cliente.data != None:
                for palabra in lista_busqueda:
                    if form.cliente.data.upper() in palabra:
                        lista.append(palabra)
                if len(lista) != 0:
                    ff = True
                else:
                    ff = False
                    msg = "No se encontro nombre del cliente"
                return render_template("cliente.html", form = form, lista = lista, msg = msg , ff = ff)
        return render_template("cliente.html", form = form, ff = False)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))

""" Función con lógica para filtrar y mostrar información sobre un determinado producto en base
 a caracteres que componen su nombre. Se solicita y valida el ingreso de 3 caracteres. El resultado se mostrara
en mostrar.html """ 

@app.route("/producto", methods = ('GET', 'POST'))
def producto():
    if session.get("nombre"):
        form = ConsultaProducto()
        lista_busqueda = archivo.lista_producto("baseDeDatos/archivo.csv")
        ff = False
        msg = ""
        if form.validate_on_submit():
            lista = []
            if form.producto.data != None:
                for palabra in lista_busqueda:
                    if form.producto.data.upper() in palabra:
                        lista.append(palabra)
                if len(lista) != 0:
                    ff = True
                else:
                    ff = False
                    msg = "No se encontro nombre del producto"
                return render_template('producto.html', form = form, lista = lista, msg = msg , ff = ff)
        return render_template('producto.html', form = form, ff = False)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))

""" Muestra el resultado de la lógica contenida en las secciones de "cliente" y "producto" 
una vez validada y procesada la información ingresada por el usuario """        

@app.route("/mostrar", methods=('GET', 'POST'))
def mostrar():
    if session.get("nombre"):
        if request.method == 'POST':
            lista = []
            msg = ""
            msg2 = ""
            msg3 = ""
            listado = archivo.leer("baseDeDatos/archivo.csv")
            seleccion = request.form['selecc']
            for l in listado:
                if seleccion == l['CLIENTE']:
                    msg = "Listado de todos los productos que compro un Cliente"
                    msg2 = seleccion
                    msg3 = "cliente"
                    lista.append(l)
                elif seleccion == l['PRODUCTO']:
                    lista.append(l)
                    msg = "Listado de clientes que comparon un producto"
                    msg2 = seleccion
                    msg3 = "producto"
            return render_template('mostrar.html', lista=lista, ff=True, msg=msg, msg2=msg2, msg3=msg3)
        return render_template('mostrar.html')
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))

""" Solicita al usuario el ingreso de un número, que será la cantidad de resultados a mostrar en base a
los clientes. Los resultados se basan en las variables que contienen los datos de 
clientes, precios y cantidad de ventas realizadas. Esta función Lee la información de "archivo.csv" para generar una nueva lista
tomando datos con los métodos GET y POST. La funcion recorre el archivo y trae información de las columnas "CLIENTE" y "PRODUCTO" para mostrar
finalmente, un nuevo listado de los productos que compró un cliente en particular """

@app.route("/mejores_clientes", methods = ('GET', 'POST'))
def mejores_clientes():

    if session.get("nombre"):
        form = Consulta()
        if form.validate_on_submit():
            listado = archivo.leer("baseDeDatos/archivo.csv")
            masgasto = []
            consulta = []
            lista_busqueda = archivo.lista_clientes("baseDeDatos/archivo.csv")
            for listcli in lista_busqueda:
                gastoTotal = 0
                for clientes in listado:
                    if listcli == clientes['CLIENTE']:
                        gasto = float(clientes['CANTIDAD']) * float(clientes['PRECIO'])
                        gastoTotal = gastoTotal + gasto
                masgasto.append([gastoTotal, listcli])
            cont = 1
            masgasto.sort(reverse = True)
            for datos in masgasto:
                if cont <= form.cantidad.data:
                    consulta.append(datos)
                    cont = cont + 1
            consulta.sort(reverse = True)
            return render_template('mejores_clientes.html', form = form, fc = True, consulta = consulta, msg2 = "Importe")
        return render_template('mejores_clientes.html', form = form)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))

""" Solicita al usuario el ingreso de un número, que será la cantidad de resultados a mostrar en 
base a los productos vendidos. Los resultados se basan en las variables que contienen los datos de
 clientes, precios y cantidad de ventas realizadas """        

@app.route("/mas_vendidos", methods = ('GET', 'POST'))
def mas_vendidos():
    if session.get("nombre"):
        form = Consulta()
        if form.validate_on_submit():
            listado = archivo.leer("baseDeDatos/archivo.csv")
            masvendio = []
            consulta = []
            lista_busqueda = archivo.lista_producto("baseDeDatos/archivo.csv")
            for listcli in lista_busqueda:
                cant = 0
                codigo = 0
                for clientes in listado:
                    if listcli == clientes['PRODUCTO']:
                         cant = cant + float(clientes['CANTIDAD'])
                         codigo = clientes['CODIGO']
                masvendio.append([int(cant), listcli, codigo])
            cont = 1
            masvendio.sort(reverse = True)
            for datos in masvendio:
                if cont <= form.cantidad.data:
                    consulta.append(datos)
                    cont = cont + 1
            consulta.sort(reverse = True)
            return render_template('mas_vendidos.html', form = form, fc = True, consulta = consulta, msg2 = "Cantidad")
        return render_template('mas_vendidos.html', form = form)
    flash('Debe estar logueado para acceder')
    return redirect(url_for('login'))

# Manejo de errores: Se muestra una página de error 404 al usuario en caso de ser necesario    

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

# Manejo de errores: Se muestra una página de error 500 al usuario en caso de ser necesario    

@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run()
