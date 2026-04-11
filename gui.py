import utils
from engine import engine
from sqlalchemy import inspect
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_user():
    res = utils.create_user()
    if res == -1:
        print("Você já possui um usuário com esse email.")
    elif res:
        print("Usuário criado.")
    else:
        print("Nome e email não podem ser nulos.")


def delete_user():
    res = utils.delete_user()
    if res:
        print("Usuário deletado.")
    else:
        print("Usuário não existe.")


def create_task():
    res = utils.create_task()
    if res:
        print("Task criada.")
    else:
        print("Usuario não existe.")


def update():
    print("1 - Atualizar email")
    print("2 - Atualizar nome")

    op = input("> ").strip()

    if op == "1":
        res = utils.update_user_email()
        if not res:
            print("O usuário não existe")
    elif op == "2":
        res = utils.update_user_name()
        if not res:
            print("O usuário não existe")
    else:
        print("Opção inválida")


def show_users():
    data = utils.list_users()
    if data:
        for id, name, tasks in data:
            print(f"[{id}] - {name}, Tarefas: {tasks}")
    else:
        print("Você não possui usuários cadastrados.")


def show_tasks():
    data = utils.list_tasks()
    if data:
        print("Tasks: ")
        for task in data:
            print(task)
    else:
        print("Esse usuário não existe ou não possui tarefas.")


def menu():
    utils.create_tables()
    insp = inspect(engine)

    # Checa se as tabelas existem
    if not insp.has_table("users") or not insp.has_table("tasks"):
        raise ConnectionError("Error to connect with tables")
    
    funcs = {
            "1": ("Listar funcionários", show_users),
            "2": ("Listar tasks", show_tasks),
            "3": ("Criar funcionário", create_user),
            "4": ("Atualizar dados", update),
            "5": ("Criar tarefa", create_task),
            "6": ("Deletar usuário", delete_user),
            "7": ("Sair", None)
        }
    
    while True:
        clear_terminal()

        for key, value in funcs.items():
            print(f"{key} - {value[0]}")
        
        option = input("> ").strip()
        if option not in funcs:
            print("Opção invalida tente novamente.")
            input("Pressione ENTER para continuar")
            continue
        elif option == "7":
            break
        else:
            _, func = funcs[option]
            func()
            input("Pressione ENTER para continuar")
            continue
