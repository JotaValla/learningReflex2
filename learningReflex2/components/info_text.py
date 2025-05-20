import reflex as rx
import learningReflex2.styles.styles as styles
from learningReflex2.styles.colors import TextColors, Colors

def info_text(text: str, body:str) -> rx.Component:
   return rx.box(
        rx.text(
            text,
            as_="span",
            font_weight="bold",
            color=TextColors.TEXT.value
        ),
        f" {body}",
        font_size=styles.Size.MEDIUM.value,
        color=TextColors.BODY.value
    )
