from fastapi import APIRouter, HTTPException, Query
from app.models.user_model import User
from app.controllers import user_controller

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def list_users():
    return user_controller.get_users()

@router.get("/{user_id}")
def get_user(user_id: int):
    user = user_controller.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/")
def create_user(user: User):
    return user_controller.create_user(user)

@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    updated = user_controller.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated

@router.delete("/{user_id}")
def delete_user(user_id: int):
    deleted = user_controller.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado"}


# 🔹 GET usando PATH PARAM
@router.get("/{user_id}")
def get_user(user_id: int):
    user = user_controller.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


# 🔹 POST usando QUERY PARAMS (LINK)
@router.post("/create")
def create_user(
    name: str = Query(...),
    email: str = Query(...)
):
    return user_controller.create_user_from_link(name, email)