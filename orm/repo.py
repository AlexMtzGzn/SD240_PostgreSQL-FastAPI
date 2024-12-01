import orm.modelos as modelos
from sqlalchemy.orm import Session

# Esta función es llamada por api.py
# para atender GET '/usuarios/{id}'
# select * from app.usuarios where id = id_usuario
def usuario_por_id(sesion:Session,id_usuario:int):
    print("select * from app.usuarios where id = ", id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()

#Select * from compras
#definicion de compra y foto
def compra_por_id(sesion:Session, id_Compra:int):
    print("Select * from compra where id= ", id_Compra)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_Compra).first()
