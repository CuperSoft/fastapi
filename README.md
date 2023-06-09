1. Crear ambiente virtual con virtualenv

virtualenv .venv


2. Activar el ambiente virtual

.venv\Scripts\activate


3. Instalar los requerimientos con pip

pip install -r requirements.txt


4. Validar cadena de conexión en config/db.py


5. Correr servidor con uvicorn

uvicorn app:app