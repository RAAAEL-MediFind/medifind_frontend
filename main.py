from nicegui import ui, app
from pages.home import *
from pages.shop import *
from components.footer import *
from components.navbar import *
from components.signup import *
from components.signin import *
from components.user_dashboard import *
from components.vendor_dashbord import *
from pages.main_page import *

app.add_static_files("/assets", "assets")
ui.run()
