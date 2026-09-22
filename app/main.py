from fastapi import FastAPI

from . import database, models
from .routers import expenses, users

app = FastAPI()

# Adding the routers
app.include_router(users.router)
app.include_router(expenses.router)

# Creating the database
models.Base.metadata.create_all(bind=database.engine)

@app.get('/')
def root():
    return 'Main page'