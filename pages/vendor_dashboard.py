from nicegui import ui

@ui.page("/pharmacydashboard")
def pharmacy_dashboard():
    # === PHARMACY SIDEBAR (same design as user sidebar) ===
    with ui.left_drawer().classes(
        "bg-white w-64 shadow-xl p-0 flex flex-col h-screen overflow-y-auto"
    ):
        with ui.element('div').classes("flex flex-col flex-grow px-3 pt-8"):

            # Define pharmacy-specific links
            primary_links = [
                ("Dashboard", "/pharmacydashboard", "dashboard"),
                ("Inventory", "/pharmacy/inventory", "medical_services"),
                ("Orders", "/pharmacy/orders", "shopping_bag"),
                ("Customers", "/pharmacy/customers", "people"),
                ("Reports", "/pharmacy/reports", "bar_chart"),
                ("Notifications", "/pharmacy/notifications", "notifications_none"),
            ]

            # Navigation links
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

            # Settings
            with ui.row().classes(
                "items-center gap-4 px-3 py-2 rounded-lg hover:bg-blue-100 "
                "transition-colors duration-200 cursor-pointer"
            ).on("click", lambda: ui.open("/pharmacy/settings")):
                ui.icon("settings").classes("text-blue-600 text-xl")
                ui.label("Settings").classes("text-base font-medium text-gray-800")

            # Logout Button
            with ui.row().classes('w-full mt-auto mb-6 px-3'):
                ui.button("Logout", icon="logout", on_click=lambda: ui.open("/logout")).classes(
                    "w-full bg-gradient-to-r from-red-500 to-red-600 text-white font-semibold "
                    "rounded-xl py-2.5 shadow-md hover:from-red-600 hover:to-red-700 transition-all duration-200"
                ).props("unelevated")

        ui.element('div').classes('h-2')

    # === MAIN DASHBOARD AREA ===
    with ui.column().classes("flex-grow p-8 bg-gray-50 min-h-screen"):
        ui.label("Pharmacy Dashboard").classes("text-3xl font-bold text-blue-700 mb-6")

        # Overview Cards
        with ui.row().classes("w-full justify-around mt-4"):
            for title, count in [
                ("Total Medicines", "145"),
                ("Pending Orders", "23"),
                ("Completed Sales", "410"),
                ("Customers", "87"),
            ]:
                with ui.card().classes(
                    "bg-white shadow-md rounded-2xl w-60 p-5 flex flex-col items-center text-center hover:shadow-lg transition-all duration-200"
                ):
                    ui.label(title).classes("text-gray-600 text-sm")
                    ui.label(count).classes("text-2xl font-bold text-blue-700")

        # Divider
        ui.separator().classes("my-6")

        # Table Placeholder
        ui.label("Recent Orders Summary").classes("text-xl font-semibold text-gray-700 mb-3")
        ui.label("📊 Chart or data table coming soon...").classes("text-gray-500 italic")


# Run app directly (for local testing)
if __name__ == "__main__":
    ui.run(title="Pharmacy Dashboard")
