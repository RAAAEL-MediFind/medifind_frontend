from nicegui import ui, app
import asyncio
from components.navbar import show_navbar 

@ui.page("/pharmacydashboard")
def pharmacy_dashboard():
    # This creates the top navigation bar.
    show_navbar()

    # --- LOGOUT FUNCTIONALITY ---
    async def logout():
        """Clears the user's session and redirects to the sign-in page."""
        app.storage.user.clear()
        ui.notify("You have been successfully logged out.")
        ui.navigate.to('/signin')

    # === PHARMACY SIDEBAR ===
    # The 'top_corner=True' parameter is the key. 
    # It tells the sidebar to start *below* the header you just created.
    with ui.left_drawer(top_corner=True).classes("bg-white w-64 shadow-xl"):
        with ui.column().classes("p-8 gap-y-2 h-screen"):
            ui.button("Add New Stock", icon="add_circle", on_click=lambda: ui.navigate.to('/create_ad')).classes(
                "w-full bg-blue-600 text-white font-semibold rounded-lg py-2.5 mb-4 hover:bg-blue-700"
            )
            primary_links = [
                ("Dashboard", "/pharmacydashboard", "dashboard"),
                ("Inventory", "/pharmacy/inventory", "medical_services"),
                ("Orders", "/pharmacy/orders", "shopping_bag"),
                ("Customers", "/pharmacy/customers", "people"),
                ("Reports", "/pharmacy/reports", "bar_chart"),
                ("Notifications", "/pharmacy/notifications", "notifications_none"),
            ]
            for label, route, icon_name in primary_links:
                with ui.row().classes("w-full items-center gap-4 px-3 py-2 rounded-lg hover:bg-blue-100 cursor-pointer").on("click", lambda r=route: ui.navigate.to(r)):
                    ui.icon(icon_name).classes("text-blue-600 text-xl")
                    ui.label(label).classes("text-base font-medium text-gray-800")
            
            ui.separator().classes("my-4")
            ui.label("ACCOUNT").classes("text-xs font-semibold text-gray-500 uppercase px-3")
            
            with ui.row().classes("items-center gap-4 px-3 py-2 rounded-lg hover:bg-blue-100 cursor-pointer").on("click", lambda: ui.navigate.to("/pharmacy/settings")):
                ui.icon("settings").classes("text-blue-600 text-xl")
                ui.label("Settings").classes("text-base font-medium text-gray-800")
            
            # Pushes the logout button to the bottom
            ui.space()
            
            ui.button("Logout", icon="logout", on_click=logout).classes(
                "w-full bg-gradient-to-r from-red-500 to-red-600 text-white font-semibold rounded-xl py-2.5 shadow-md"
            ).props("unelevated")

    # === MAIN CONTENT AREA ===
    # Because this column comes after the header and drawer, NiceGUI automatically
    # places it in the remaining space without any manual adjustments.
    with ui.column().classes("w-full p-8"):
        ui.label("Pharmacy Dashboard").classes("text-3xl font-bold text-blue-700 mb-6")

        # Overview Cards
        with ui.row().classes("w-full gap-6"):
            for title, count in [
                ("Total Medicines", "145"), ("Pending Orders", "23"),
                ("Completed Sales", "410"), ("Customers", "87"),
            ]:
                with ui.card().classes(
                    "bg-white shadow-md rounded-2xl flex-grow p-5 flex flex-col items-center text-center "
                    "hover:shadow-lg transition-shadow duration-300"
                ):
                    ui.label(title).classes("text-gray-600 text-sm")
                    ui.label(count).classes("text-3xl font-bold text-blue-700")

        ui.separator().classes("my-8")

        # Table Placeholder
        ui.label("AVAILABLE STOCK").classes("text-xl font-semibold text-gray-700 mb-4")
        ui.label("📊 Chart or data table coming soon...").classes("text-gray-500 italic")
