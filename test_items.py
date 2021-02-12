import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def is_element_present(browser):
    try:
        browser.implicitly_wait(5)
        browser.find_element_by_css_selector(".btn-add-to-basket")
        return True
    except:
        return False

def test_button_add_to_basket(browser):
    browser.get(link)
    assert is_element_present(browser)==True, "Кнопка добавить в корзину не найдена"
    time.sleep(10)
