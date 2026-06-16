# Mini Web - Gestor de tareas

## Descripción

Mini Web es una aplicación desarrollada con Flask que combina una página personal tipo CV con un gestor de tareas.
El usuario puede registrarse, iniciar sesión y gestionar sus propias tareas de forma personalizada.

## Funcionalidades

- Registro e inicio de sesión de usuarios.
- Panel personalizado para cada usuario.
- Creación, edición, completado y eliminación de tareas.
- Asignación de prioridades a las tareas: alta, media y baja.
- Filtros por estado y prioridad.
- Ordenación de tareas.
- Dashboard con estadísticas personalizadas.

## Tecnologías

- Python
- Flask
- HTML
- Jinja
- CSS
- PostgreSQL
- SQLAlchemy
- Git
- python-dotenv
- Flask-SQLAlchemy

## Instalación

1. Clonar el repositorio.

```bash
git clone URL
```
2. Entrar en la carpeta del proyecto.

```bash
cd [Ruta_Proyecto]
```
3. Crear y activar un entorno virtual.

En PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
En CMD:

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

En Linux/Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Instalar las dependencias.

```bash
pip install -r requirements.txt
```
5. Crear base de datos en PostgreSQL.
6. Crear el archivo `.env` usando `.env.example` como referencia.
7. Ejecutar la app.

## Variables de entorno

Para ejecutar el proyecto es necesario crear un archivo `.env` en la raíz del proyecto

Puedes usar `.env.example` como referencia:

```env
DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_base_datos
SECRET_KEY=pon_aqui_tu_clave_secreta
```

`DATABASE_URL` contiene la conexión a la base de datos PostgreSQL.

`SECRET_KEY` se usa para la seguridad interna de Flask.

## Ejecutar la app

Una vez creado y activado el entorno virtual, y configuradas las variables de entorno, ejecuta:

```bash
python run.py
```

Flask mostrará una URL en la terminal. Cópiala y ábrela.

## Estado del proyecto

Proyecto en desarrollo, con funcionalidades principales ya implementadas y en fase de preparación para despliegue.