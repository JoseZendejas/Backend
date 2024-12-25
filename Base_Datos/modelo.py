from sqlalchemy import Column,Integer,String
from .conexion import Base

# Definición del modelo de la tabla Tareas
class Tareas(Base):
    # Nombre de la tabla en la base de datos
    __tablename__='Tareas'
    # Definición de las columnas de la tabla
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(30))
    description = Column(String(255))
    status = Column(String(15))




