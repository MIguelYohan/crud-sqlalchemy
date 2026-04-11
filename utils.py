from models import User, Task
from engine import Session, Base, engine

# Funções CRUD de usuarios
# 1 - Criar: Cria um Usuario sem task
# 2 - Listar: Lista os usuarios, seu id e a quantidade de tasks
# 3 - Atualizar: atualiza dados de um usuario
# 4 - Criar Task: Cria uma task para um usuario específico
# 5 - Deletar: Deleta usuarios e todas as tasks ligadas a ele

def create_tables():
    Base.metadata.create_all(bind= engine)


def create_user():
    name = input("Nome: ").strip()
    email = input("Email: ").strip()
    if name and email:
        u = User(name, email)
        with Session() as session:
            user = session.query(User).filter_by(email= email).first()
            if user:
                return -1
            session.add(u)
            session.commit()
            return True
    else:
        return False


def create_task():
    title = input("Título: ").strip()
    user_id = int(input("ID: "))

    t = Task(title, user_id)
    with Session() as session:
        user = session.query(User).filter_by(id= user_id).first()
        if user:
            session.add(t)
            session.commit()
            return True
        else:
            return False


def list_tasks():
    try:
        user_id = int(input("ID: "))
    except ValueError:
        return False
    with Session() as session:
        user = session.query(User).filter_by(id = user_id).first()
        if user:
            return [task.title for task in user.tasks]
        else:
            return False


def list_users():
    with Session() as session:
        users_list = session.query(User).all()
        data = []
        for user in users_list:
            data.append((user.id, user.name, len(user.tasks)))
    return data


def update_user_name():
    user_id = int(input("ID: "))
    name = input("Nome: ").strip()

    with Session() as session:
        user = session.query(User).filter_by(id = user_id).first()
        if user:
            user.name = name
            session.commit()
            return True
        else:
            return False
        

def update_user_email():
    user_id = int(input("ID: "))
    email = input("Email: ").strip()

    with Session() as session:
        user = session.query(User).filter_by(id = user_id).first()
        if user:
            user.email = email
            session.commit()
            return True
        else:
            return False


def delete_user():
    user_id = int(input("ID: "))

    with Session() as session:
        user = session.query(User).filter_by(id = user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        else:
            return False
