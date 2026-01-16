import flet as ft

def cadastro(page: ft.Page, abre_login):
    page.clean()
    page.title = "SmartCheckout - Cadastro"
    
    img = ft.Container(
        content=ft.Image(src="assets/logo.png", width=200, height=200,fit=ft.ImageFit.CONTAIN),
        
        padding=20,
    )

    input_nome = ft.TextField(
        value="",
        label="Nome",
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLACK,
        border_radius=8,
    )

    input_email = ft.TextField(
        value="",
        label="Email",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLACK,
        border_radius=8,
    )

    input_senha = ft.TextField(
        value="",
        label="Senha",
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLACK,
        border_radius=8,
        password=True,
        can_reveal_password=True,
    )

    btn_cadastrar = ft.ElevatedButton(
        text="Cadastrar",
        bgcolor=ft.Colors.BLUE_300,
        color=ft.Colors.WHITE,
        width=200,
        height=50,
        on_click=abre_login,
    )

    cadastro_container = ft.Container(
        content=ft.Column(
            controls=[
                img,
                input_nome,
                input_email,
                input_senha,
                btn_cadastrar,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        
        padding=30,
        )
    
    page.add(cadastro_container)
    page.update()
    