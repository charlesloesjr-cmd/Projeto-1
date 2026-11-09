from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def acessar_menu(self, menu: str) -> None:
        self.page.get_by_role("button", name=menu).click()

    def assert_saldo_atual(self, saldo_atual_esperado: str) -> None:
        expect(self.page.get_by_text(saldo_atual_esperado)).to_be_visible()

    def assert_text(self, texto: str) -> None:
        expect(self.page.get_by_text(texto)).to_be_visible()
