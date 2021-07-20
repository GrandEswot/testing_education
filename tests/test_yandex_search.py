from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


def test_yandex_search():
    driver = WebDriver(executable_path='/home/eswot/PycharmProjects/testing_from_youtube/'
                                       'Web UI автоматизация на Selenium: с нуля до первого теста (Python)'
                                       '/chromedriver')
    driver.get('https://ya.ru')
    search_input = driver.find_element_by_xpath('//input[@id="text"]')
    button_submit = driver.find_element_by_xpath('//button[@type="submit"]')
    search_input.send_keys('market.yandex.ru')
    button_submit.click()

    def check_result_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        print(type(inner_search_results))
        return len(inner_search_results) >= 5

    WebDriverWait(driver, 5, 0.5).until(check_result_count, 'Кол-во результатов поиска меньше 5')

    search_result = driver.find_elements_by_xpath('//li[@class="serp-item"]')
    link = search_result[0].find_element_by_xpath('.//h2/a')
    link.click()

    driver.switch_to.window(driver.window_handles[1])

    assert driver.title == 'Яндекс.Маркет — покупки с быстрой доставкой'