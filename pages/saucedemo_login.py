from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.username_input =  page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.locator("[data-test=\"login-button\"]")

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()
