from nicegui import ui, events, app  # Added app for potential future use
import asyncio

# This variable will hold a reference to the submit button.
_create_ad_btn: ui.button = None

def handle_flyer_upload(e: events.UploadEventArguments):
    """
    Handles the file upload event and displays a notification.
    """
    ui.notify(f"File '{e.name}' uploaded successfully!")

@ui.page("/create_ad")
def show_create_ad_page():
    global _create_ad_btn

    # --- Page Styling ---
    ui.add_head_html(
        """
    <style>
    body {
        margin: 0;
        background:url('/assets/create.jpg') no-repeat center center fixed;
     background-size: cover;
        font-family: 'Poppins', sans-serif;
        color: white;
        overflow: hidden; /* Prevent the main body from scrolling */
    }
    </style>"""
    )

    # --- Main Page Layout ---
    with ui.column().classes("w-full items-center"):
        ui.label("MEDIFIND").classes("text-6xl font-bold text-teal-900") \
    .style('letter-spacing: 0.1em; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);')
        ui.label("...because the right care shouldn't be hard to find").classes("text-sm font-normal text-black mt-1 tracking-wide").style('letter-spacing: 0.1em; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);')

        # --- Form Container ---
        with ui.column().classes(
            "w-full max-w-2xl mx-auto mt-4 p-8 rounded-2xl shadow-2xl bg-white space-y-6 "
            "max-h-[80vh] overflow-y-auto"
        ):
            ui.label("CREATE A NEW AD").classes(
                "font-extrabold text-4xl tracking-wide text-center text-teal-900"
            )

            # --- Input Fields ---
            title = ui.input("Medication Name").props("outlined").classes("w-full")
            description = ui.textarea("Description").props("outlined").classes("w-full")
            price = ui.number("Price").props("outlined").classes("w-full")

            # --- Category Selection ---
            ui.label("Categories").classes("font-medium text-gray-600")
            categories = (
                ui.select(
                    [
                        "ANALGESICS", "ANTIBIOTICS", "ANTI HYPERTENSIVES",
                        "ANTI DIABETICS", "ANTI VIRAL", "ANTI ULCERS",
                    ]
                )
                .classes("w-full text-gray-800")
                .props('outlined popup-content-class="text-gray-800"')
            )
            stock= ui.number("Available Stock").props("outlined").classes("w-full")

            # --- STEP 1: Create a container for the uploader ---
            upload_container = ui.column().classes('w-full gap-0')
            flyer: ui.upload = None  # Initialize flyer variable

            # --- STEP 2: Create a function to build the uploader ---
            def build_uploader():
                nonlocal flyer
                upload_container.clear()  # Clear the container first
                with upload_container:
                    ui.label("Upload image").classes("font-medium text-gray-600")
                    flyer = (
                        ui.upload(on_upload=handle_flyer_upload)
                        .classes("w-full rounded-lg border border-dashed border-gray-400 p-4")
                        .props("color=teal")
                    )

            async def submit():
                if not title.value:
                    ui.notify("Please enter a title.", color="negative")
                    return

                _create_ad_btn.props(add="disable loading")
                await asyncio.sleep(2)
                _create_ad_btn.props(remove="disable loading")
                ui.notify(f"Ad '{title.value}' submitted successfully!", color="positive")

                # --- Clear the form fields for the next entry ---
                title.value = ""
                description.value = ""
                price.value = None
                categories.value = None

                # --- STEP 3: Rebuild the uploader to completely reset it ---
                build_uploader()

            # --- Submit Button ---
            _create_ad_btn = (
                ui.button("Submit", on_click=submit)
                .classes(
                    "mt-6 bg-orange-500 hover:bg-orange-600 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full"
                ).props("color=teal")
            )
            ui.button('Cancel', on_click=lambda: ui.navigate.to('/pharmacydashboard')).classes(
                    "mt-6 bg-orange-500 hover:bg-orange-600 text-white font-semibold py-3 px-6 rounded-xl shadow-md w-full"
                ).props("color=teal")
            

            # Build the uploader for the first time
            build_uploader()