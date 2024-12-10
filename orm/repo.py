import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_
import orm.esquemas as esquemas

# ------------ Peticiones a usuarios ---------------------
# Esta función es llamada por api.py
# para atender GET '/usuarios/{id}'
# select * from app.usuarios where id = id_usuario
def usuario_por_id(sesion:Session,id_usuario:int):
    print("select * from app.usuarios where id = ", id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()

def actualizar_usuario(sesion:Session,id_usuario:int , usr_esquema:esquemas.UsuarioBase):
    usr_bd = usuario_por_id(sesion,id_usuario)
    if usr_bd is not None:
        usr_bd.nombre = usr_esquema.nombre
        usr_bd.edad = usr_esquema.edad
        usr_bd.domicilio = usr_esquema.domicilio
        usr_bd.email = usr_esquema.email
        usr_bd.password = usr_esquema.password
        
        sesion.commit()
        sesion.refresh(usr_bd)
        print(usr_bd)
        return usr_bd
    else :
        respuesta = {"mensaje","Usuario no encontrado"}
        return respuesta


#Select * from compras
#definicion de compra y foto
def compra_por_id(sesion:Session, id_Compra:int):
    print("Select * from compra where id= ", id_Compra)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_Compra).first()

# GET '/usuarios'
# select * from app.usuarios
def devuelve_usuarios(sesion:Session):
    print("select * from app.usuarios")
    return sesion.query(modelos.Usuario).all()

# ------------ Peticiones a fotos ---------------------
# GET '/fotos/{id}'
# select * from app.fotos where id = id_foto
def foto_por_id(sesion:Session,id_foto:int):
    print("select * from fotos where id = id_foto")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()

# GET '/fotos'
# select * from app.fotos
def devuelve_fotos(sesion:Session):
    print("select * from app.fotos")
    return sesion.query(modelos.Foto).all()

# ------------ Peticiones a compras ---------------------
# GET '/compras/{id}'
# select * from app.compras where id = id_compra
def compra_por_id(sesion:Session,id_compra:int):
    print("select * from compras where id = id_compra")
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_compra).first()

# GET '/compras'
# select * from app.compras
def devuelve_compras(sesion:Session):
    print("select * from app.compras")
    return sesion.query(modelos.Compra).all()

# GET '/compras?id_usuario={id_usr}&precio={p}'
# select * from app.compras where id_usuario=id_usr and precio>=p
def devuelve_compras_por_usuario_precio(sesion:Session, id_usr:int, p:float):
    print("select * from app.compras where id_usuario=id_usr and precio>=p")
    return sesion.query(modelos.Compra).filter(and_(modelos.Compra.id_usuario==id_usr, modelos.Compra.precio>=p)).all()