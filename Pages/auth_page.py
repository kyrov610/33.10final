from Pages.base import WebPage
from Pages.elements import WebElement

user_info = 'Фуагра Анри'
# фамилия и имя зарегистрированого пользователя
# ниже его почта, пароль и телефон
email1 = 'afuagra@inbox.ru'
password1 = '12Gaimorit21'
phone1 = '1234567890'




class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redire' \
              'ct_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=6870d174-45' \
              '3f-41dd-ae5c-ea8ae56e50f5&theme&auth_type'
        # адресс основной страницы авторизации
        super().__init__(web_driver, url)

    btn_email = WebElement(id="t-btn-tab-mail")
    #локатор для выбора кнопки "почта"
    btn_phone = WebElement(id="t-btn-tab-phone")
    # локатор для выбора кнопки "телфон"
    phone = WebElement(id="username")
    #локатор для выбора поля телфон/электронный адресс
    email = WebElement(id="username")
    # локатор для выбора поля телфон/электронный адресс
    password = WebElement(id="password")
    # локатор для выбора поля пароль
    btn = WebElement(id="kc-login")
    # локатор для выбора кнопки "Войти"
    element_user_info = WebElement(xpath='//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2')
    # локатор для информации об имени и фамилии пользователя на странице личных данных

    element_forgot_pas = WebElement(xpath='//*[@id="forgot_password"]')
    # локатор для выбора кнопки "Забыл пароль"

    element_wrong_email = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')

    # локатор для появившегося сообщения о неправильно введеной почте

    element_wrong_phone = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')

    # локатор для появившегося сообщения о неправильно введеной почте

    btn_regist = WebElement(id="kc-register")

    # локатор для кнопки "зарегистрироваться"
