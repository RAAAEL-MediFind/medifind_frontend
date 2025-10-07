from nicegui import ui,app
from components.navbar import show_navbar
import requests


@ui.page("/pharmacydashboard")
def show_signin_page():
    ui.label("this is the pharmacy dashboard page")

