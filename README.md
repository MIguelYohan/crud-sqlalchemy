# 🗂️ Task Manager (Funcionários)

## 📌 Sobre o projeto

Este projeto é um gerenciador de tarefas voltado para funcionários. Ele permite o gerenciamento completo de usuários e tarefas, incluindo a criação, atualização, listagem e remoção de dados.

O sistema implementa operações CRUD (Create, Read, Update, Delete) para as entidades principais:

* Usuários
* Tarefas (associadas a um usuário específico)

---

## ⚙️ Tecnologias utilizadas

* Python
* SQLAlchemy
* MySQL

---

## 🧠 Funcionalidades

### 👤 Usuários

* Criar usuário
* Listar usuários
* Atualizar dados do usuário
* Deletar usuário

### 📋 Tarefas

* Criar tarefas vinculadas a um usuário
* Gerenciar tarefas associadas

---

## 💾 Persistência de dados

O projeto utiliza banco de dados relacional com MySQL, utilizando SQLAlchemy como ORM para manipulação dos dados.

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados

É necessário ter o MySQL instalado localmente.

Crie um arquivo `.env` na raiz do projeto e configure a URL de conexão:

```env
DATABASE_URL=mysql+mysqldb://usuario:senha@localhost/nome_do_banco
```

---

### 5. Executar o projeto

```bash
python main.py
```

---

## ⚠️ Observações importantes

* O banco de dados deve estar criado previamente no MySQL
* As credenciais devem ser configuradas corretamente no arquivo `.env`
* O projeto depende de um banco de dados local para funcionamento

---