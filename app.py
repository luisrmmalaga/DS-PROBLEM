from fastapi import FastAPI

from routes.user import users_controller

app = FastAPI()


@app.get('/')
def read_root():
    return 'Hello world!'


app.include_router(users_controller)
