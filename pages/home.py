from nicegui import ui, app
from components.navbar import show_navbar
from components.footer import show_footer
import requests


@ui.page("/home")
def show_home_page():
    show_navbar()
    ui.label("this is the home page")
    show_footer()
