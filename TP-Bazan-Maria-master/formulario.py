from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms import validators

"""Se definen y validan los datos para nuevos registros de usuarios"""

class Registro(FlaskForm):
    usu = StringField('Usuario', [validators.data_required(message = "Debe ingresar un usuario")])
    passw = PasswordField('Contrasena', [validators.data_required(message = "Debe ingresar una contrasena")])
    usu1 = StringField('Repetir Usuario', [validators.data_required(message = "Debe ingresar un usuario ")])
    passw1 = PasswordField('Repetir Contrasena', [validators.data_required(message = "Debe ingresar una contrasena")])
    submit = SubmitField("Enviar")

""" Se definen y validan los campos utilizados para la funcíon de logueo de los usuarios """

class Login(FlaskForm):
    usu = StringField('Usuario', [validators.data_required(message = "Debe ingresar un usuario")])
    passw = PasswordField('Login', [validators.data_required(message = "Debe ingresar una contrasena")])
    submit = SubmitField("Ingresar")

"""Se define y validan los campos para la consulta de productos"""

class ConsultaProducto(FlaskForm):
    submit = SubmitField("Buscar")
    producto = StringField('Producto', [validators.data_required(message = "Debe ingresar el nombre del Producto"), validators.Length(min = 3, message = "Debe ingresar como minimo 3 caracteres")])
    submit_selec = SubmitField("Seleccionar")

""" Se define y validan los campos para las consultas de la sección 'Mejores Clientes'"""

class Consulta(FlaskForm):
    submit = SubmitField("Aceptar")
    cantidad = IntegerField('Cantidad de items a mostrar', [validators.data_required(message = "Debe ingresar un numero entero")])
    
"""Se define y validan los campos para la consulta de clientes"""

class ConsultaCliente(FlaskForm):
    submit = SubmitField("Buscar")
    cliente = StringField('Cliente', [validators.data_required(message = "Debe ingresar el nombre del Cliente"), validators.Length(min = 3, message = "Debe ingresar como minimo 3 caracteres")])
    submit_selec = SubmitField("Seleccionar")
