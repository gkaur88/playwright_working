import re
from playwright.sync_api import expect
from pages.saucedemo_login import LoginPage
from pages.saucedemo_home import HomePage
import pytest



def test_valid_login(page): 
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    page.wait_for_timeout(2000)
    login_page.click_login()
    expect(page.locator(".title")).to_have_text("Products")


def test_invalid_login(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.enter_username("invalid_user")
    login_page.enter_password("invalid_password")
    page.wait_for_timeout(2000)
    login_page.click_login()
    page.wait_for_timeout(3000)
    expect(page.locator("[data-test='error']")).to_have_text(re.compile(".*Username and password do not match any user in this service.*")) 

def test_home_page_banner_visibility(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    page.wait_for_timeout(2000)
    login_page.click_login()
    home_page = HomePage(page)
    page.wait_for_timeout(6000)
    assert home_page.is_product_banner_visible()
    assert home_page.is_backpack_visible()
    expected_options = ['Name (A to Z)Name (Z to A)Price (low to high)Price (high to low)']
    assert home_page.validate_dropdown_sortby_options(expected_options)

def test_add():
    assert 2 + 3 == 5
