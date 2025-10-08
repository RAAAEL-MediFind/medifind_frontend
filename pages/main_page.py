from nicegui import ui, app
from components.footer import show_footer
import requests


@ui.page("/")
def show_main_page():
    ui.add_head_html(
        """
    <style>
    body {
    margin: 0;
    background: linear-gradient(180deg, #00a7b1, #02c3b8);
    font-family: 'Poppins', sans-serif;
    color: white;
    overflow-x: hidden;
    }

    .hero-title {
    font-size: 3rem;
    font-weight: 700;
    line-height: 1.3;
    margin-bottom: 2rem;
    }

    @keyframes floatLeaf {
    0% { transform: translateY(0) rotate(0deg); opacity: 0.8; }
    50% { transform: translateY(-30px) rotate(45deg); opacity: 1; }
    100% { transform: translateY(0) rotate(90deg); opacity: 0.8; }
    }

    /* Responsive */
    @media (max-width: 768px) {
    .hero-section {
        padding: 7rem 2rem;
    }
    .hero-title {
        font-size: 2.2rem;
    }
    .device-container {
        flex-direction: column;
        align-items: center;
    }
    .device-img {
        width: 90%;
    }
    .device-img-small {
        width: 120px;
    }
    }
    </style>

    <script>
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

    with ui.header().classes("items-center bg-transparent fixed w-[100%]").style(
        "display: flex; top: 0; z-index: 100;"
    ):
        ui.image("assets/medilogo.png").classes(
            "items-center ml-[400px] w-[250px] h-[100px] mt-0 "
        )

        ui.button("PURCHASE THEME").classes(
            "text-white text-bold items-end ml-[600px]"
        ).style(
            "border-radius: 25px; padding: 0.6rem 1.5rem;   cursor: pointer; transition: 0.3s ease;"
        ).props(
            "color=#11cdef"
        )

    with ui.grid(columns=2).classes():
        with ui.column().classes().style("padding: 8rem 6rem 5rem 6rem; z-index: 10;"):
            ui.label("Professional Medicine Shop & A Cluster of Pharmacies").classes(
                "hero-title"
            )
            ui.image("assets/h1-slider04 (1).png").classes("w-[200px]")

        with ui.row().style("display: flex; align-items: flex-end; gap: 2rem;"):
            ui.image("assets/ldp-laptop.png").classes(
                "w-[500px] border-rounded ml-60"
            ).style("transition: transform 0.4s ease;")
            ui.image("assets/ldp-tablet-02 (1).png").classes(
                "w-[300px] mr-40 -mt-20"
            ).style("transition: transform 0.4s ease;")
            ui.image("assets/ldp-phone-02.png").classes("w-[300px] ml-80 -mt-80").style(
                " transition: transform 0.4s ease;"
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

    show_footer()
