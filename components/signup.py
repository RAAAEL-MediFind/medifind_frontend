from nicegui import ui
from nicegui.events import UploadEventArguments
import base64
import requests 
import asyncio
from utils.api import base_url # Assuming base_url is in this file

@ui.page("/signup")
def show_signup_page():
    # A dictionary to hold the uploaded file's data for this session
    uploaded_file_data = {}

    # The head_html section with CSS and JavaScript
    ui.add_head_html('''
    <style>
        .typing-cursor::after { content: '|'; animation: blink 1s step-end infinite; }
        @keyframes blink { from, to { color: transparent; } 50% { color: white; } }
    </style>
    <script>
        function typeDeleteAnimation(elementId, text) {
            const element = document.getElementById(elementId);
            if (!element) return;
            let i = 0;
            let isDeleting = false;
            const typingSpeed = 150, deletingSpeed = 75, pauseDuration = 2000;
            function animate() {
                const currentSubstring = text.substring(0, i);
                element.textContent = currentSubstring;
                if (isDeleting) { i--; } else { i++; }
                if (!isDeleting && i > text.length) {
                    isDeleting = true;
                    setTimeout(animate, pauseDuration);
                } else if (isDeleting && i < 0) {
                    isDeleting = false;
                    i = 0;
                    setTimeout(animate, 500);
                } else {
                    setTimeout(animate, isDeleting ? deletingSpeed : typingSpeed);
                }
            }
            animate();
        }
        document.addEventListener('DOMContentLoaded', (event) => {
            typeDeleteAnimation('welcome-text', 'Welcome to Medifind');
        });
    </script>
    ''')

    with ui.grid(columns=2).classes('w-full min-h-screen'):
        # --- Left Welcome Column ---
        with ui.column().classes("w-full bg-cover bg-no-repeat bg-center relative").style("background-image:url(/assets/signup.png)"):
            with ui.column().classes("absolute inset-0 bg-black/60 flex items-center justify-center"):
                with ui.column().classes("text-center items-center max-w-sm"):
                    ui.label().classes("text-white font-extrabold text-4xl typing-cursor h-12").props('id="welcome-text"')
                    ui.label("Already have an account? Sign in to stay connected.").classes("text-white text-lg")
                    ui.element("div").classes("h-8")
                    ui.button("SIGN IN", on_click=lambda: ui.navigate.to('/signin')).classes("bg-blue text-white font-semibold px-8 py-2 rounded-full")

        # --- Right Form Column ---
        with ui.column().classes("w-full flex items-center justify-start pt-20 bg-white"):
            with ui.column().classes('w-[500px] px-8'):
                with ui.column().classes('w-full items-center mb-8'):
                    ui.label("MEDIFIND").classes("text-5xl font-bold text-blue").style('letter-spacing: 0.1em')
                    ui.image("assets/signuplog.png").classes("items-center w-[250px] h-[100px] mt-0 ")
                    ui.label("...because the right care shouldn't be hard to find").classes("text-sm font-normal text-gray-500 mt-1 tracking-wide")

                ui.label("Create Account").classes("text-2xl font-bold mt-4 mb-2 text-gray-800")
                ui.label("Choose your role:").classes("text-md font-semibold text-gray-600 mb-4")

                with ui.row().classes('w-full justify-start gap-4 mb-6'):
                    user_button = ui.card().classes('w-32 h-24 flex flex-col items-center justify-center cursor-pointer border-2 border-gray-200 rounded-lg transition-all hover:border-blue-300 hover:shadow-lg')
                    with user_button:
                        user_icon = ui.icon('person_outline', size='0.5').classes('text-gray-500')
                        user_label = ui.label('User').classes('text-gray-500 font-semibold')
                    pharmacy_button = ui.card().classes('w-32 h-24 flex flex-col items-center justify-center cursor-pointer border-2 border-gray-200 rounded-lg transition-all hover:border-blue-300 hover:shadow-lg')
                    with pharmacy_button:
                        pharmacy_icon = ui.icon('medical_services', size='0.5').classes('text-gray-500')
                        pharmacy_label = ui.label('Pharmacy').classes('text-gray-500 font-semibold')
                
                with ui.column().classes("w-full relative h-[400px]"):
                    # --- User Form ---
                    with ui.column().classes("w-full absolute top-0 left-0 overflow-y-auto h-full pr-2") as user_form:
                        user_form.visible = False
                        ui.label("YOUR FULL NAME").classes("text-sm font-semibold text-gray-700")
                        user_username = ui.input(placeholder="Enter your name").props("outlined").classes("w-full mb-4")
                        ui.label("YOUR EMAIL").classes("text-sm font-semibold text-gray-700")
                        user_email = ui.input(placeholder="Enter email").props("outlined").classes("w-full mb-4")
                        ui.label("PHONE NUMBER").classes("text-sm font-semibold text-gray-700")
                        user_phone = ui.input(placeholder="Enter phone number").props("outlined").classes("w-full mb-4")
                        ui.label("PASSWORD").classes("text-sm font-semibold text-gray-700")
                        user_password = ui.input(placeholder="Enter your password", password=True).props("outlined").classes("w-full mb-4")
                        ui.label("CONFIRM PASSWORD").classes("text-sm font-semibold text-gray-700")
                        user_confirm_password = ui.input(placeholder="Confirm password", password=True).props("outlined").classes("w-full mb-8")
                        ui.button("Sign Up as User", on_click=lambda: handle_signup('user')).classes("w-full bg-blue-300 text-white font-semibold py-2 rounded-full")

                    # --- Pharmacy Form ---
                    with ui.column().classes("w-full absolute top-0 left-0 overflow-y-auto h-full pr-2") as pharmacy_form:
                        pharmacy_form.visible = False
                        ui.label("PHARMACY NAME").classes("text-sm font-semibold text-gray-700")
                        pharma_username = ui.input(placeholder="Enter pharmacy name").props("outlined").classes("w-full mb-4")
                        ui.label("PHARMACY EMAIL").classes("text-sm font-semibold text-gray-700")
                        pharma_email = ui.input(placeholder="Enter email").props("outlined").classes("w-full mb-4")
                        ui.label("PHONE NUMBER").classes("text-sm font-semibold text-gray-700")
                        pharma_phone = ui.input(placeholder="Enter phone number").props("outlined").classes("w-full mb-4")
                        ui.label("LICENSE NUMBER").classes("text-sm font-semibold text-gray-700")
                        pharma_license = ui.input(placeholder="License number").props("outlined").classes("w-full mb-4")
                        ui.label("GPS ADDRESS").classes("text-sm font-semibold text-gray-700")
                        pharma_address = ui.input(placeholder="Gps Address").props("outlined").classes("w-full mb-4")
                        
                        ui.label("PHARMACY IMAGE (Flyer)").classes("text-sm font-semibold text-gray-700")
                        image_preview = ui.image().classes("w-32 h-32 object-cover rounded-lg my-2")
                        image_preview.visible = False
                        
                        async def handle_upload(e: UploadEventArguments):
                            try:
                                file = e.file
                                if not file:
                                    ui.notify('No file was uploaded.', color='negative')
                                    return
                                
                                content = await file.read()
                                file_name = getattr(file, 'name', 'flyer')
                                file_type = getattr(file, 'content_type', 'application/octet-stream')

                                uploaded_file_data.clear()
                                uploaded_file_data['name'] = file_name
                                uploaded_file_data['content'] = content
                                uploaded_file_data['type'] = file_type
                                
                                b64_content = base64.b64encode(content).decode('utf-8')
                                data_url = f"data:{file_type};base64,{b64_content}"
                                
                                image_preview.set_source(data_url)
                                image_preview.set_visibility(True)
                                
                                ui.notify(f'Uploaded {file_name}')
                            except Exception as ex:
                                ui.notify(f'Could not process file: {ex}', color='negative')
                        
                        ui.upload(on_upload=handle_upload, auto_upload=True, max_files=1, label="Upload Picture").classes("w-full mb-4")

                        ui.label("PASSWORD").classes("text-sm font-semibold text-gray-700")
                        pharma_password = ui.input(placeholder="Enter your password", password=True).props("outlined").classes("w-full mb-4")
                        ui.label("CONFIRM PASSWORD").classes("text-sm font-semibold text-gray-700")
                        pharma_confirm_password = ui.input(placeholder="Confirm password", password=True).props("outlined").classes("w-full mb-8")
                        ui.button("Sign Up as Pharmacy", on_click=lambda: handle_signup('pharmacy')).classes("w-full bg-blue-300 text-white font-semibold py-2 rounded-full")

                # --- Backend Integration Logic ---
                def send_request_sync(url, data, files):
                    """Synchronous function to send the request."""
                    try:
                        return requests.post(url, data=data, files=files)
                    except requests.RequestException as e:
                        return e

                async def handle_signup(role: str):
                    endpoint_url = f"{base_url}/users/register"
                    payload_data, files = {}, {}

                    if role == 'user':
                        if user_password.value != user_confirm_password.value:
                            ui.notify("Passwords do not match!", color='negative'); return
                        payload_data = {
                            "username": user_username.value, "email": user_email.value,
                            "phone": user_phone.value, "password": user_password.value,
                            # ##### THIS IS THE FIX: Send 'patient' instead of 'user' #####
                            "role": "patient",
                        }
                    else: # Pharmacy
                        if pharma_password.value != pharma_confirm_password.value:
                            ui.notify("Passwords do not match!", color='negative'); return
                        if 'content' not in uploaded_file_data:
                            ui.notify("Pharmacy flyer is required.", color='negative'); return
                            
                        payload_data = {
                            "username": pharma_username.value, "email": pharma_email.value,
                            "phone": pharma_phone.value, "password": pharma_password.value,
                            "license_number": pharma_license.value, "digital_address": pharma_address.value,
                            "role": "pharmacy",
                        }
                        files['flyer'] = (uploaded_file_data['name'], uploaded_file_data['content'], uploaded_file_data['type'])
                    
                    ui.notify('Submitting form...', spinner=True)
                    response = await asyncio.to_thread(send_request_sync, endpoint_url, payload_data, files)

                    if isinstance(response, requests.Response):
                        if response.status_code in [200, 201]:
                            ui.notify("Registration successful! Please sign in.", color='positive')
                            ui.navigate.to('/signin')
                        else:
                            try:
                                error_detail = response.json().get('detail', 'An unknown error occurred.')
                            except requests.exceptions.JSONDecodeError:
                                error_detail = response.text
                            ui.notify(f"Registration failed: {error_detail}", color='negative', multi_line=True)
                    else:
                        ui.notify(f"Could not connect to the server: {response}", color='negative')
                
                # --- Role Selection Logic ---
                state = {'selected_role': None}
                def select_role(role):
                    if state['selected_role'] == role:
                        user_form.visible, pharmacy_form.visible = False, False
                        user_button.classes(remove='border-blue-300', add='border-gray-200')
                        user_icon.classes(remove='text-blue-300', add='text-gray-500')
                        user_label.classes(remove='text-blue-300', add='text-gray-500')
                        pharmacy_button.classes(remove='border-blue-300', add='border-gray-200')
                        pharmacy_icon.classes(remove='text-blue-300', add='text-gray-500')
                        pharmacy_label.classes(remove='text-blue-300', add='text-gray-500')
                        state['selected_role'] = None
                        return
                    
                    state['selected_role'] = role
                    user_form.visible = (role == 'user')
                    pharmacy_form.visible = (role == 'pharmacy')
                    
                    is_user = (role == 'user')
                    user_button.classes(add='border-blue-300' if is_user else 'border-gray-200', remove='border-gray-200' if is_user else 'border-blue-300')
                    user_icon.classes(add='text-blue-300' if is_user else 'text-gray-500', remove='text-gray-500' if is_user else 'text-blue-300')
                    user_label.classes(add='text-blue-300' if is_user else 'text-gray-500', remove='text-gray-500' if is_user else 'text-blue-300')

                    is_pharmacy = (role == 'pharmacy')
                    pharmacy_button.classes(add='border-blue-300' if is_pharmacy else 'border-gray-200', remove='border-gray-200' if is_pharmacy else 'border-blue-300')
                    pharmacy_icon.classes(add='text-blue-300' if is_pharmacy else 'text-gray-500', remove='text-gray-500' if is_pharmacy else 'text-blue-300')
                    pharmacy_label.classes(add='text-blue-300' if is_pharmacy else 'text-gray-500', remove='text-gray-500' if is_pharmacy else 'text-blue-300')

                user_button.on('click', lambda: select_role('user'))
                pharmacy_button.on('click', lambda: select_role('pharmacy'))
