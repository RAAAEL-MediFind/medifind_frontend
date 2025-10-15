from nicegui import ui,app
#from components.navbar import show_navbar
import requests


@ui.page("/pharmacydashboard")
def pharmacy_dashboard():
    # NAVBAR 
    with ui.header().classes('bg-sky-500 text-white flex items-center justify-between px-6 py-3 shadow-sm'):
        ui.label('MEDIFIND Pharmacy Portal').classes('text-lg font-semibold tracking-wide')
        with ui.row().classes('items-center gap-4'):
            ui.icon('notifications').classes('text-white cursor-pointer')
            ui.avatar('https://cdn-icons-png.flaticon.com/512/9187/9187604.png').classes('w-8 h-8 cursor-pointer')

    #  MAIN CONTAINER 
    with ui.row().classes('w-full h-screen bg-gray-100'):
        
        # SIDEBAR 
        with ui.column().classes('bg-sky-500 text-white w-64 py-6 px-4 space-y-4 rounded-r-2xl'):
            ui.label('Dashboard Menu').classes('text-lg font-bold mb-4 text-white')

            ui.link('Overview', '#', new_tab=False).classes('text-white hover:underline')
            ui.link(' Inventory', '#', new_tab=False).classes('text-white hover:underline')
            ui.link(' Orders', '#', new_tab=False).classes('text-white hover:underline')
            ui.link(' Profile', '#', new_tab=False).classes('text-white hover:underline')
            ui.separator()
            ui.button('Logout', color='white', text_color='sky-600').classes('rounded-xl mt-4')

        # MAIN DASHBOARD AREA 
        with ui.column().classes('flex-1 p-6 space-y-8 overflow-y-auto'):
            
            ui.label('Welcome back, Pharmacy Admin 👋').classes('text-2xl font-semibold text-gray-800')

            # STAT CARDS 
            with ui.row().classes('gap-6'):
                with ui.card().classes('w-1/4 bg-sky-50 p-4 shadow-md rounded-xl'):
                    ui.label('Total Sales').classes('text-gray-500 text-sm')
                    ui.label('₵4,500').classes('text-2xl font-bold text-sky-600')
                with ui.card().classes('w-1/4 bg-sky-50 p-4 shadow-md rounded-xl'):
                    ui.label('Pending Orders').classes('text-gray-500 text-sm')
                    ui.label('12').classes('text-2xl font-bold text-sky-600')
                with ui.card().classes('w-1/4 bg-sky-50 p-4 shadow-md rounded-xl'):
                    ui.label('Medicines in Stock').classes('text-gray-500 text-sm')
                    ui.label('120').classes('text-2xl font-bold text-sky-600')
                with ui.card().classes('w-1/4 bg-sky-50 p-4 shadow-md rounded-xl'):
                    ui.label('Customers Served').classes('text-gray-500 text-sm')
                    ui.label('89').classes('text-2xl font-bold text-sky-600')

            #  RECENT ORDERS TABLE
            ui.label('Recent Orders').classes('text-xl font-semibold text-gray-700 mt-6')
            ui.table(
                columns=[
                    {'name': 'id', 'label': 'Order ID', 'field': 'id'},
                    {'name': 'medicine', 'label': 'Medicine', 'field': 'medicine'},
                    {'name': 'quantity', 'label': 'Qty', 'field': 'quantity'},
                    {'name': 'status', 'label': 'Status', 'field': 'status'},
                ],
                rows=[
                    {'id': 'ORD001', 'medicine': 'Paracetamol', 'quantity': 5, 'status': 'Delivered'},
                    {'id': 'ORD002', 'medicine': 'Amoxicillin', 'quantity': 2, 'status': 'Pending'},
                    {'id': 'ORD003', 'medicine': 'Ibuprofen', 'quantity': 3, 'status': 'Ready'},
                ],
                row_key='id'
            ).classes('bg-white rounded-xl shadow-md')

            # PROFILE SECTION 
            ui.label('Pharmacy Profile').classes('text-xl font-semibold text-gray-700 mt-8')
            with ui.card().classes('bg-white p-4 shadow-md rounded-xl w-1/2'):
                ui.label('Name: Medifind Pharmacy').classes('text-gray-700')
                ui.label('Location: Accra, Ghana').classes('text-gray-700')
                ui.label('Email: medifind@example.com').classes('text-gray-700')
                ui.label('Contact: 0545819523').classes('text-gray-700')
                ui.button('Edit Profile', color='sky-500', text_color='white').classes('mt-4')

# Run directly for testing
if __name__ in {"__main__", "__mp_main__"}:
    pharmacy_dashboard()
    ui.run()


