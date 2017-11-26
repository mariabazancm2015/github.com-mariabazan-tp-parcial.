import csv

# Se crea una clase para el manejo de errores

class Error (Exception) :
    pass
def grabar(archivo, dato1, dato2) :
    with open(archivo,  "a") as salidacsv:
        campos = ['login', 'usuario']
        salida = csv.DictWriter(salidacsv,lineterminator='\n', fieldnames = campos)
        salida.writerow({'login': dato1, 'usuario': dato2})

# Toma la información de PRODUCTO de un archivo y lo muestra en una lista        

def lista_producto(archivo1):
    with open(archivo1) as archivo:
        arch_csv = csv.DictReader(archivo)
        listadic = list(arch_csv)
        lista_consulta = []
        for l in listadic :
            if l['PRODUCTO'] not in lista_consulta:
                lista_consulta.append(l['PRODUCTO'])
        return lista_consulta

""" Devuelve el contenido de la variable "listadic", la cual guarda
el contenido de un archivo previamente leido """

def leer(archivo1) :
    with open(archivo1) as archivo :
         arch_csv = csv.DictReader(archivo)
         listadic = list(arch_csv)
         return listadic

# Toma la información de CLIENTE de un archivo y lo muestra en una lista         

def lista_clientes(archivo1) :
    with open(archivo1) as archivo :
        arch_csv = csv.DictReader(archivo)
        listadic = list(arch_csv)
        lista_consulta = []
        for l in listadic :
            if l['CLIENTE'] not in lista_consulta :
               lista_consulta.append(l['CLIENTE'])
        return lista_consulta

""" Procesa la información contenida en la variable listadic para poder validarla.
 Se muestra un mensaje de error en caso de ser validado correctamente """            

def validar(archivo) :
    try:
        with open(archivo) as archivo:
            arch_csv = csv.DictReader(archivo)
            listadic = list(arch_csv)
            msj = False

# Valida la cantidad de columnas ingresadas por el usuario            

            for item in listadic :
                if len(item) != 5 :
                    raise Error("verifique el nro de columnas del archivo")

# Valida el número y el tipo ingresado por el usuario                    

                if type(int(item['CODIGO'])) != int and item['CODIGO'] is not None :
                   pass
                else :
                    msj = True

# Valida que los datos ingresados por el usuario no contengan números                                        

                if str(item['PRODUCTO']).isnumeric():
                    raise Error("el campo no debe contener numeros")
                else :
                    msj = True

                if str(item['CLIENTE']).isnumeric():
                    raise Error("el campo no debe contener numeros")
                else :
                    msj = True

# Valida que los datos ingresados por el usuario sean números                    

                if float(item['CANTIDAD']) % 1 == 0 :
                    msj = True
                else :
                    raise Error("La cantidad debe ser un numero entero")

# Valida que los datos ingresados por el usuario sean únicamente números reales                    

                if float(item['PRECIO']) % 1 == 0 or float(item['PRECIO']) % 1 != 0 :
                     msj = True
                else:
                    raise Error("El precio debe ser un numero")
        if msj:
             return True

# Salida para cada tipo de error

    except Error as error :
        print(error)
        print("")
        print("-No se puede procesar el archivo-")
    except ValueError:
        print("error en el tipo de valor del campo")
        print("")
        print("-No se puede procesar el archivo-")
    except FileNotFoundError:
        print("No se puede leer el archivo")
        print("")
        print("-No se puede procesar el archivo-")





