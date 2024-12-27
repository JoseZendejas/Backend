# Backend

1.-Inicia el servidor de FastAPI:
uvicorn main:app --reload

2.-Ruta Principal
GET /: Redirige automáticamente a /docs.

Gestión de Tareas
GET /Tarea/: Muestra todas las tareas disponibles.

GET /Tarea/{tarea_id}: Muestra la información de una tarea específica.

Parámetros:
tarea_id (int): ID de la tarea

POST /Tarea/: Crea una nueva tarea.
cuerpo de la tarea:
{
  "title": "str",
  "description": "str",
  "status": "str"
}

PUT /Tarea/{tarea_id}: Actualiza una tarea existente.

Parámetros:
tarea_id (int): ID de la tarea a actualizar.

DELETE /Tarea/{tarea_id}: Elimina una tarea existente.

Parámetros:
tarea_id (int): ID de la tarea a eliminar.

Autor
José Guadalupe Zendejas Sotelo
