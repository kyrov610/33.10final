QAP_results
В данном репозитории представлены автотесты с позитивными и негативными сценариями для формы авторизации и

регистрации Ростелеком

Необходимо установить на в виртуальном окружении интерпритатора Python - pytest, pytest-selenium, selenium 4.9.0.,

драйвер браузера Chrome.

Автотесты запускаются комндой в терминале

pytest -v -s --driver Chrome --driver-path /путь к chromedriver.exe путь к автотестам

При составлении тестов использовались техники эквивалентного разбиения и граничных значений, и предугадывания ошибок.

Использовались интрументы DevTools браузера Chrome, и его расширения Еlement Locator, Xpath Helper для определяения

локаторов Selenium.