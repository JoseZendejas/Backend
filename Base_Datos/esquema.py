from pydantic import BaseModel

class Tarea(BaseModel):
    id:int
    title:str
    description:str
    status:str

    class Config:
        orm_mode = True


class TareaUpdate(BaseModel):
    title:str
    description:str
    status:str

    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    mensaje:str

