from nicegui import ui, app
from components.navbar import show_navbar
from components.footer import show_footer
import requests

PHARMACIES = [
    {"name": "MediCare", "link_name": "medicare"},
    {"name": "Wellness Rx", "link_name": "wellness_rx"},
    {"name": "Local Drug Mart", "link_name": "local_drug_mart"},
]


@ui.page("/pharmacy/{name}")
def show_pharmacy_page(name: str):

    # Get the friendly name from the link_name
    pharmacy_info = next(
        (p for p in PHARMACIES if p["link_name"] == name),
        {"name": name.replace("_", " ").title()},
    )
    pharmacy_name = pharmacy_info["name"]

    ui.page_title(f"{pharmacy_name} - Shop Home")

    # Minimal head HTML to set the font/body margin
    ui.add_head_html(
        """
    <style>
        body { margin: 0; font-family: 'Poppins', sans-serif; }
        .hero-bg { 
            background-color: #f0f7fa; /* Light blue/grey background */
            /* Add padding and positioning for the background elements */
            padding-bottom: 500px; /* Ensure space for the full hero section */
        }
        .search-container {
            width: 100%;
            max-width: 600px;
        }
    </style>
    """
    )

    # 2. HERO CONTENT SECTION (Light Blue Background)
    with ui.column().classes("w-full items-center pt-20 relative hero-bg min-h-screen"):

        # === Hero Text ===
        ui.label("What Are You Looking For?").classes(
            "text-5xl font-extrabold text-gray-800 mt-16"
        )
        ui.label("The pharmacy that really delivers").classes(
            "text-lg text-gray-600 mt-2 mb-10"
        )

        # === Search Bar Component (Categories + Input) ===
        with ui.row().classes(
            "search-container shadow-lg rounded-full overflow-hidden bg-white"
        ):

            # Categories Dropdown (Tailwind only)
            with ui.row().classes(
                "px-4 py-3 border-r border-gray-200 items-center hidden sm:flex"
            ):
                ui.select(
                    options=["All categories", "Prescription", "OTC", "Vitamins"],
                    value="All categories",
                ).classes("bg-white text-sm w-36 ").props("borderless dense")

            # Search Input
            ui.input(placeholder="search product").classes(
                "flex-grow bg-white text-lg h-full"
            ).props("borderless dense")

            # Search Icon
            ui.button(icon="search").props("flat color=black text-primary").classes(
                "text-lg w-16 h-full"
            )

        ui.image("assets/product_tube.png").classes(
            "absolute w-[300px] right-[10%] bottom-[10%] transform -translate-y-1/2"
        ).style("z-index: 1;")

        ui.image("assets/blister_pack.png").classes(
            "absolute w-[200px] top-[10%] left-[5%] opacity-70 rotate-[-15deg]"
        )

        # Add a clear link back to the main directory
        ui.button("Back to Directory", on_click=lambda: ui.open("/")).classes(
            "mt-12 mb-4 bg-primary-dark"
        ).props("flat").style("z-index: 10;")

    # Content of the rest of the pharmacy page (e.g., featured products) would go here

    show_footer()
