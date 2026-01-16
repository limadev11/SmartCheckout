import flet as ft

from cadastro import cadastro


def Login (page: ft.Page, callback_menu,callback_cadastro,abre_cadastro):
    page.clean()

    img = ft.Container(
        content=ft.Image(src="assets/logo.png", width=200, height=200),
        padding=20,
    )

    input_email = ft.TextField(
        value="",
        label="Email",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_300,
        border_radius=8,
    )

    input_senha = ft.TextField(
        value="",
        label="Senha",
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_300,
        border_radius=8,
        password=True,
        can_reveal_password=True,
    )

    btn_entrar = ft.ElevatedButton(
        "Entrar",
        bgcolor=ft.Colors.BLUE_300,
        color=ft.Colors.WHITE,
        width=200,
        height=50,
        on_click=callback_menu,
    )

    btn_cadastro = ft.TextButton(
        "Não tem uma conta? Cadastre-se",
        style=ft.ButtonStyle(
            text_style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
        ),
        on_click=abre_cadastro,
    )

    login_container = ft.Container(
        content=ft.Column(
            controls=[
                img,
                input_email,
                input_senha,
                btn_entrar,
                btn_cadastro,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=30,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        width=400,
        height=600,
        
    )
    page.add(login_container)
    page.update()