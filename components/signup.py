from nicegui import ui
from components.navbar import show_navbar

@ui.page("/signup")
def show_signup_page():
    """Displays the main signup page with a split-screen layout."""
    show_navbar()
    
    with ui.grid(columns=2).classes('w-full h-screen'):
        # Left side: This column has the background image and takes up the full screen height.
        with ui.column().classes("w-full h-screen bg-cover bg-no-repeat bg-center items-center justify-center flex").style("background-image:url(/assets/signup.png)"):
            with ui.column().classes("text-center items-center bg-black/60 p-8 rounded-xl max-w-sm"):
                ui.label("Welcome to Medifind").classes("text-white font-extrabold text-4xl")
                ui.label("Already have an account? Sign in to stay connected.").classes("text-white text-lg")
                ui.element("div").classes("h-8")  # A small spacer
                ui.button("SIGN IN", on_click=lambda: ui.navigate('/login')).classes("bg-grey text-purple-600 font-semibold px-8 py-2 rounded-full")

        # Right side with the sign-up forms.
        with ui.column().classes("w-full flex items-center justify-start pt-16"):
            with ui.column().classes('w-[500px]'): # This container holds the form
                # New column to center the title and tagline.
                with ui.column().classes('w-full items-center mb-8'):
                    ui.label("MEDIFIND").classes("text-5xl font-bold text-purple-600").style('letter-spacing: 0.1em')
                    ui.label("...because the right care shouldn't be hard to find").classes("text-sm text-black mt-1").style('font-style: italic;')

                ui.label("Create Account").classes("text-2xl font-bold mt-4 mb-2")
                ui.label("Choose your role:").classes("text-md font-semibold text-gray-600 mb-4")

                #  Role Selection Buttons
                with ui.row().classes('w-full justify-start gap-4 mb-6') as role_selection:
                    user_button = ui.card().classes('w-32 h-24 flex flex-col items-center justify-center cursor-pointer border-2 border-gray-200 rounded-lg')
                    with user_button:
                        user_icon = ui.icon('person_outline', size='0.5').classes('text-gray-500')
                        user_label = ui.label('User').classes('text-gray-500 font-semibold')

                    pharmacy_button = ui.card().classes('w-32 h-24 flex flex-col items-center justify-center cursor-pointer border-2 border-gray-200 rounded-lg')
                    with pharmacy_button:
                        pharmacy_icon = ui.icon('medical_services', size='0.5').classes('text-gray-500')
                        pharmacy_label = ui.label('Pharmacy').classes('text-gray-500 font-semibold')

                #  Forms Container
                with ui.column().classes("w-full") as user_form:
                    user_form.visible = False
                    ui.label("YOUR FULL NAME").classes("text-sm font-semibold text-gray-700")
                    ui.input(placeholder="Enter your name").props("outlined").classes("w-full mb-4")
                    ui.label("YOUR EMAIL").classes("text-sm font-semibold text-gray-700")
                    ui.input(placeholder="Enter email").props("outlined").classes("w-full mb-4")
                    ui.label("PASSWORD").classes("text-sm font-semibold text-gray-700")
                    ui.input(placeholder="Enter your password", password=True).props("outlined").classes("w-full mb-4")
                    ui.label("CONFIRM PASSWORD").classes("text-sm font-semibold text-gray-700")
                    ui.input(placeholder="Confirm password", password=True).props("outlined").classes("w-full mb-8")
                    ui.button("Sign Up as User", on_click=lambda: ui.notify("User Sign Up clicked")).classes("w-full bg-purple-600 text-white font-semibold py-2 rounded-full")

                with ui.column().classes("w-full") as pharmacy_form:
                    pharmacy_form.visible = False
                    ui.label("PHARMACY NAME").classes("text-sm font-semibold text-gray-700")
                    ui.input(placeholder="Enter pharmacy name").props("outlined").classes("w-full mb-4")
                    ui.label("PHARMACY EMAIL").classes("text-sm font-semibold text-gray-700")
                    ui.input(placeholder="Enter email").props("outlined").classes("w-full mb-4")
                    ui.label("PASSWORD").classes("text-sm font-semibold text-gray-700")
                    ui.input(placeholder="Enter your password", password=True).props("outlined").classes("w-full mb-4")
                    ui.label("CONFIRM PASSWORD").classes("text-sm font-semibold text-gray-700")
                    ui.input(placeholder="Confirm password", password=True).props("outlined").classes("w-full mb-8")
                    ui.button("Sign Up as Pharmacy", on_click=lambda: ui.notify("Pharmacy Sign Up clicked")).classes("w-full bg-purple-600 text-white font-semibold py-2 rounded-full")

                # Toggle Logic
                # Use a dictionary to hold the state of the selected role.
                state = {'selected_role': None}

                def select_role(role):
                    # If the clicked role is already selected, deselect it and hide the forms.
                    if state['selected_role'] == role:
                        user_form.visible = False
                        pharmacy_form.visible = False
                        # Reset both buttons to inactive style
                        user_button.classes(remove='border-purple-600', add='border-gray-200')
                        user_icon.classes(remove='text-purple-600', add='text-gray-500')
                        user_label.classes(remove='text-purple-600', add='text-gray-500')
                        pharmacy_button.classes(remove='border-purple-600', add='border-gray-200')
                        pharmacy_icon.classes(remove='text-purple-600', add='text-gray-500')
                        pharmacy_label.classes(remove='text-purple-600', add='text-gray-500')
                        state['selected_role'] = None
                        return

                    # Otherwise, set the new role as active.
                    state['selected_role'] = role
                    if role == 'user':
                        user_form.visible = True
                        pharmacy_form.visible = False
                        # Style User button as active
                        user_button.classes(remove='border-gray-200', add='border-purple-600')
                        user_icon.classes(remove='text-gray-500', add='text-purple-600')
                        user_label.classes(remove='text-gray-500', add='text-purple-600')
                        # Style Pharmacy button as inactive
                        pharmacy_button.classes(remove='border-purple-600', add='border-gray-200')
                        pharmacy_icon.classes(remove='text-purple-600', add='text-gray-500')
                        pharmacy_label.classes(remove='text-purple-600', add='text-gray-500')
                    else:
                        user_form.visible = False
                        pharmacy_form.visible = True
                        # Style Pharmacy button as active
                        pharmacy_button.classes(remove='border-gray-200', add='border-purple-600')
                        pharmacy_icon.classes(remove='text-gray-500', add='text-purple-600')
                        pharmacy_label.classes(remove='text-gray-500', add='text-purple-600')
                        # Style User button as inactive
                        user_button.classes(remove='border-purple-600', add='border-gray-200')
                        user_icon.classes(remove='text-purple-600', add='text-gray-500')
                        user_label.classes(remove='text-purple-600', add='text-gray-500')

                user_button.on('click', lambda: select_role('user'))
                pharmacy_button.on('click', lambda: select_role('pharmacy'))

                # "Or" divider and Google sign-up remain common for both
                with ui.row().classes('w-full items-center my-4'):
                    ui.element('div').classes('flex-grow h-[1px] bg-gray-300')
                    ui.label('or').classes('text-gray-500 mx-4')
                    ui.element('div').classes('flex-grow h-[1px] bg-gray-300')

                def signup_with_google():
                    ui.notify('Redirecting to Google sign-up...')

                with ui.button(on_click=signup_with_google).props('outline').classes('w-full text-gray-700 border border-gray-300 hover:bg-gray-100 py-2 rounded-full'):
                    with ui.row().classes('w-full items-center justify-center no-wrap'):
                        ui.image('https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg').classes('w-5 h-5 mr-2')
                        ui.label('Sign up with Google').classes('text-base text-black font-medium')










