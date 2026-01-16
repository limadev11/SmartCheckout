import flet as ft
import json


def exibeproduto(page: ft.Page, abre_login, exibemenu_callback):
    page.clean()
    page.title = "SmartCheckout - Produtos"
    page.window_width = 560
    page.window_height = 800

    PRIMARY = ft.Colors.BLUE_300
    ACCENT = ft.Colors.BLACK
    ON_PRIMARY = ft.Colors.WHITE

    # =============================
    # Estados de filtro
    # =============================
    filtros = {
        "empresa": None,   # "BigMais" | "Coelho Diniz" | "MartMinas"
        "estoque": None,   # "sim" | "não" | None
        "busca": "",       # termo de pesquisa
    }

    # =============================
    # Carregar produtos
    # =============================
    try:
        with open("produtos.json", "r", encoding="utf-8") as f:
            produtos = json.load(f)
    except Exception as e:
        print("Erro ao carregar produtos.json:", e)
        produtos = []

    for p in produtos:
        p["estoque"] = "sim" if p.get("quantidade", 5) > 0 else "não"

    # =============================
    # Card do produto
    # =============================
    # =============================
    # Card do produto (SEM LIMITE DE ALTURA)
    # =============================
    def criar_card(produto):
        return ft.Card(
            elevation=2,
            content=ft.Container(
                padding=12,
                content=ft.Column(
                    spacing=6,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Image(
                            src=produto.get("imagem", "assets/img/sem-imagem.png"),
                            height=140, width=200,
                        ),
                        ft.Text(
                            produto["nome"],
                            size=14,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            f"Empresa: {produto.get('empresa', 'N/A')}",
                            size=12
                        ),
                        ft.Text(
                            f"Corredor: {produto.get('corredor', 'N/A')}",
                            size=12
                        ),
                        ft.Text(
                            f"R$ {float(produto.get('preco', 0)):.2f}",
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.GREEN_700
                        ),
                        ft.Text(
                            f"Estoque: {produto.get('estoque', 'N/A')}",
                            size=12,
                            color=ft.Colors.BLUE_GREY
                        ),
                        ft.Divider(),
                        ft.Text(
                            produto.get("descricao", "Sem descrição"),
                            size=12,
                            selectable=True
                        )
                    ]
                )
            )
        )

    # =============================
    # Grid de produtos
    # =============================
    grid_produtos = ft.GridView(
        expand=True,
        max_extent=420,
        spacing=12,
        run_spacing=12,
    )

    # =============================
    # Aplicar todos os filtros
    # =============================
    def aplicar_filtros():
        lista = produtos

        if filtros["empresa"]:
            lista = [p for p in lista if p.get("empresa") == filtros["empresa"]]

        if filtros["estoque"]:
            lista = [p for p in lista if p.get("estoque") == filtros["estoque"]]

        if filtros["busca"]:
            termo = filtros["busca"]
            lista = [p for p in lista if termo in p["nome"].lower()]

        grid_produtos.controls.clear()
        for p in lista:
            grid_produtos.controls.append(criar_card(p))

        page.update()

    # =============================
    # Busca por nome
    # =============================
    campo_busca = ft.TextField(
        label="Pesquisar produto",
        prefix_icon=ft.Icons.SEARCH,
        border_radius=8,
        on_change=lambda e: (
            filtros.update({"busca": e.control.value.lower()}),
            aplicar_filtros(),
        ),
    )

    # =============================
    # Botão dropdown para filtro de estoque
    # =============================
    texto_filtro_estoque = ft.Text("Estoque: Todos", size=12)

    def aplicar_filtro_estoque(valor):
        filtros["estoque"] = valor
        texto_filtro_estoque.value = (
            "Estoque: Em estoque" if valor == "sim"
            else "Estoque: Sem estoque" if valor == "não"
            else "Estoque: Todos"
        )
        aplicar_filtros()
        page.update()

    botao_filtro_estoque = ft.PopupMenuButton(
        content=ft.Row(
            spacing=6,
            controls=[
                ft.Icon(ft.Icons.FILTER_LIST, size=18),
                texto_filtro_estoque,
            ],
        ),
        items=[
            ft.PopupMenuItem(
                "Todos",
                on_click=lambda e: aplicar_filtro_estoque(None),
            ),
            ft.PopupMenuItem(
                "Em estoque",
                on_click=lambda e: aplicar_filtro_estoque("sim"),
            ),
            ft.PopupMenuItem(
                "Sem estoque",
                on_click=lambda e: aplicar_filtro_estoque("não"),
            ),
        ],
    )

    # =============================
    # Filtro por empresa (logos)
    # =============================
    def filtrar_empresa(empresa):
        filtros["empresa"] = None if filtros["empresa"] == empresa else empresa
        atualizar_estilo_logos()
        aplicar_filtros()

    def criar_logo(nome, img):
        return ft.Container(
            width=100,
            height=100,
            border_radius=16,
            padding=10,
            bgcolor=ft.Colors.WHITE,
            data=nome,  # salva o nome da empresa
            content=ft.Image(src=img),
            on_click=lambda e: filtrar_empresa(e.control.data),
        )

    logos_row = ft.Row(
        spacing=16,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            criar_logo("BigMais", "assets/img/bigmais.png"),
            criar_logo("Coelho Diniz", "assets/img/coelhodiniz.png"),
            criar_logo("MartMinas", "assets/img/martminas.png"),
        ],
    )

    def atualizar_estilo_logos():
        for logo in logos_row.controls:
            ativo = logo.data == filtros["empresa"]
            logo.border = ft.border.all(2, PRIMARY) if ativo else None
            logo.bgcolor = ft.Colors.BLUE_50 if ativo else ft.Colors.WHITE
        page.update()

    # =============================
    # Navbar
    # =============================
    navbar = ft.Container(
        bgcolor=PRIMARY,
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text("SmartCheckout", color=ON_PRIMARY, weight=ft.FontWeight.BOLD),
                ft.TextButton(
                    "Home",
                    on_click=lambda e: exibemenu_callback(page, abre_login),
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(color=ON_PRIMARY)
                    ),
                ),
            ],
        ),
    )

    # =============================
    # Corpo
    # =============================
    body = ft.Container(
        expand=True,
        padding=16,
        content=ft.Column(
            spacing=16,
            controls=[
                logos_row,
                botao_filtro_estoque,  # botão dropdown de estoque
                campo_busca,
                ft.Container(expand=True, content=grid_produtos),
            ],
        ),
    )

    page.add(
        ft.Column(
            expand=True,
            controls=[
                navbar,
                body,
            ],
        )
    )

    aplicar_filtros()
