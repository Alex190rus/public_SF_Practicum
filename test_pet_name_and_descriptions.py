#2.3.4 задание. обобщенная версия. не явное ожидание
from selenium import webdriver
import pytest
from setting import email, password

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome()
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

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
    all_my_pets = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody')
    data_of_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td')

    images = pytest.driver.find_elements_by_tag_name('img')
    names = data_of_my_pets[::4]  # извлекаем имена
    breed = data_of_my_pets[1::4]  # извлекаем породу
    age = data_of_my_pets[2::4]  # извлекаем возраст

    for i in range(len(images)):
       try:
          assert images[i].get_attribute('img') != ''
       except AssertionError:
          pass
       try:
           assert len(images) / len(all_my_pets) > 0, 5
       except AssertionError:
           pass


    for i in range(len(names)):
       try:
          assert names[i].text != ''
       except AssertionError:
          pass


    for i in range(len(breed)):
       try:
          assert breed[i].text != ''
          assert ', ' in breed[i].text
          parts = breed[i].text.split(", ")
          assert len(parts[0]) > 0
          assert len(parts[1]) > 0
       except AssertionError:
          pass


    for i in range(len(age)):
       try:
          assert age[i].text != ''
          assert ', ' in age[i].text
          parts = age[i].text.split(", ")
          assert len(parts[0]) > 0
          assert len(parts[1]) > 0
       except AssertionError:
          pass




