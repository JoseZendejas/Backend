from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Formato de la URL de la base de datos
DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/Tareas"
#Motor de conexión a la base de datos usando la URL
engine = create_engine(DATABASE_URL)
#Configura las sesiones para interactuar con la base de datos.
Session_Local = sessionmaker(autocommit=False,autoflush=False,bind=engine)
#Base declarativa
Base = declarative_base()



