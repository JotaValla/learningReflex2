import reflex as rx
from learningReflex2.components.link_button import link_button
from learningReflex2.components.title import title
from learningReflex2.routes import Route

def links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_button(title="Python", body="Aprende python", url="https://www.google.com", src_icon="worm"),
        link_button(title="Java", body="Aprende java", url="https://www.google.com", src_icon="coffee"),
        link_button(title="Javascript", body="Aprende javascript", url="https://www.google.com", src_icon="braces"),
        link_button(title="SQL", body="Aprende sql", url="https://www.google.com", src_icon="database"),
        width="100%",
        justify_content="center",
        align_items="center",
        spacing="4",
        padding="4"
    )