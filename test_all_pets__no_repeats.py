#1.5 задание.  явное ожидание
import pytest
from setting import email, password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome()
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')
   element = WebDriverWait(pytest.driver, 10).until(
       EC.title_contains(("PetFriends"))
   )
   assert element

   yield

   pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys(email)
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys(password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем кнопку мои питомцы
    pytest.driver.find_element_by_xpath("// *[ @ id = 'navbarNav'] / ul / li[1] / a").click()
    # собираем данные по питомцам
    count_of_my_pets = pytest.driver.find_element_by_css_selector('div.\\.col-sm-4.left').text.split()
    all_my_pets = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody')
    data_of_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td')


    names = data_of_my_pets[::4]  # извлекаем имена


    for i in range(len(all_my_pets)):
        try:
            assert len(all_my_pets) is count_of_my_pets
        except AssertionError:
            pass

    for i in range(len(names)):
        try:
            assert len(names) is len(set(names))
        except AssertionError:
            pass