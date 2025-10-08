from nicegui import ui
from components.navbar import show_navbar

@ui.page("/signup")
def show_signup_page():
    show_navbar()
    
    # This is the main two-column grid that fills the screen.
    with ui.grid(columns=2).classes('w-full min-h-screen'):
        
        # Left side
        with ui.column().classes("w-full bg-cover bg-no-repeat bg-center relative").style("background-image:url(/assets/signup.png)"):
            with ui.column().classes("absolute inset-0 bg-black/60 flex items-center justify-center"):
                with ui.column().classes("text-center items-center max-w-sm"):
                    ui.label("Welcome to Medifind").classes("text-white font-extrabold text-4xl")
                    ui.label("Already have an account? Sign in to stay connected.").classes("text-white text-lg")
                    ui.element("div").classes("h-8")
                    ui.button("SIGN IN", on_click=lambda: ui.navigate('/login')).classes("bg-blue text-white font-semibold px-8 py-2 rounded-full")

        # Right side
        with ui.column().classes("w-full flex items-center justify-start pt-20 bg-white"):
            with ui.column().classes('w-[500px] px-8'): # Added padding for content spacing
                with ui.column().classes('w-full items-center mb-8'):
                    # REVERTED: Changed back to text-blue as requested
                    ui.label("MEDIFIND").classes("text-5xl font-bold text-blue").style('letter-spacing: 0.1em')
                    ui.image("assets/signuplog.png").classes("items-center w-[250px] h-[100px] mt-0 ")
                    ui.label("...because the right care shouldn't be hard to find").classes("text-sm font-normal text-gray-500 mt-1 tracking-wide")

                ui.label("Create Account").classes("text-2xl font-bold mt-4 mb-2 text-gray-800")
                ui.label("Choose your role:").classes("text-md font-semibold text-gray-600 mb-4")

                # Role Selection Buttons with hover effects
                with ui.row().classes('w-full justify-start gap-4 mb-6') as role_selection:
                    
                    user_button = ui.card().classes('w-32 h-24 flex flex-col items-center justify-center cursor-pointer border-2 border-gray-200 rounded-lg transition-all hover:border-blue-300 hover:shadow-lg')
                    with user_button:
                        user_icon = ui.icon('person_outline', size='0.5').classes('text-gray-500')
                        user_label = ui.label('User').classes('text-gray-500 font-semibold')

                    
                    pharmacy_button = ui.card().classes('w-32 h-24 flex flex-col items-center justify-center cursor-pointer border-2 border-gray-200 rounded-lg transition-all hover:border-blue-300 hover:shadow-lg')
                    with pharmacy_button:
                        pharmacy_icon = ui.icon('medical_services', size='0.5').classes('text-gray-500')
                        pharmacy_label = ui.label('Pharmacy').classes('text-gray-500 font-semibold')
                
                # Form container with fixed height
                with ui.column().classes("w-full relative h-[400px]"):
                    # User Signup Form
                    with ui.column().classes("w-full absolute top-0 left-0 overflow-y-auto h-full pr-2") as user_form:
                        user_form.visible = False
                        ui.label("YOUR FULL NAME").classes("text-sm font-semibold text-gray-700")
                        ui.input(placeholder="Enter your name").props("outlined").classes("w-full mb-4")
                        ui.label("YOUR EMAIL").classes("text-sm font-semibold text-gray-700")
                        ui.input(placeholder="Enter email").props("outlined").classes("w-full mb-4")
                        ui.label("PASSWORD").classes("text-sm font-semibold text-gray-700")
                        ui.input(placeholder="Enter your password", password=True).props("outlined").classes("w-full mb-4")
                        ui.label("CONFIRM PASSWORD").classes("text-sm font-semibold text-gray-700")
                        ui.input(placeholder="Confirm password", password=True).props("outlined").classes("w-full mb-8")
                        ui.button("Sign Up as User", on_click=lambda: ui.notify("User Sign Up clicked")).classes("w-full bg-blue-300 text-white font-semibold py-2 rounded-full")

                    # Pharmacy Signup Form
                    with ui.column().classes("w-full absolute top-0 left-0 overflow-y-auto h-full pr-2") as pharmacy_form:
                        pharmacy_form.visible = False
                        ui.label("PHARMACY NAME").classes("text-sm font-semibold text-gray-700")
                        ui.input(placeholder="Enter pharmacy name").props("outlined").classes("w-full mb-4")
                        ui.label("PHARMACY EMAIL").classes("text-sm font-semibold text-gray-700")
                        ui.input(placeholder="Enter email").props("outlined").classes("w-full mb-4")
                        ui.label("PASSWORD").classes("text-sm font-semibold text-gray-700")
                        ui.input(placeholder="Enter your password", password=True).props("outlined").classes("w-full mb-4")
                        ui.label("CONFIRM PASSWORD").classes("text-sm font-semibold text-gray-700")
                        ui.input(placeholder="Confirm password", password=True).props("outlined").classes("w-full mb-8")
                        ui.button("Sign Up as Pharmacy", on_click=lambda: ui.notify("Pharmacy Sign Up clicked")).classes("w-full bg-blue-300 text-white font-semibold py-2 rounded-full")

                # Toggle Logic
                state = {'selected_role': None}
                def select_role(role):
                    if state['selected_role'] == role:
                        user_form.visible = False
                        pharmacy_form.visible = False
                        user_button.classes(remove='border-blue-300', add='border-gray-200')
                        user_icon.classes(remove='text-blue-300', add='text-gray-500')
                        user_label.classes(remove='text-blue-300', add='text-gray-500')
                        pharmacy_button.classes(remove='border-blue-300', add='border-gray-200')
                        pharmacy_icon.classes(remove='text-blue-300', add='text-gray-500')
                        pharmacy_label.classes(remove='text-blue-300', add='text-gray-500')
                        state['selected_role'] = None
                        return

                    state['selected_role'] = role
                    if role == 'user':
                        user_form.visible = True
                        pharmacy_form.visible = False
                        user_button.classes(remove='border-gray-200', add='border-blue-300')
                        user_icon.classes(remove='text-gray-500', add='text-blue-300')
                        user_label.classes(remove='text-gray-500', add='text-blue-300')
                        pharmacy_button.classes(remove='border-blue-300', add='border-gray-200')
                        pharmacy_icon.classes(remove='text-blue-300', add='text-gray-500')
                        pharmacy_label.classes(remove='text-blue-300', add='text-gray-500')
                    else:
                        user_form.visible = False
                        pharmacy_form.visible = True
                        pharmacy_button.classes(remove='border-gray-200', add='border-blue-300')
                        pharmacy_icon.classes(remove='text-gray-500', add='text-blue-300')
                        pharmacy_label.classes(remove='text-gray-500', add='text-blue-300')
                        user_button.classes(remove='border-blue-300', add='border-gray-200')
                        user_icon.classes(remove='text-blue-300', add='text-gray-500')
                        user_label.classes(remove='text-blue-300', add='text-gray-500')

                user_button.on('click', lambda: select_role('user'))
                pharmacy_button.on('click', lambda: select_role('pharmacy'))

