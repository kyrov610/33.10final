from Pages.base import WebPage
from Pages.elements import WebElement

name2 = 'Эрнест'
lastname2 = 'Поттер'
email2 = 'fuagra@inbox.ru'
password2 = '1GaimoriT1'
phone2 = '9853462924'




class RegistPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redire' \
              'ct_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=6870d174-45' \
              '3f-41dd-ae5c-ea8ae56e50f5&theme&auth_type'
        # адресс основной страницы авторизаци - система не дает прямой переход на страницу регистрации
        super().__init__(web_driver, url)

    name = WebElement(name='firstName')
    # Локатор для поля ввода имя

    lastname = WebElement(name='lastName')
    # Локатор для поля ввода фамилии


    phone = WebElement(id="address")
    # Локатор для поля ввода телефона/электронной почты

    email = WebElement(id="address")
    # Локатор для поля ввода телефона/электронной почты

    password = WebElement(id="password")
    # Локатор для поля ввода пароля

    password_confirm = WebElement(id="password-confirm")
    # Локатор для поля ввода подтверждения пароля

    btn = WebElement(name="register")
    # Локатор для кнопки "Зарегистрироваться"


    element_confirm_code = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]')
    # Локатор для поля ввода потверждения пароля со страницы подтверждения пароля, поскольку нужн данный код то дальнейшая
    # проверка не соуществлялась

    element_restore_password =WebElement(id="reg-err-reset-pass")
    # Локатор для кнопки "Восстановить" пароль из всплывающего окна с сообщением об уже существующей учетной записи -
    # выбрана так как именно она имеет уникальный атрибут на странице id
