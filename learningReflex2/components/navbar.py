import reflex as rx
import learningReflex2.styles.styles as styles
from learningReflex2.styles.colors import Colors, TextColors

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("jota", color=TextColors.TEXT.value, **styles.navbar_style, font_weight="bold", size="1"),
        rx.text("code", color=TextColors.TEXT.value, **styles.navbar_style, size="1"),
        position="sticky",
        padding_x=styles.Size.DEFAULT.value,
        padding_y=styles.Size.SMALL.value,
        top="0",
        spacing="0",
        z_index="999",
        background_color=Colors.SECONDARY.value,
        padding=styles.Size.DEFAULT.value,
    )

