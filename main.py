import flet as ft
from index import Login
from menu import exibemenu
from cadastro import cadastro


def main(page: ft.Page):
    page.title = "SmartCheckout"
    page.window_width = 560
    page.window_height = 800


    def abre_menu(e=None):
       exibemenu(page, abre_login)
       
    def abre_login(e=None):
        # passe as três callbacks exigidas por Login
        Login(page, callback_menu=abre_menu, callback_cadastro=abre_cadastro, abre_cadastro=abre_cadastro)

    def abre_cadastro(e=None):
        cadastro(page, abre_login)
    
    abre_login()

ft.app(target=main, assets_dir="assets")