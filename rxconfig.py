import reflex as rx


config = rx.Config(
    app_name="learningReflex2",
    cors_allow_origins=[
        "https://localhost:3000",
        "https://learning-reflex.vercel.app/", 
    ],
)