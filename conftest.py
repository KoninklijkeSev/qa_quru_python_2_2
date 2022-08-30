import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session", autouse=True)
def browser_config():
    """Настройка разрешения окна браузера"""
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    # browser.driver.maximize_window()
    yield
