# Nombre: Jhostyn Javier Gavilanez Suarez
# Proyecto Unidad I - Sistemas de Gestion de Pedidos de un Restaurante

# importar la libreria flask
# En este apartado se añade la libreria de flask, entre otras para hacer el llamado y otras funcionalidades acerca de nuestro sistema.
from flask import Flask, render_template, redirect, request, url_for

# ---------------------------------------------------------------------------
# Este es el nombre para llamar a los templates de python, ya que se inicializa y se llama a traves del templates donde tenemos nuestra carpeta.
app = Flask(__name__, template_folder='templates')

# ---------------------------------------------------------------------------
# Este es el arreglo para almacenar los pedidos en forma de lista.

ListasRegistros = []  # Esta es para la lista al instante y Domicilio
# ---------------------------------------------------------------------------
# Password para tener acceso a dicha aplicacion mediante el uso del secret key
app.secret_key = 'restaurante123'

# ---------------------------------------------------------------------------
# Inicializamos la ruta principal para que empieza desde el login


@app.route('/')
# llamar a login.html como  ruta principal
def panelPrincipal():
    return render_template('/login.html')

# Inicializamos la ruta secundaria que es el inicio de nuestra aplicacion


@app.route('/home')
# llamar a home.html a la ruta seucndaria
def panelInicio():
    return render_template('/home.html')

# Inicializamos la ruta catalago


@app.route('/catalogo')
# llamar a catalogo.html a la ruta catalogo
def panelCatalogo():
    return render_template('/catalogo.html')

# Inicializamos la ruta pedido


@app.route('/pedidos')
# llamar a pedidos.html a la ruta seucndaria
def panelPedidos():
    return render_template('/pedidos.html')

# *********************************************************************************************
# Aqui van las Supginas de Pedidos del metodo de las listas
# inicializamos la rutas de pedido a domicilio
# *********************************************************************************************
# inicializacion de pedidos a Domicilio 
# *********************************************************************************************

@app.route('/pedidosDomicilio')
# llamar a index.html en la ruta principal
def panelPrincipalPedidosDom():
    return render_template('/pedidosDomicilio.html', ListasRegistros=ListasRegistros)


# *********************************************************************************************
# inicializacion de pedidos al instante
# *********************************************************************************************

@app.route('/pedidosInstante')
# llamar a index.html en la ruta principal
def panelPrincipalPedidosIs():
    return render_template('/pedidosInstante.html', ListasRegistros=ListasRegistros)

# ---------------------------------------------------------------------------
# Este es el segundo paso para enviar datos a nuestra el Registro mediante el formulario dado.
# Controlador de envio.

@app.route('/enviarRegistros', methods=['POST'])
# metodo de guardar los datos
def enviarRegistros():  # Aqui realiza el envio de datos para ser guardados en la lista.
    if request.method == 'POST':
        # el mensaje de añadir un registro de un nuevo dato se muestra por codigo javascript en el html
        Registro_NombreI = request.form['Registro_NombreI']
        Registro_ApellidoI = request.form['Registro_ApellidoI']
        Registro_EmailI = request.form['Registro_EmailI']
        Registro_NombrePlatoI = request.form['Registro_NombrePlatoI']
        Registro_CantidadI = request.form['Registro_CantidadI']
        Registro_RefrescoI = request.form['Registro_RefrescoI']

        # El mensaje esta por codigo javascript dentro del HTML
        if Registro_NombreI == '' or Registro_ApellidoI == '' or Registro_EmailI == '' or Registro_NombrePlatoI == '' or Registro_CantidadI == ''  or Registro_RefrescoI== '' :
            return redirect(url_for('panelPrincipalPedidosIs'))
        else:
            ListasRegistros.append(
                {'Registro_NombreI': Registro_NombreI,
                 'Registro_ApellidoI': Registro_ApellidoI,
                 'Registro_EmailI': Registro_EmailI,
                 'Registro_NombrePlatoI': Registro_NombrePlatoI,
                 'Registro_CantidadI': Registro_CantidadI,
                 'Registro_RefrescoI': Registro_RefrescoI})

            return redirect(url_for('panelPrincipalPedidosIs'))
# ---------------------------------------------------------------------------
# Controlador de la ruta para borrar todos los datos encontrados del registro 
# Controlador de borrar registros del cliente
@app.route('/borrarRegistros', methods=['POST'])
def borrarRegistros():              # La funcion de envio de mensaje borrado se hace mediante codigo Javascript
    ListasRegistros.clear()
    return redirect(url_for('panelPrincipalPedidosIs'))



# *********************************************************************************************

# Inicializamos la ruta de nuestros servicios
@app.route('/NuestrosServicios')
# llamar a NuestrosServicios.html a la ruta seucndaria
def panelNuestrosServicios():
    return render_template('/NuestrosServicios.html')


# Inicializamos la ruta de testimonios
@app.route('/testimonios')
# llamar a testimonios.html a la ruta seucndaria
def panelTestimonios():
    return render_template('/testimonios.html')

# Inicializamos la ruta de Contactanos


@app.route('/Contactanos')
# llamar a Contactanos.html a la ruta seucndaria
def panelContactanos():
    return render_template('/Contactanos.html')

# Inicializamos la ruta de Acerca de


@app.route('/acercaDe')
# llamar a Contactanos.html a la ruta seucndaria
def panelAcercaDe():
    return render_template('/acercaDe.html')


# ejecutar del main principal de la pagina To DO local host - version final del proyecto
if __name__ == '__main__':
    app.run(debug=True)
  