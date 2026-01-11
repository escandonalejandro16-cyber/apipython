from app.models.user_model import User

# Simulación de base de datos
users_db = []

def get_users():
    return users_db

def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    return None

def create_user(user: User):
    user.id = len(users_db) + 1
    users_db.append(user)
    return user

def update_user(user_id: int, user_data: User):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            user_data.id = user_id
            users_db[index] = user_data
            return user_data
    return None

def delete_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            users_db.remove(user)
            return user
    return None


def create_user_from_link(name: str, email: str):
    user = User(
        id=len(users_db) + 1,
        name=name,
        email=email
    )
    users_db.append(user)
    return user
