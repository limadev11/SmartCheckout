import flet as ft

def exibe_panfletos(page: ft.Page):
    page.clean()
    page.title = "SmartCheckout - Panfletos"
    
    # Lista de panfletos (imagens)
    panfletos = [
        "panfleto1.png",
        "panfleto2.png",
        "panfleto3.png"
    ]
    
    lista_panfletos = ft.Column(
        [
            ft.Container(
                ft.Image(src=img, width=300, height=400),
                padding=10,
                border_radius=10,
                bgcolor=ft.colors.LIGHT_GRAY,
                shadow=ft.BoxShadow(blur_radius=5)
            )
            for img in panfletos
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )
    
    page.add(
        ft.Column(
            [
                ft.Text("Panfletos de Oferta", size=24, weight="bold"),
                lista_panfletos
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    