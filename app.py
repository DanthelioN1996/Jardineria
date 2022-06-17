# 0. ejecutamos pip install flask flask-sqlalchemy flask-migrate flask-cors
# 1. Crear modelos
# 2. importamos las librerias de flask

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Usuario, Productos
from flask_cors import CORS

# 3. instanciamos la app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Conten-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

# 5. Creamos la ruta por defecto para saber si mi app esta funcionado
# 6. ejecutamos el comando en la consola: python app.py o python3 app.py y revisamos nuestro navegador
@app.route('/')
def index():
    return 'Hola desde gitpod'

# 7. Ruta para consultar todos los Usuarios
@app.route('/usuarios', methods=['GET'])
def getUsuarios():
    user = Usuario.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

# 12. Ruta para agregar usuario
@app.route('/usuarios', methods=['POST'])
def addUsuario():
    user = Usuario()
    # asignar a variables lo que recibo mediante post
    user.primer_nombre = request.json.get('primer_nombre')
    user.apellido_paterno = request.json.get('apellido_paterno')
    user.direccion = request.json.get('direccion')
    user.telefono = request.json.get('telefono')
    user.correo_electronico = request.json.get('correo_electronico')

    Usuario.save(user)

    return jsonify(user.serialize()),200

# 13. Creamos metodo para consultar un usuario en especifico
@app.route('/usuarios/<id>', methods=['GET'])
def getUsuario(id):
    user = Usuario.query.get(id)
    return jsonify(user.serialize()),200

# 14. Borrar usuario
@app.route('/usuarios/<id>', methods=['DELETE'])
def deleteUsuario(id):
    user = Usuario.query.get(id)
    Usuario.delete(user)
    return jsonify(user.serialize()),200

# 15. Modificar Usuario
@app.route('/usuarios/<id>', methods=['PUT'])
def updateUsuario(id):
    user = Usuario.query.get(id)
    
    user.primer_nombre = request.json.get('primer_nombre')
    user.apellido_paterno = request.json.get('apellido_paterno')
    user.direccion = request.json.get('direccion')
    user.telefono = request.json.get('telefono')
    user.correo_electronico = request.json.get('correo_electronico')

    Usuario.save(user)

    return jsonify(user.serialize()),200

#Productos----------------------------------------------------------------------

# Ruta para consultar todos los Productos
@app.route('/Productos', methods=['GET'])
def getProductos():
    prd = Productos.query.all()
    prd = list(map(lambda x: x.serialize(), prd))
    return jsonify(prd),200

# Ruta para agregar Producto
@app.route('/Productos', methods=['POST'])
def addProductos():
    prd = Productos()
    # asignar a variables lo que recibo mediante post
    prd.codigo_productos = request.json.get('codigo_productos')
    prd.nombre_productos = request.json.get('nombre_productos')
    prd.dimension_productos = request.json.get('dimencion_productos')
    prd.descripcion_productos = request.json.get('descripcion_productos')
    prd.cantidad_productos = request.json.get('cantidad_productos')
    prd.precio_productos = request.json.get('precio_productos')

    Productos.save(prd)

    return jsonify(prd.serialize()),200

# Creamos metodo para consultar un usuario en especifico
@app.route('/Productos/<id>', methods=['GET'])
def getProductos(codigo_productos):
    prd = Productos.query.get(codigo_productos)
    return jsonify(prd.serialize()),200

# 14. Borrar usuario
@app.route('/Productos/<id>', methods=['DELETE'])
def deleteProductos(codigo_productos):
    prd = Productos.query.get(codigo_productos)
    Productos.delete(prd)
    return jsonify(prd.serialize()),200

# 15. Modificar Usuario
@app.route('/Productos/<id>', methods=['PUT'])
def updateProductos(codigo_productos):
    prd = Productos.query.get(codigo_productos)

    prd.codigo_productos = request.json.get('codigo_productos')
    prd.nombre_productos = request.json.get('nombre_productos')
    prd.dimension_productos = request.json.get('dimencion_productos')
    prd.descripcion_productos = request.json.get('descripcion_productos')
    prd.cantidad_productos = request.json.get('cantidad_productos')
    prd.precio_productos = request.json.get('precio_productos')

    Usuario.save(prd)

    return jsonify(prd.serialize()),200


# 8. comando para iniciar mi app flask: flask db init
# 9. comando para migrar mis modelos:   flask db migrate
# 10. comando para crear nuestros modelos como tablas : flask db upgrade
# 11. comando para iniciar la app flask: flask run

# 4. Configurar los puertos nuestra app 
if __name__ == '__main__':
    app.run(port=5000, debug=True)