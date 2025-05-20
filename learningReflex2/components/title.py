import reflex as rx
import learningReflex2.styles.styles as styles

def title(title: str) -> rx.Component:
    return rx.heading(
        title,
        size="6",
        style=styles.title_style,
    )
