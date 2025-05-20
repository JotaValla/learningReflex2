import reflex as rx
from datetime import datetime
import learningReflex2.styles.styles as styles
from learningReflex2.styles.colors import TextColors

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico", width="20px", height="20px", size="20px", border_radius="50%", alt="Icono de reflex"),
        rx.link(
            f"@ 2023 - {datetime.now().year} Reflex App",
            href="https://github.com/reflex-devs/reflex",
            is_external=True,
            color=TextColors.TEXT.value,
        ),
        rx.text(
            "@ Made with love by Jota Code",
            size="2",
            font_weight="bold", 
        ),
        width="100%",
        height="100%",
        justify_content="center",
        align_items="center",
        padding_bottom=styles.Size.MEDIUM.value,
        color=TextColors.FOOTER.value,
    )
    