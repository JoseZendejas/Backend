from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import RedirectResponse
from Base_Datos import modelo, esquema
from Base_Datos.conexion import Session_Local, engine
from sqlalchemy.orm import Session
from typing import List
from Base_Datos.esquema import Tarea


# Crear todas las tablas en la base de datos
modelo.Base.metadata.create_all(bind=engine)

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Dependencia para obtener la sesión de base de datos
def get_db():
    try:
        db = Session_Local()
        yield db
    finally:
        db.close()

# Ruta principal que redirige a la documentación
@app.get('/')
def saludo():
    return RedirectResponse(url='/docs/')

# Mostrar todas las tareas
@app.get('/Tarea/', response_model=List[esquema.Tarea])
def mostrar_Tareas(db: Session = Depends(get_db)):
    tareas = db.query(modelo.Tareas).all()
    return tareas

# Crear una nueva tarea
@app.put('/Tarea/', response_model=esquema.Tarea)
def crear_Tarea(entrada: esquema.Tarea, db: Session = Depends(get_db)):
    tarea = modelo.Tareas(
        title=entrada.title,
        description=entrada.description,
        status=entrada.status
    )
    db.add(tarea)
    db.commit()
    db.refresh(tarea)
    return tarea

# Actualizar una tarea existente
@app.put('/Tarea/{tarea_id}', response_model=esquema.Tarea)
def actualizar_Tarea(tarea_id: int, entrada: esquema.TareaUpdate, db: Session = Depends(get_db)):
    tarea = db.query(modelo.Tareas).filter_by(id=tarea_id).first()
    
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea.title = entrada.title
    tarea.description = entrada.description
    tarea.status = entrada.status
    db.commit()
    db.refresh(tarea)
    return tarea

# Borrar una tarea
@app.delete('/Tarea/{tarea_id}', response_model=esquema.Respuesta)
def borrar_Tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(modelo.Tareas).filter_by(id=tarea_id).first()
    
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(tarea)
    db.commit()
    respuesta = esquema.Respuesta(mensaje = "Tarea Eliminada")
    return respuesta



