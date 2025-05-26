import reflex as rx

# Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang = 'es'")

preview = "assets/preview_page.png"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitteer:site", "content": "@jotacode"},
]

# index
index_title = "Jota Code | Pagina para aprender Reflex"
index_description = "Jota Code es una pagina para aprender Reflex"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "description", "content": index_description},
]
index_meta.extend(_meta)

# Cursos

courses_title = "Jota Code | Cursos"
courses_description = "Cursos de Reflex para aprender a programar"

course_meta =[
    {"name": "og:title", "content": courses_title},
    {"name": "description", "content": courses_description},
]
course_meta.extend(_meta)