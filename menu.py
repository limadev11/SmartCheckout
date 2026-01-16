import flet as ft
from produtos import exibeproduto


def exibemenu(page: ft.Page, abre_login):
    page.clean()
    page.title = "SmartCheckout - Menu"
    page.window_width = 560
    page.window_height = 800


    PRIMARY = ft.Colors.BLUE_300
    ACCENT = ft.Colors.BLACK
    ON_PRIMARY = ft.Colors.WHITE
    
    navbar = ft.Container(
        bgcolor=PRIMARY,
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Image(src="assets/logo.png", width=44, height=44),
                    padding=6,
                    bgcolor=ON_PRIMARY,
                    border_radius=8,
                    width=56,
                    height=56,
                ),
                ft.Column(
                    controls=[
                        ft.Text("SmartCheckout", color=ON_PRIMARY, weight=ft.FontWeight.BOLD, size=16),
                    ],
                    spacing=2,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.TextButton(
                            "Home",
                            on_click=lambda e: exibemenu(page, abre_login),
                            style=ft.ButtonStyle(text_style=ft.TextStyle(color=ON_PRIMARY))
                        ),
                        ft.TextButton(
                            "Produtos",
                            on_click=lambda e: exibeproduto(page, abre_login, exibemenu),
                            style=ft.ButtonStyle(text_style=ft.TextStyle(color=ON_PRIMARY))
                        ),
                    ],
                    spacing=8,
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        ),
        border_radius=4,
        width=800,
        height=72,
    )

    accent_line = ft.Container(height=4, bgcolor=ACCENT, width=800)

    body_card = ft.Container(
    expand=True,  # torna responsivo
    content=ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=24,
        controls=[
            # CARD - Escanear Arquivo
            ft.Card(
                elevation=4,
                content=ft.Container(
                    width=480,
                    padding=20,
                    content=ft.Column(
                        spacing=8,
                        controls=[
                            ft.Text(
                                "Escanear (Arquivo)",
                                weight=ft.FontWeight.BOLD,
                                size=16
                            ),
                            ft.Text(
                                "Selecione uma imagem de código de barras.",
                                size=12,
                                color=ft.Colors.BLACK45
                            ),
                            ft.ElevatedButton(
                                "Escolher arquivo",
                                bgcolor=PRIMARY,
                                color=ON_PRIMARY,
                                width=200
                            ),
                        ],
                    ),
                ),
            ),

            # CARD - Escanear Câmera
            ft.Card(
                elevation=4,
                content=ft.Container(
                    width=480,
                    padding=20,
                    content=ft.Column(
                        spacing=8,
                        controls=[
                            ft.Text(
                                "Escanear (Câmera)",
                                weight=ft.FontWeight.BOLD,
                                size=16
                            ),
                            ft.Text(
                                "Abrir câmera.",
                                size=12,
                                color=ft.Colors.BLACK45
                            ),
                            ft.ElevatedButton(
                                "Abrir câmera",
                                bgcolor=ACCENT,
                                color=ft.Colors.WHITE,
                                width=200
                            ),
                        ],
                    ),
                ),
            ),

            # BOTÃO LOGOUT
            ft.ElevatedButton(
                "Logout",
                bgcolor=PRIMARY,
                color=ON_PRIMARY,
                width=200,
                on_click=abre_login
            ),
        ],
    ),
)


    page.add(
        ft.Column(
            controls=[
                navbar,
                ft.Container(height=6),
                accent_line,
                ft.Container(height=18),
                body_card,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        )
    )
    page.update()
