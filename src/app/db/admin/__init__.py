from fastapi import FastAPI
from sqladmin import Admin
from .views import TaskView, AccountView
from .auth import authentication_backend
from app.db.tables import engine


def attach_admin_panel(application: FastAPI):
    admin = Admin(application, engine.engine, authentication_backend=authentication_backend)

    admin.add_view(TaskView)
    admin.add_view(AccountView)

