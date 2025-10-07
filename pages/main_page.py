from nicegui import ui,app
from components.navbar import show_navbar
from components.footer import show_footer
import requests


@ui.page("/main_page")
def show_main_page():
    show_navbar()
    ui.label("this is the main page")
    show_footer()
