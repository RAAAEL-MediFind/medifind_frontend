from nicegui import ui, app
import requests

from pages.shop import shop_page

# Define the gradient and white styles once for consistency
GRADIENT_STYLE = "background: linear-gradient(180deg, #00a7b1, #02c3b8);"
WHITE_SECTION_STYLE = "background-color: white; color: #333;"

PHARMACIES = [
    {"name": "MediCare", "link_name": "medicare"},
    {"name": "Wellness Rx", "link_name": "wellness_rx"},
    {"name": "Local Drug Mart", "link_name": "local_drug_mart"},
]


@ui.page("/")
def show_main_page():

    ui.add_head_html(
        """
    <style>
    /* Keyframes MUST be here */
    @keyframes floatLeaf {
        0% { transform: translateY(0) rotate(0deg); opacity: 0.8; }
        50% { transform: translateY(-30px) rotate(45deg); opacity: 1; }
        100% { transform: translateY(0) rotate(90deg); opacity: 0.8; }
    }
    /* Device transition style */
    .device-transition {
        transition: transform 0.4s ease;
    }
    </style>
    <script>
    /* JavaScript for mouse tracking MUST be here */
    document.addEventListener("mousemove", (e) => {
        document.querySelectorAll(".device-img, .device-img-small").forEach((el) => {
            const speed = 0.05;
            const x = (window.innerWidth - e.pageX * speed) / 100;
            const y = (window.innerHeight - e.pageY * speed) / 100;
            el.style.transform = `translate(${x}px, ${y}px)`;
        });
    });
    </script>
    """
    )

    with ui.column().classes("w-screen relative pt-24").style(GRADIENT_STYLE):

        with ui.row().classes("items-center w-full -mt-20").style(
            f"display: flex; top: 0; z-index: 100; {GRADIENT_STYLE}"
        ):
            ui.image("assets/medilogo.png").classes(
                "items-center w-[150px] md:w-[250px] h-[75px] md:h-[100px] mt-0 "
            )

            ui.button("PURCHASE ITEM").classes(
                "text-white text-bold items-end md:block md:ml-[800px]"
            ).style(
                "border-radius: 25px; padding: 0.6rem 1.5rem; cursor: pointer; transition: 0.3s ease;"
            ).props(
                "color=#11cdef"
            )

        # GRID: Mobile: 1 column, Desktop: 2 columns
        with ui.grid().classes("w-full grid-cols-1 md:grid-cols-2"):

            # TEXT COLUMN: Responsive padding and text alignment
            with ui.column().classes(
                " items-center px-4 md:px-24 pb-12 md:pb-20 text-center md:text-left z-10 mt-40"
            ):

                # TITLE: Responsive font size
                ui.label("Because the right Care shouldn't be hard to find").classes(
                    "font-extrabold leading-tight mb-8 text-3xl md:text-[3rem] text-white"
                )
                ui.image("assets/h1-slider04 (1).png").classes(
                    "w-[200px] mx-auto md:mx-0"
                )

            # DEVICES ROW: Mobile: stacked, centered; Desktop: row, custom positions
            with ui.row().classes(
                "w-full flex flex-col md:flex-row items-center md:items-end justify-center gap-4 md:gap-8"
            ):

                # Device 1: Laptop (Responsive width and position)
                ui.image("assets/ldp-laptop.png").classes(
                    "w-4/5 md:w-[500px] border-rounded device-img device-transition md:ml-60"
                )

                # Device 2: Tablet (Responsive width and position)
                ui.image("assets/ldp-tablet-02 (1).png").classes(
                    "w-3/5 md:w-[300px] device-img-small device-transition md:mr-40 md:-mt-20"
                )

                # Device 3: Phone (Responsive width and position)
                ui.image("assets/ldp-phone-02.png").classes(
                    "w-3/5 md:w-[300px] device-img-small device-transition md:ml-80 md:-mt-80"
                )

        ui.image("assets/ldp-leaf-03 (1).png").classes("absolute w-[40px]").style(
            "top:20%; left:10%; animation-delay:2s; opacity: 0.8; animation: floatLeaf 10s linear infinite;"
        )
        ui.image("assets/ldp-leaf-03 (1).png").classes("absolute w-[40px]").style(
            "top:50%; left:60%; animation-delay:4s; opacity: 0.8; animation: floatLeaf 10s linear infinite;"
        )
        ui.image("assets/ldp-leaf-03 (1).png").classes("absolute w-[40px]").style(
            "top:70%; left:80%; animation-delay:6s; opacity: 0.8; animation: floatLeaf 10s linear infinite;"
        )

    with ui.grid().classes(
        "w-full p-10 justify-items-center grid-cols-1 md:grid-cols-3"
    ).style(WHITE_SECTION_STYLE):
        for pharmacy in PHARMACIES:

            with ui.card().classes(
                "w-11/12 md:w-[20rem] h-[15rem] shadow-xl hover:shadow-2xl transition duration-300 rounded"
            ):
                ui.link(
                    f"Visit {pharmacy['name']} Home Page",
                    f"/pharmacy/{pharmacy['link_name']}",
                    new_tab=False,
                ).classes("text-lg text-primary")

                ui.image("assets/landing_home11.jpg")

                ui.label(pharmacy["name"]).classes("text-bold text-3xl mt-4")
