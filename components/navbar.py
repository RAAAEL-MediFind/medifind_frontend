from nicegui import ui

def show_navbar():
    """
    A modern and responsive navigation bar component for NiceGUI.
    """
    # Use a header or element for semantic HTML and full width
    with ui.header().classes('bg-blue-600 text-white shadow-lg h-16'):
        # Flex container for layout: space-between distributes items
        with ui.element('div').classes("flex justify-between items-center w-full h-full px-4 sm:px-8"):

            # 1. Left: Clickable Logo/Brand
            with ui.row().classes("items-center"):
                with ui.link("/"):
                    # Use a clean icon and text as a robust placeholder for the logo
                    ui.image("assets/signuplog.png").classes("h-10 w-auto object-contain cursor-pointer") 

                    


            # 2. Center: Navigation Links (Desktop/Tablet Only)
            with ui.row().classes("hidden md:flex gap-8"):
                for label, link in [
                    ("Home", "/"),
                    ("Find Medicine", "/find"),
                    ("Upload Prescription", "/upload"),
                    ("My Orders", "/orders"),
                    ("Contact", "/contact"),
                ]:
                    ui.link(label, link).classes(
                        "text-base font-medium hover:text-blue-200 transition-colors duration-200 py-1"
                    ).props('flat') # Add a 'flat' prop if this were a button, but for links, it's clean.

            # 3. Right: User Actions (Icons and Button)
            with ui.row().classes("items-center gap-4"):
                # Notifications Icon
                ui.icon("notifications_none").classes(
                    "text-2xl cursor-pointer hover:text-blue-200 transition-colors duration-200"
                )
                
                # Dashboard Button
                ui.button("Dashboard", on_click=lambda: ui.open("/userdashboard")).classes(
                    "bg-blue-800 text-white font-semibold text-sm px-4 py-1.5 rounded-full shadow-md "
                    "hover:bg-blue-700 transition-colors duration-200"
                )
