# TP-Bazan-Maria

#Sistema Web para consulta de información dinámica basadas en la la interacción del usuario:

El sistema es modular y se compone de varios segmentos que interactúan entre sí, mostrando distintos tipos de información dependiendo de la necesidad del usuario.

El sistema permite el acceso a un único usuario, previamente registrado ("admin"), el cual tiene privilegios necesarios para consultar distintos tipos de información, tales como:

* Clientes
* Productos y códigos de productos
* Precios
* Cantidad de productos vendidos

Una vez logueado en el sistema, es redirigido a la sección "ultimas ventas", pudiendo ver un resumen de los últimos productos vendidos, discriminados por las características mencionadas anteriormente.

Dentro del sistema, el usuario tiene privilegios para realizar consultas dinámicas desde las secciones "Productos por cliente", "Clientes por producto", "Mejores cleintes" y "productos más vendidos". Estas secciones interactúan entre sí para brindar información útil al usuario a modo de "ranking" de mejores resultados.

Terminadas las consultas necesarias, el usuario tiene la posibilidad de realizar "logout" en el sistema, regresando a la página principal del mismo.

Detalle de los módulos:

1) Sección de Bienvenida para logueo del usuario.
2) Sección de "ultimas ventas" con un ranking de los últimos productos que se vendieron, y sus cantidades
3) Sección de "producto por cliente" donde el usuario puede consultar cúales son los últimos productos comprados, en base al nombre del cliente en cuestión
4) Sección de "clientes por producto" donde el usuario puede consultar, en base al nombre del producto, cúales son los clientes que adquirieron dichos productos.
5) Sección de "mejores clientes" donde el usuario puede conocer cuáles son los clientes que más compraron.
6) Sección de "productos más vendidos" donde el usuario puede consultar cúales son los productos más vendidos y sus cantidades, junto con su correspondiente código de producto.
7) Sección de "salir" donde el usuario puede realizar un logout del sistema, regresando a la página principal del mismo.


Carárcterísticas técnicas del sistema Web:

form flask_bootstrap es un framework de Python para interactuar con las plantillas HTML, es decir para intectuar con sitios Web. 

Se utilizaron las siguientes funciones del framework Flask:

* Import se utiliza para llamar a las funciones
* Render se utiliza para interpretar y renderizar el código HTML
* Session se utiliza para manejar sesiones de usuarios
* Redirect se utiliza para redireccionar URLs en base a distintas situaciones
* Request se utiliza para invocar distintos métodos
* Flash se utiliza para mostrar mensajes en pantalla 
* Import se utliza para decir a python que incluya funciones, tales como login, ConsultaCliente

Las plantillas HTML interactúan enviando información utilizando los métodos GET y POST.

Como base de datos local, se utilizan archivos CSV, por ejemplo en archivo.csv y passws.csv. Estos archivos son llamados por las funciones para recorrer y utilizar su contenido dependiendo cada módulo.