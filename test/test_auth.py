import allure


@allure.id("29999")
@allure.title("Auth via Google")
@allure.tag("web", "smoke")
@allure.story("External Auth")
@allure.feature("Auth")
@allure.label("msrv", "Auth")
@allure.label("owner", "allure8")
def test_google_auth():
    with allure.step("Открыть главную страницу"):
        pass
    with allure.step("Выбрать способ авторизации через Google"):
        pass
    with allure.step("Авторизоваться под основным пользователем `Mr. Random`"):
        pass
    with allure.step("Ввести логин `random-user@gmail.com`"):
        pass
    with allure.step("Ввести пароль `random-pass`"):
        pass
    with allure.step("Нажать на кнопку Войти"):
        pass
    with allure.step("Проверить, что авторизация успешна"):
        pass
    with allure.step("Проверить, что данные профиля обновились из Google"):
        pass
    with allure.step("Имя: `Mr. Random`"):
        pass
    with allure.step("Email: `random-user@gmail.com`"):
        pass
