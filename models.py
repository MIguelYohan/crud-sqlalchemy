from engine import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import validates ,relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique= True)
    is_online = Column(Boolean)

    # Relation Ship garante a interação entre dois objetos no Python
    tasks = relationship("Task",
                        back_populates="user",
                        cascade="all, delete-orphan") # Deleta as tasks quando o usuario for deletado 

    @validates("name")
    def validate_name(self, key, value):
        if not value or value.strip() == '':
            raise ValueError("Column name cannot be null")
        return value
    
    @validates("email")
    def validate_email(self, key, value):
        if not value or value.strip() == '':
            raise ValueError("Column email cannot be null")
        return value
    
    def __init__(self, name, email, is_online= True):
        self.name = name
        self.email = email
        self.is_online = is_online
    

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # A FK garante o nivel de interação entre duas entidades no banco de dados
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(100), nullable= False)

    user = relationship("User", back_populates= "tasks")

    def __init__(self, title, user_id):
        self.title = title
        self.user_id = user_id
