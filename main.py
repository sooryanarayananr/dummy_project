from fastapi import FastAPI
from routers import items, users, files
from internal import admin

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(files.router)
