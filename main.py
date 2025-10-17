from nicegui import ui, app
from pages.home import *
from pages.shop import *
from components.footer import *
from components.navbar import *
from components.signup import *
from components.signin import *
from pages.user_dashboard import *
from pages.vendor_dashboard import *
from pages.main_page import *
from components.create_ad import *
from components.edit_stock import *

app.add_static_files("/assets", "assets")
ui.run(storage_secret='nanijayblinkz1234@')
