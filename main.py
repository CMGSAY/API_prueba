from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

usuarios = {}

class Login(BaseModel):
    correo: str
    contrasenia: str


usuarios[1] = {
    "nombre": "Carlos Garcia",
    "correo": "carlosgarcias@umes.edu.gt",
    "contrasenia": "1234"
}


@app.get("/")
def home():
    return {"mensaje": "API funcionando"}


@app.post("/login")
def login(datos: Login):

    for usuario in usuarios.values():
        if usuario["correo"] == datos.correo and usuario["contrasenia"] == datos.contrasenia:
            return {"mensaje": "Login exitoso"}

    raise HTTPException(status_code=401, detail="Credenciales incorrectas")