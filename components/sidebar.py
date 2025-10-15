from nicegui import ui

def show_sidebar():
    with ui.left_drawer().classes(
        "bg-white w-64 shadow-xl p-0 flex flex-col h-screen overflow-y-auto"
    ):
        # Navigation Links Container 
        with ui.element('div').classes("flex flex-col flex-grow px-3 pt-8"):

            # Define link data
            primary_links = [
                ("Dashboard", "/userdashboard", "dashboard"),
                ("Find Medicine", "/find", "pill"),
                ("Upload Prescription", "/upload", "cloud_upload"),
                ("My Orders", "/orders", "shopping_cart"),
                ("Saved Pharmacies", "/saved", "favorite_border"),
                ("Notifications", "/notifications", "notifications_none"),
            ]
            
            # Primary Actions
            for label, route, icon_name in primary_links:
                with ui.row().classes(
                    "items-center gap-4 px-3 py-2 rounded-lg hover:bg-blue-100 "
                    "transition-colors duration-200 cursor-pointer"
                ).on("click", lambda route=route: ui.open(route)):
                    ui.icon(icon_name).classes("text-blue-600 text-xl")
                    ui.label(label).classes("text-base font-medium text-gray-800")

            # Divider 
            ui.separator().classes("my-4 border-gray-200")

            # Account Section 
            ui.label("ACCOUNT").classes(
                "text-xs font-semibold text-gray-500 uppercase mt-2 mb-2 px-3"
            )
            
            # Settings Link
            with ui.row().classes(
                "items-center gap-4 px-3 py-2 rounded-lg hover:bg-blue-100 "
                "transition-colors duration-200 cursor-pointer"
            ).on("click", lambda: ui.open("/settings")):
                ui.icon("settings").classes("text-blue-600 text-xl")
                ui.label("Settings").classes("text-base font-medium text-gray-800")

            # Logout Button 
            with ui.row().classes('w-full mt-auto mb-6 px-3'):
                ui.button("Logout", icon="logout", on_click=lambda: ui.open("/logout")).classes(
                    "w-full bg-gradient-to-r from-red-500 to-red-600 text-white font-semibold "
                    "rounded-xl py-2.5 shadow-md hover:from-red-600 hover:to-red-700 transition-all duration-200"
                ).props("unelevated")

        ui.element('div').classes('h-2')
