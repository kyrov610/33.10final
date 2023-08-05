import pytest
from Pages.regist_page import *
from Pages.auth_page import *


def test_successful_registrsation_email(web_browser):
    # удачная регистрация по почте

    pageA = AuthPage (web_browser)

    page = RegistPage(web_browser)

    pageA.btn_regist.click()
    # нажимаем кнопку зарегестрироваться, переходим на страницу регстрации

    page.name.send_keys(name2)
    # вводим имя

    page.lastname.send_keys(lastname2)
    # вводим фамилию

    page.email.send_keys(email2)
    # вводим почту

    page.password.send_keys(password2)
    # вводим пароль

    page.password_confirm.send_keys(password2)
    # подтверждаем пароль



    page.btn.click()
    # нажимаем кнопку зарегестрироваться, переходим к форме подтверждени почты

    assert page.element_confirm_code.is_presented()
#     подтверждаем что есть элемент для поля ввода потверждения пароля со страницы подтверждения пароля

def test_registrsation_email_authoris_user(web_browser):
    # регистрация уже авторизированого пользователя по почте

    pageA = AuthPage (web_browser)

    page = RegistPage(web_browser)

    pageA.btn_regist.click()
    # нажимаем кнопку зарегестрироваться, переходим на страницу регстрации

    page.name.send_keys(user_name)
    # вводим имя

    page.lastname.send_keys(user_lastname)
    # вводим фамилию

    page.email.send_keys(email1)
    # вводим почту

    page.password.send_keys(password1)
    # вводим пароль

    page.password_confirm.send_keys(password1)
    # подтверждаем пароль

    page.btn.click()
    # нажимаем кнопку зарегестрироваться, переходим к форме подтверждени почты

    assert page.element_restore_password.is_clickable()
    # подтверждаем что есть элемент - кнопка "Восстановить" пароль из всплывающего окна с сообщением об уже существующей
    # учетной записи



# параметризация для негативных тестов полей имени, фамилии, телефона, пароля, подтверждения пароля
@pytest.mark.parametrize('name2, lastname2, phone2, password2, password21', [
    ('Эрн ест', 'Пот тер', '9853 462924', '1Gai moriT1', '1Gaim oriT1'),  # Пробелы внутри валидных значений
    ('', '', '', '', ''),  # Отсутсвие данных
    ('Э', 'Поттер', '9853462924', '1GaimoriT1', '1GaimoriT1'),  # Имя из одного символа (менее 2 символов)
    ('ЭрнесЭрнесЭрнесЭрнесЭрнесЭрнест', 'Поттер', '9853462924', '1GaimoriT1', '1GaimoriT1'),
    # Имя из 31 (более чем 30 символов)
    ('', 'Поттер', '9853462924', '1GaimoriT1', '1GaimoriT1'),  # Отсутсвие имени
    ('ЗLСOFjpYШоWЭrмAЯKВmWBцMJцzGтшPqшnDЙDзФГг'
     'иМCeпСghGёcTЕЪYHяёдУжЩЙжМdиЛGbГQfшIUГjWл'
     'MnЯCЗлЫЬcuюSЯкrхJЖSfsjХЦXЛКIТЗъGLЯУdFХрО'
     'ЖШоИVвТvBtШvУАKЫюЛWOeЖzЮГзRnyТВжcЫзеQiEp'
     'oтwUVхвГaиABдиCУULйrюЖoгСзЫZlgтVёIrHлкII'
     'TctHzШЖоМqмЫCЧяGтбсхBБЭёwkфVoKЙkщЮsУdЁэv'
     'меHЖЬTTXбJvЭCLDd', 'Поттер', '9853462924', '1GaimoriT1', '1GaimoriT1'),
    # Строка более 255 в поле имя
    ("""№;"?@%صسغذئآ龍門大酒秋瑞<IMG src="#">') # ; -- ☺☻♥♦♣♠•◘""", 'Поттер', '9853462924', '1GaimoriT1', '1GaimoriT1'),
    # Строка специальных символов в поле имя
    ('<script>alert("Поле input уязвимо!")</script>', 'Поттер', '9853462924', '1GaimoriT1', '1GaimoriT1'),
    # XSS инъекции (JS) в поле имя
    ('Эрнест', '', '9853462924', '1GaimoriT1', '1GaimoriT1'),  # Отсутсвие фамилии
    ('Эрнест', 'П', '9853462924', '1GaimoriT1', '1GaimoriT1'),  # Фамилия из одного символа (менее 2 символов)
    ('Эрнест', 'ЭрнесЭрнесЭрнесЭрнесЭрнесЭрнест', '9853462924', '1GaimoriT1', '1GaimoriT1'),
    # Фамилия из 31 (более чем 30 символов)
    ('Эрнест', 'ЗLСOFjpYШоWЭrмAЯKВmWBцMJцzGтшPqшnDЙDзФГг'
     'иМCeпСghGёcTЕЪYHяёдУжЩЙжМdиЛGbГQfшIUГjWл'
     'MnЯCЗлЫЬcuюSЯкrхJЖSfsjХЦXЛКIТЗъGLЯУdFХрО'
     'ЖШоИVвТvBtШvУАKЫюЛWOeЖzЮГзRnyТВжcЫзеQiEp'
     'oтwUVхвГaиABдиCУULйrюЖoгСзЫZlgтVёIrHлкII'
     'TctHzШЖоМqмЫCЧяGтбсхBБЭёwkфVoKЙkщЮsУdЁэv'
     'меHЖЬTTXбJvЭCLDd', '9853462924', '1GaimoriT1', '1GaimoriT1'),
    # Строка более 255 в поле фамилии
    ('Эрнест', """№;"?@%صسغذئآ龍門大酒秋瑞<IMG src="#">') # ; -- ☺☻♥♦♣♠•◘""", '9853462924', '1GaimoriT1', '1GaimoriT1'),
    # Строка специальных символов в поле фамилия
    ('Эрнест', '<script>alert("Поле input уязвимо!")</script>', '9853462924', '1GaimoriT1', '1GaimoriT1'),
    # XSS инъекции (JS) в поле фамилия
    ('Эрнест', 'Поттер', '9853462923', '', '1GaimoriT1'),  # Отсутсвие пароля
    (1, 1, 1, 1, 1),  # Числа в данных
    ('Эрнест', 'Поттер', '', '1GaimoriT1', '1GaimoriT1'),  # Отсутсвие номера телефона
    ('Эрнест', 'Поттер', '1', '1GaimoriT1', '1GaimoriT1'),  # одна цифра в номере телефона
    ('Эрнест', 'Поттер', '123456789', '1GaimoriT1', '1GaimoriT1'),  # 9 цифр в номере телефона
    ('Эрнест', 'Поттер', '12345678901', '1GaimoriT1', '1GaimoriT1'),  # 11 цифр в номере телефона
    ('Эрнест', 'Поттер', '0000000000', '1Gaimorit', '1GaimoriT1'),# Все нули в номере телефона
    ('Эрнест', 'Поттер', 'ЗLСOFjpYШоWЭrмAЯKВmWBцMJцzGтшPqшnDЙDзФГг'
     'иМCeпСghGёcTЕЪYHяёдУжЩЙжМdиЛGbГQfшIUГjWл'
     'MnЯCЗлЫЬcuюSЯкrхJЖSfsjХЦXЛКIТЗъGLЯУdFХрО'
     'ЖШоИVвТvBtШvУАKЫюЛWOeЖzЮГзRnyТВжcЫзеQiEp'
     'oтwUVхвГaиABдиCУULйrюЖoгСзЫZlgтVёIrHлкII'
     'TctHzШЖоМqмЫCЧяGтбсхBБЭёwkфVoKЙkщЮsУdЁэv'
     'меHЖЬTTXбJvЭCLDd', '1GaimoriT1', '1GaimoriT1'),  # Строка более 255 в номере телефона
    ('Эрнест', 'Поттер', '9853462924', 'ЗLСOFjpYШоWЭrмAЯKВmWBцMJцzGтшPqшnDЙDзФГг'
                   'иМCeпСghGёcTЕЪYHяёдУжЩЙжМdиЛGbГQfшIUГjWл'
                   'MnЯCЗлЫЬcuюSЯкrхJЖSfsjХЦXЛКIТЗъGLЯУdFХрО'
                   'ЖШоИVвТvBtШvУАKЫюЛWOeЖzЮГзRnyТВжcЫзеQiEp'
                   'oтwUVхвГaиABдиCУULйrюЖoгСзЫZlgтVёIrHлкII'
                   'TctHzШЖоМqмЫCЧяGтбсхBБЭёwkфVoKЙkщЮsУdЁэv'
                   'меHЖЬTTXбJvЭCLDd', '1GaimoriT1'),  # Строка более 255 символов в поле password
    ('Эрнест', 'Поттер', """№;"?@%صسغذئآ龍門大酒秋瑞<IMG src="#">') # ; -- ☺☻♥♦♣♠•◘""",
     '1GaimoriT1', '1GaimoriT1'),  # Строка специальных символов в номере телефона
    ('Эрнест','Поттер','9853462924', """№;"?@%صسغذئآ龍門大酒秋瑞<IMG src="#">') # ; -- ☺☻♥♦♣♠•◘""", '1GaimoriT1'),
    # Строка специальных символов в поле password
    ('Эрнест', 'Поттер', '<script>alert("Поле input уязвимо!")</script>',
     '1GaimoriT1', '1GaimoriT1'),
    # XSS инъекции (JS) в в номере телефона
    ('Эрнест', 'Поттер', '9853462924', '<script>alert("Поле input уязвимо!")</script>', '1GaimoriT1'),
    # XSS инъекции (JS) в поле password
    ('Эрнест', 'Поттер', '9853462924', '1GaimoriT1', ''),  # Отсутсвие подтверждения пароля
    ('Эрнест', 'Поттер', '9853462924', '1GaimoriT1', 'ЗLСOFjpYШоWЭrмAЯKВmWBцMJцzGтшPqшnDЙDзФГг'
     'иМCeпСghGёcTЕЪYHяёдУжЩЙжМdиЛGbГQfшIUГjWл'
     'MnЯCЗлЫЬcuюSЯкrхJЖSfsjХЦXЛКIТЗъGLЯУdFХрО'
     'ЖШоИVвТvBtШvУАKЫюЛWOeЖzЮГзRnyТВжcЫзеQiEp'
     'oтwUVхвГaиABдиCУULйrюЖoгСзЫZlgтVёIrHлкII'
     'TctHzШЖоМqмЫCЧяGтбсхBБЭёwkфVoKЙkщЮsУdЁэv'
     'меHЖЬTTXбJvЭCLDd'),
    # Строка более 255 символов в поле подтверждения пароля
    ('Эрнест', 'Поттер', '9853462924', '1GaimoriT1', """№;"?@%صسغذئآ龍門大酒秋瑞<IMG src="#">') # ; -- ☺☻♥♦♣♠•◘"""),
    # Строка специальных символов в поле подтверждения пароля
    ('Эрнест', 'Поттер', '9853462924', '1GaimoriT1', '<script>alert("Поле input уязвимо!")</script>'),
    # XSS инъекции (JS) в поле подтверждения пароля
    ('Эрнест', 'Поттер', '9853462924', '1GaimoriT1', '1gAIMORIt1'),  # Не совпадение паролей
    ('Эрнест', 'Поттер', '9853462924', '1', '1'),
    # Пароль из одного символа - цифры
    ('Эрнест', 'Поттер', '9853462924', '12345Gt', '12345Gt'),
    # Пароль из 7 симвоволов
    ('Эрнест', 'Поттер', '9853462924', 'i', '12345Gt'),
    # Пароль из 1 симвовола - буквы
    ('Эрнест', 'Поттер', '9853462924', 'Эрнест12345678', '12345Gt'),
    # Пароль на кирилице
    ('Эрнест', 'Поттер', '9853462924', 'ERNESTPOTTER', '12345Gt'),
    # Пароль только из заглавных букв
    ('Эрнест', 'Поттер', '9853462924', '1ERNESTPOTTER', '12345Gt'),
    # Пароль из 1 цифры и только заглавных букв
    ('Эрнест', 'Поттер', '9853462924', '1ernestpotter', '12345Gt'),
    # Пароль из 1 цифры и только прописных букв
    ('Эрнест', 'Поттер', '9853462924', '12121121212122', '12345Gt'),
    # Пароль только из цифр
    ('Эрнест', 'Поттер', '9853462924', '1I3t56789V123456789u1', '12345Gt'),
    # Пароль из 21 символа (более 20)
])
def test_negative_registrsation_phone(web_browser, name2, lastname2, phone2, password2, password21):
    pageA = AuthPage(web_browser)
    page = RegistPage(web_browser)

    pageA.btn_regist.click()
    # нажимаем кнопку зарегестрироваться, переходим на страницу регстрации

    url = page.get_current_url()
    # присваиваем переменной значение URL страницы регистрации


    # вводим исключения для прохождения тестов без перерыва при возникновении ошибки AttributeError
    try:
        page.name.send_keys(name2)
        # вводи имя

        page.lastname.send_keys(lastname2)

        # вводи фамилию


        page.phone.send_keys(phone2)
        # вводи телефон

        page.password.send_keys(password2)
        # вводи пароль

        page.password_confirm.send_keys(password21)
    #     подтверждение пароля


    except AttributeError:
        print('Введенные данные не соответсвуют формату поля ввода, ПО не дает ввести их')
        # выводим сообщение в консоль об ошибке что говорит о позитивном тесте
        pass
    page.btn.click()
    # нажимаем кнопку зарегестрироваться, переходим к форме подтверждени телефона

    assert page.get_current_url() == url
#     проверяем что не произошел переход на страницу к форме подтверждения телефона, URL соответсвует странице регистрации
