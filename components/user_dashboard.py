from nicegui import ui,app
from components.navbar import show_navbar
import requests


@ui.page("/userdashboard")
def show_user_dashboard():
    ui.label("this is the userdashboard page")
