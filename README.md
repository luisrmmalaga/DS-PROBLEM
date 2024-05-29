# Proyecto DS-PROBLEM

## Índice

- [Backend](#backend)

  - [Install Dependencies](#install-dependencies)
  - [Run server](#run-server)

- [Frontend](#frontend)
  - [Install Dependencies](#install-dependencies)

## Requisitos Previos

Antes de comenzar, asegúrate de cumplir los siguientes requisitos:

- Python 3.12
- Tener una base de datos MySQL creada con el nombre ´dsproblem´ en un servidor local (localhost) en el puerto 3306

## Backend

### Install Dependencies

Para instalar las dependencias de Python necesarias para este proyecto, ejecuta el siguiente comando estando dentro del directorio Backend:

```bash
<path>\DS-PROBLEM\Backend\venv\Scripts\Activate.ps1
```

```bash
pip install -r requirements.txt
```

### Run server

```bash
uvicorn app:app --reload
```
