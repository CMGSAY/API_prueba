from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Login(BaseModel):
    correo: str
    contrasenia: str

usuarios = {
    "carlosgarcias@umes.edu.gt": "1234"
}

@app.get("/")
async def root():
    return {"mensaje": "API funcionando en Vercel"}

@app.post("/login")
async def login(datos: Login):

    if datos.correo in usuarios and usuarios[datos.correo] == datos.contrasenia:
        return {"mensaje": "Login exitoso"}

    raise HTTPException(status_code=401, detail="Credenciales incorrectas")


# IMPORTANTE PARA VERCEL
def handler(request, response):
    return app