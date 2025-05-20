import reflex as rx
from learningReflex2.components.navbar import navbar
from learningReflex2.views.header.header import header
from learningReflex2.views.links.links import links
from learningReflex2.components.footer import footer
import learningReflex2.styles.styles as styles

class State(rx.State):
    ...

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin=styles.Size.LARGE.value,
            padding=styles.Size.DEFAULT.value,
            ),
        ),
        footer(),
    )

app = rx.App(
    style=styles.GLOBAL_STYLES,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&display=swap",
        "https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap",
        
    ]
)
app.add_page(
    index,
    title="Jota Code",
    description="Jota Code is a website for learning Reflex",
)
