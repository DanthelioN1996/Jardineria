from sqlite3 import dbapi2
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Usuario(db.Model):
    
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    primer_nombre = db.Column(db.String(250), nullable= False)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    direccion = db.Column(db.String(250), nullable= False)
    telefono = db.Column(db.Integer, nullable= False)
    correo_electronico = db.Column(db.String(250), nullable= False)

    def serialize(self):
        return{
            "id": self.id,
            "primer_nombre": self.primer_nombre,
            "apellido_paterno": self.apellido_paterno,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "correo_electronico": self.correo_electronico
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#Clase Productos 

class Productos(db.Model):
    __tablename__ = 'Productos'

    id_codigo_productos = db.Column(db.Integer, primary_key=True)
    nombre_productos = db.Column(db.String(250), nullable= False)
    dimension_productos = db.Column(db.String(250))
    descripcion_productos = db.Column(db.String(250))
    cantidad_productos = db.Column(db.String(250), nullable= False)
    precio_productos = db.Column(db.Integer, nullable= False)

    def serialize(self):
        return{
            "id_codigo_productos": self.id_codigo_productos,
            "nombre_productos": self.nombre_productos,
            "dimension_productos": self.dimension_productos,
            "descripcion_productos": self.descripcion_productos,
            "cantidad_productos": self.cantidad_productos,
            "precio_productos": self.precio_productos
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
