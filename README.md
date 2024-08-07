# Gerenciador de Tarefas 📝

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Unittest-002F6C?style=for-the-badge&logo=unittest&logoColor=white" />
<img src="https://img.shields.io/badge/Colorama-00BFFF?style=for-the-badge&logo=colorama&logoColor=white" />

Sistema de gestão de tarefas que permite ao usuário adicionar, listar, marcar como concluída e remover tarefas através do terminal. 

## 📝 Funcionalidades

- Adicionar tarefas 📝
- Listar tarefas 📝
- Marcar tarefa como concluída ✅
- Remover tarefas ❌
- Exibir detalhes de uma tarefa ℹ️

## 🔧 Tecnologias

- Python 🐍
- Colorama 🎨
- Unittest 🧪

## 📁 Arquitetura

O projeto foi desenvolvido utilizando o padrão MVC (Model-View-Controller), onde existe uma classe de Task (modelo), TaskView (interface de usuário), TaskController (controlador de tarefas) e TaskFactory (fabrica de tarefas).

## 📁 Organização

O projeto está organizado da seguinte forma:

- `src` 📁
  - `task_model.py` 📝: implementa a classe Task
  - `task_view.py` 📝: implementa a classe TaskView
  - `task_controller.py` 📝: implementa a classe TaskController
  - `task_factory.py` 📝: implementa a classe TaskFactory
  - `utils` 📁
    - `task_validators.py` 📝: implementa as validações das tarefas
    - `view_utils.py` 📝: implementa as funções de exibição da interface de usuário

- `tests` 📁
  - `test_task_model.py` 🧪: testes unitários para a classe Task
  - `test_task_controller.py` 🧪: testes unitários para a classe TaskController
  - `test_task_view.py` 🧪: testes unitários para a classe TaskView
  - `test_task_factory.py` 🧪: testes unitários para a classe TaskFactory

- `app.py` 📝: arquivo principal que executa o sistema de gerenciamento de tarefas

- `requirements.txt` 📝: lista de dependências do projeto

- `README.md` 📝: este arquivo

