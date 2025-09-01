# Backend

# Proyecto Django - Gestión de Clientes y Órdenes

Este proyecto fue desarrollado en Django y permite gestionar clientes y órdenes desde el panel de administración.

## Requisitos

- Python 3.12
- Django 5.2.5
- Entorno virtual (recomendado)

## Instalación

1. Clonar el repositorio:

git clone https://github.com/Tatiana1607/BackEnd

2. Crear y activar el entorno virtual:
   
   python -m venv .venv
   .venv\Scripts\activate
   

3. Instalar dependencias:
   
   pip install -r requirements.txt
   

4. Aplicar migraciones:
   
   python manage.py migrate
   

5. Crear superusuario:
   
   python manage.py createsuperuser
   

6. Ejecutar el servidor:
   
   python manage.py runserver
   

## Acceso al panel de administración

Ir a http://127.0.0.1:8000/admin e ingresar con el superusuario creado.

---

Este proyecto fue desarrollado por Karen Florez como parte de su aprendizaje en Django. Para cualquier duda o sugerencia, puedes revisar el código en el repositorio o contactarme por GitHub.