import reflex as rx
from learningReflex2.components.link_icon import link_icon
from learningReflex2.components.info_text import info_text
import learningReflex2.styles.styles as styles
from learningReflex2.styles.colors import Colors, TextColors
from learningReflex2.styles.fonts import Fonts

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="https://i.pinimg.com/736x/84/00/12/84001281558601329ff08fe876fe6f3a.jpg",
                size="7",
                radius="full",
                border = "4px solid",
                border_color=TextColors.TEXT.value,   
                alt="Icono de perrito",
            ),
            rx.vstack(
                rx.text("Jimmy Valladares", size="6", margin_bottom="0em !important", color=TextColors.HEADER.value),
                rx.text("@jotacode.com", size="2", margin_top="0em !important", color=TextColors.BODY.value),
                rx.hstack(
                    link_icon(name="instagram", url="https://www.instagram.com/andercod/"),
                    link_icon(name="github", url="https://github.com/andercod"),
                    link_icon(name="linkedin", url="https://www.linkedin.com/in/andercod/"),
                ),
                align_items="start",
                justify_content="start",
            ),
            spacing="4"
        ),
        rx.flex(
            info_text(text="Name", body="Jimmy Valladares"),
            rx.spacer(),
            info_text(text="Phone", body="+34 666 666 666"),
            rx.spacer(),
            info_text(text="Location", body="Madrid, Spain"),
            width="100%",
        ),
        rx.text("""
                Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                when an unknown printer took a galley of type and scrambled it to make a type specimen book.
                """,
                color=TextColors.HEADER.value,
                center=True,
                font_size=styles.Size.MEDIUM.value,
                ),
        spacing="3",
        align_items="start",
    )