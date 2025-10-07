from nicegui import ui,app
from components.navbar import show_navbar
from components.footer import show_footer
import requests


@ui.page("/signin")
def show_signin_page():
    show_navbar()
    ui.label("this is the signin page")
    show_footer()