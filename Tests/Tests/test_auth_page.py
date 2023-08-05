import pytest
from Pages.auth_page import *


def test_successful_authorisation_email(web_browser):
    # успешная авторизация по почте

    page = AuthPage(web_browser)

    page.btn_email.click()
    # нажимаем кнопку почта

    page.email.send_keys(email1)
    # вводим почту

    page.password.send_keys(password1)
    # вводим пароль
    page.btn.click()
    # нажимаем кнопку войти, переходим на страницу с личными данными пользователя




    page.element_user_info.is_presented()
    # дожидаемся присутвия элемента с информацией о фамилии и имени пользователя

    user_info_UI = page.element_user_info.get_attribute('title')
    # из этого элемнета получам информацию о имени и фамилии пользователя странцы

    assert user_info_UI == user_info
#     подтверждаем что имя и фамилия пользователя полученные с элемента страницы совпадают с именем и фамилией
#     зарегистрированого пользователя


def test_successful_authorisation_phone(web_browser):
    # успешная авторизация по телефону

    page = AuthPage(web_browser)


    page.btn_phone.click()
    # нажимаем кнопку телефон

    page.phone.send_keys(phone1)
    # вводим телефон

    page.password.send_keys(password1)
    # вводим пароль
    page.btn.click()
    # нажимаем кнопку "Войти"

    page.element_user_info.is_presented()
    # дожидаемся присутвия элемента с информацией о фамилии и имени пользователя

    user_info_UI = page.element_user_info.get_attribute('title')
    # из этого элемнета получам информацию о имени и фамилии пользователя странцы

    assert user_info_UI == user_info
    #     подтверждаем что имя и фамилия пользователя полученные с элемента страницы совпадают с именем и фамилией
    #     зарегистрированого пользователя


# параметризация негативного теста авторизации по почте
@pytest.mark.parametrize('email1, password1', [
    ('af uagra@inbox.ru', '1Gaim orit'),# Пробелы внутри валидных значений
    ('', ''),                  # Отсутсвие данных
    ( 1, 1),                   # Числа в данных
    ('ЗLСOFjpYШоWЭrмAЯKВmWBцMJцzGтшPqшnDЙDзФГг'
      'иМCeпСghGёcTЕЪYHяёдУжЩЙжМdиЛGbГQfшIUГjWл'
      'MnЯCЗлЫЬcuюSЯкrхJЖSfsjХЦXЛКIТЗъGLЯУdFХрО'
      'ЖШоИVвТvBtШvУАKЫюЛWOeЖzЮГзRnyТВжcЫзеQiEp'
      'oтwUVхвГaиABдиCУULйrюЖoгСзЫZlgтVёIrHлкII'
      'TctHzШЖоМqмЫCЧяGтбсхBБЭёwkфVoKЙkщЮsУdЁэv'
      'меHЖЬTTXбJvЭCLDd', '1Gaimorit'), # Строка более 255 символов в поле email
    ('afuagra@inbox.ru', 'ЗLСOFjpYШоWЭrмAЯKВmWBцMJцzGтшPqшnDЙDзФГг'
      'иМCeпСghGёcTЕЪYHяёдУжЩЙжМdиЛGbГQfшIUГjWл'
      'MnЯCЗлЫЬcuюSЯкrхJЖSfsjХЦXЛКIТЗъGLЯУdFХрО'
      'ЖШоИVвТvBtШvУАKЫюЛWOeЖzЮГзRnyТВжcЫзеQiEp'
      'oтwUVхвГaиABдиCУULйrюЖoгСзЫZlgтVёIrHлкII'
      'TctHzШЖоМqмЫCЧяGтбсхBБЭёwkфVoKЙkщЮsУdЁэv'
      'меHЖЬTTXбJvЭCLDd'),    # Строка более 255 символов в поле password
    ("""№;"?@%صسغذئآ龍門大酒秋瑞<IMG src="#">') # ; -- ☺☻♥♦♣♠•◘""",
       '1Gaimorit'),         # Строка специальных символов в поле email
    ('afuagra@inbox.ru',"""№;"?@%صسغذئآ龍門大酒秋瑞<IMG src="#">') # ; -- ☺☻♥♦♣♠•◘"""),
    # Строка специальных символов в поле password
    ('<script>alert("Поле input уязвимо!")</script>',
       '1Gaimorit'),         # XSS инъекции (JS) в поле email
    ('afuagra@inbox.ru', '<script>alert("Поле input уязвимо!")</script>'),
    # XSS инъекции (JS) в поле password
    ('afuagagra@inbox.ru', '2gAIMORIT'),     # Не верные данные
    ('afuagrainboxru', '1Gaimorit'),     # Адресс электронной почты без "@" и "."
    ('afuagra', '1Gaimorit'),     # Адресс электронной почты без домена
    ('afuagrainbox.ru', '1Gaimorit'),     # Адресс электронной почты без "@"
    ('afuagra@inboxru', '1Gaimorit'),     # Адресс электронной почты без "." в домене
    ('@inbox.ru', '1Gaimorit'),     # Адресс электронной почты состоящий только из домена
    ('afuagra@ximm7ydIHogDQxqOkuVDxA4nvCscVBQuYsVufFrwyK9KjG0RiuRXXetF7YqUdnaSE6Bd.ru', '1Gaimorit'),
    # Адресс электронной в домене которого больше 67 символов
    ])
def test_negative_authorisation_email(web_browser, email1, password1):
    # негативная авторизация по почте

    page = AuthPage(web_browser)

    url = page.get_current_url()
    # присваиваем переменной значение URL страницы авторизации

    page.btn_email.click()
    # нажимаем кнопку почта

    # вводим исключения для прохождения тестов без перерыва при возникновении ошибки AttributeError
    try:
        page.email.send_keys(email1)
        # вводим почту
        page.password.send_keys(password1)
    #     вводим пароль

    except AttributeError:
        print('Введенные данные не соответсвуют формату поля ввода, ПО не дает ввести их')
        # выводим сообщение в консоль об ошибке что говорит о позитивном тесте
        pass

    page.btn.click()
    # нажимаем кнопку войти

    assert page.get_current_url() == url
    #     проверяем что не произошел переход на страницу пользователя, URL соответсвует странице авторизации

    if page.element_wrong_email.is_presented():
        # вводим условие присутвия сообщения о неправельно введеной почте и в случае его выполнения текст сообщения проверяем на соответствие к ниже перечисленным
        assert page.element_wrong_email.get_text() == 'Введите адрес, указанный при регистрации' or page.element_wrong_email.get_text() == 'Неверный формат адресса mail'
    else:
         # иначе проверяем что кнопка "Забыл пароль" приобрела другой цвет(измение ее класса)
         assert page.element_forgot_pas.get_attribute('class') == 'rt-link rt-link--orange login-form__forgot-pwd login-form__forgot-pwd--animated'

 # параметризация негативного теста авторизации по телефону
@pytest.mark.parametrize('phone1, password1', [
    ('9853 462923', '1Gaim orit'),# Пробелы внутри валидных значений
    ('', ''),                  # Отсутсвие данных
    ('9853462923', ''),        # Отсутсвие пароля
    ( 1, 1),                   # Числа в данных
    ('', '1Gaimorit'),        # Отсутсвие номера телефона
    ('1', '1Gaimorit'),        # одна цифра в номере телефона
    ('123456789', '1Gaimorit'), # 9 цифр в номере телефона
    ('12345678901', '1Gaimorit'), # 11 цифр в номере телефона
    ('0000000000', '1Gaimorit'),# Все нули в номере телефона
    ('ЗLСOFjpYШоWЭrмAЯKВmWBцMJцzGтшPqшnDЙDзФГг'
      'иМCeпСghGёcTЕЪYHяёдУжЩЙжМdиЛGbГQfшIUГjWл'
      'MnЯCЗлЫЬcuюSЯкrхJЖSfsjХЦXЛКIТЗъGLЯУdFХрО'
      'ЖШоИVвТvBtШvУАKЫюЛWOeЖzЮГзRnyТВжcЫзеQiEp'
      'oтwUVхвГaиABдиCУULйrюЖoгСзЫZlgтVёIrHлкII'
      'TctHzШЖоМqмЫCЧяGтбсхBБЭёwkфVoKЙkщЮsУdЁэv'
      'меHЖЬTTXбJvЭCLDd', '1Gaimorit'), # Строка более 255 в номере телефона
    ('9853462923', 'ЗLСOFjpYШоWЭrмAЯKВmWBцMJцzGтшPqшnDЙDзФГг'
      'иМCeпСghGёcTЕЪYHяёдУжЩЙжМdиЛGbГQfшIUГjWл'
      'MnЯCЗлЫЬcuюSЯкrхJЖSfsjХЦXЛКIТЗъGLЯУdFХрО'
      'ЖШоИVвТvBtШvУАKЫюЛWOeЖzЮГзRnyТВжcЫзеQiEp'
      'oтwUVхвГaиABдиCУULйrюЖoгСзЫZlgтVёIrHлкII'
      'TctHzШЖоМqмЫCЧяGтбсхBБЭёwkфVoKЙkщЮsУdЁэv'
      'меHЖЬTTXбJvЭCLDd'),    # Строка более 255 символов в поле password
    ("""№;"?@%صسغذئآ龍門大酒秋瑞<IMG src="#">') # ; -- ☺☻♥♦♣♠•◘""",
       '1Gaimorit'),         # Строка специальных символов в в номере телефона
    ('9853462923', """№;"?@%صسغذئآ龍門大酒秋瑞<IMG src="#">') # ; -- ☺☻♥♦♣♠•◘"""),
    # Строка специальных символов в поле password
    ('<script>alert("Поле input уязвимо!")</script>',
       '1Gaimorit'),         # XSS инъекции (JS) в в номере телефона
    ('9853462923', '<script>alert("Поле input уязвимо!")</script>'),
    # XSS инъекции (JS) в поле password
    ('1234567890', '2gAIMORIT'),     # Не верные данные
    ])
def test_negative_authorisation_phone(web_browser, phone1, password1):
    # негативная авторизация по телефону

    page = AuthPage(web_browser)

    url = page.get_current_url()
    # присваиваем переменной значение URL страницы авторизации

    page.btn_phone.click()
    # нажимаем кнопку телефон

    # вводим исключения для прохождения тестов без перерыва при возникновении ошибки AttributeError
    try:
        page.phone.send_keys(phone1)
        # вводим телефон

        page.password.send_keys(password1)
    #     вводим пароль
    except AttributeError:
        print('Введенные данные не соответсвуют формату поля ввода, ПО не дает ввести их')
        # выводим сообщение в консоль об ошибке что говорит о позитивном тесте
        pass
    page.btn.click()
    # нажимаем кнопку войти


    assert page.get_current_url() == url
    #     проверяем что не произошел переход на страницу пользователя, URL соответсвует странице авторизации

    if page.element_wrong_phone.is_presented():
        # вводим условие присутвия сообщения о неправельно введеном телефоне и в случае его выполнения текст сообщения проверяем на соответствие к ниже перечисленным
        assert page.element_wrong_phone.get_text() == 'Введите номер телефона' or page.element_wrong_phone.get_text() == 'Неверный формат телефона'

    # иначе проверяем что кнопка "Забыл пароль" приобрела другой цвет(измение ее класса)
    else:
        assert page.element_forgot_pas.get_attribute('class') == 'rt-link rt-link--orange login-form__forgot-pwd login-form__forgot-pwd--animated'
