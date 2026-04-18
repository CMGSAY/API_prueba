from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# ===============================
# BASE DE DATOS TEMPORAL
# ===============================

usuarios = {}
roles = {}

# ===============================
# MODELOS
# ===============================

class Rol(BaseModel):
    nombre: str
    descripcion: str
    estado: bool
    fecha_modificacion: datetime


class Usuario(BaseModel):
    nombre: str
    correo: str
    contrasenia: str
    estado: bool
    fecha_modificacion: datetime
    rol_id: int


class Login(BaseModel):
    correo: str
    contrasenia: str


# ===============================
# DATOS DE PRUEBA
# ===============================

roles[1] = Rol(
    nombre="Administrador",
    descripcion="Acceso total",
    estado=True,
    fecha_modificacion=datetime.now()
)

roles[2] = Rol(
    nombre="Usuario",
    descripcion="Acceso limitado",
    estado=True,
    fecha_modificacion=datetime.now()
)

usuarios[1] = Usuario(
    nombre="Carlos Garcia",
    correo="carlosgarcias@umes.edu.gt",
    contrasenia="1234",
    estado=True,
    fecha_modificacion=datetime.now(),
    rol_id=1
)

usuarios[2] = Usuario(
    nombre="Juan Perez",
    correo="juan@umes.edu.gt",
    contrasenia="12345678",
    estado=True,
    fecha_modificacion=datetime.now(),
    rol_id=2
)

# ===============================
# LOGIN
# ===============================
@app.get("/")
def home():
    return {"mensaje": "API funcionando"}

@app.post("/login")
def login(datos: Login):

    for usuario_id, usuario in usuarios.items():

        if usuario.correo == datos.correo and usuario.contrasenia == datos.contrasenia:

            return {
                "mensaje": "Login exitoso",
                "usuario_id": usuario_id,
                "nombre": usuario.nombre
            }

    raise HTTPException(status_code=401, detail="Credenciales incorrectas")


# ===============================
# OBTENER USUARIOS
# ===============================

@app.get("/usuarios")
def obtener_usuarios():
    return usuarios


# ===============================
# CREAR USUARIO
# ===============================

@app.post("/crear_usuario")
def crear_usuario(usuario: Usuario):

    if usuario.rol_id not in roles:
        raise HTTPException(status_code=404, detail="Rol no existe")

    usuario_id = len(usuarios) + 1
    usuarios[usuario_id] = usuario

    return {
        "mensaje": "Usuario creado",
        "usuario_id": usuario_id
    }


# ===============================
# OBTENER ROLES
# ===============================

@app.get("/roles")
def obtener_roles():
    return roles