from nicegui import ui,app
from components.navbar import show_navbar
from components.footer import show_footer  
from components.sidebar import show_sidebar
import requests


@ui.page("/userdashboard")
def user_dashboard():
    """User Dashboard Page for MediFind"""
    from components.navbar import show_navbar 
    show_navbar()
    show_sidebar()

    with ui.column().classes("mt-24 px-8 gap-8 max-w-6xl mx-auto"):

        # Welcome Header
        with ui.row().classes("justify-between items-center"):
            ui.label("Welcome, Medifinder!").classes("text-2xl font-bold text-green-700")
            
            ui.button("Logout").classes("bg-green-700 text-white px-4 py-2 rounded-lg hover:bg-green-800")

        # Quick Actions
        with ui.row().classes("gap-4 mt-4 flex-wrap"):
            ui.button("Find Medicine").classes("bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700")
            ui.button("Upload Prescription").classes("bg-white text-green-700 border border-green-700 px-6 py-3 rounded-lg hover:bg-green-100")
            ui.button("My Orders").classes("bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700")

        # Recent Searches
        with ui.card().classes("p-4 w-full bg-white shadow-md rounded-xl"):
            ui.label("Recent Searches").classes("text-xl font-semibold text-green-700 mb-3")
            with ui.row().classes("gap-4 flex-wrap"):
                ui.label("Paracetamol - 3 days ago").classes("text-gray-700")
                ui.label("Amoxicillin - 1 week ago").classes("text-gray-700")
                ui.label("Ibuprofen - 2 weeks ago").classes("text-gray-700")

        # Saved Pharmacies
        with ui.card().classes("p-4 w-full bg-white shadow-md rounded-xl"):
            ui.label("Saved Pharmacies").classes("text-xl font-semibold text-green-700 mb-3")
            with ui.row().classes("gap-4 flex-wrap"):
                for name in ["GoodHealth Pharmacy", "TrustCare Drugs", "MedPlus Pharmacy"]:
                    with ui.card().classes("p-3 w-[250px] text-center bg-green-50 hover:bg-green-100 transition"):
                        ui.label(name).classes("text-lg font-semibold text-gray-800")
                        ui.label("Accra, Ghana").classes("text-sm text-gray-500")
                        ui.button("Remove").classes("mt-2 text-sm bg-red-500 text-white px-3 py-1 rounded-lg hover:bg-red-600")

        # Notifications
        with ui.card().classes("p-4 w-full bg-white shadow-md rounded-xl"):
            ui.label("Notifications").classes("text-xl font-semibold text-green-700 mb-3")
            ui.label("Ibuprofen now available at GoodHealth Pharmacy").classes("text-gray-700")
            ui.label("Your order #12345 is ready for pickup.").classes("text-gray-700")

    show_footer()


