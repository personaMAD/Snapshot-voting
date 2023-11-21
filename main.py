# Подключить к chromedriver расширение MetaMask
# Загрузить любой кошелек в метамаск
# Добавить в расширение метамаск любую сеть через chainlist

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
from config import seed, passwd, chainid, currency, rpc, network

#Пишем путь до crx файла метамаска (с scuttleGlobalThis = false)
EXTENSION_PATH = ''

def scroll(driver, px_down=180):
    ActionChains(driver) \
        .scroll_by_amount(0, px_down) \
        .perform()


def snapshot_vote(pk):
    try:
        options = Options()
        # options.add_argument('--headless=new')
        options.add_extension(EXTENSION_PATH)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)

        time.sleep(5)
        mm_ext_handle = driver.window_handles[1]
        general_handle = driver.window_handles[0]

        driver.switch_to.window(mm_ext_handle)

        driver.find_element(by=By.XPATH, value='//*[@id="onboarding__terms-checkbox"]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[3]/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div/button[2]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="import-srp__srp-word-0"]').click()

        driver.execute_script(f"navigator.clipboard.writeText('{seed}');")
        driver.find_element(by=By.XPATH, value='//*[@id="import-srp__srp-word-0"]').send_keys(Keys.CONTROL, 'v')
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button'))).click()

        # driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(passwd)
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(passwd)

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input'))).click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button'))).click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'))).click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'))).click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'))).click()


        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="popover-content"]/div/div/section/div[1]/div/button/span'))).click()
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/button/span/div/div/span[1]').click()
        driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[3]/div/section/div[3]/button').click()
        driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[3]/div/section/div[2]/div[2]/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="private-key-box"]').send_keys(pk)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[3]/div[3]/div/section/div[2]/div/div[2]/button[2]'))).click()
        time.sleep(1)
        #### добавляем сеть руками в ММ
        def switch_network():
            # переходим во вкладку сети
            driver.get('chrome-extension://gpelijmmdobcpllnkbcibpkahbkfjlpm/home.html#settings/networks')

            driver.find_element(by=By.XPATH,
                                value='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/button').click()
            driver.find_element(by=By.XPATH,
                                value='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[3]/a/h6').click()
            # добавляем 4 параметров сети
            driver.find_element(by=By.XPATH,
                                value='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input').send_keys(
                network)
            driver.find_element(by=By.XPATH,
                                value='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input').send_keys(
                rpc)
            driver.find_element(by=By.XPATH,
                                value='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input').send_keys(
                chainid)
            driver.find_element(by=By.XPATH,
                                value='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input').send_keys(
                currency)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]'))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="popover-content"]/div/div/section/div[2]/div/button[1]/h6'))).click()
        switch_network()





        time.sleep(1)



         #####
        # #добавляем сеть
        # chain_url = 'https://chainlist.org/chain/1088'
        # driver.get(chain_url)
        # # time.sleep(10)
        # scroll(driver, 300)
        #
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, '//*[@id="__next"]/div/div[2]/div[3]/table/tbody/tr[1]/td[6]/button'))).click()
        #
        # # driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/table/tbody/tr[1]/td[6]/button').click()
        # time.sleep(1)
        #
        # driver.switch_to.window(driver.window_handles[-1])
        #
        # # time.sleep(999)
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, '//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]'))).click()
        #
        # driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]').click()
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, '//*[@id="app-content"]/div/div/div/div[2]/div[3]/button[2]'))).click()
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, '//*[@id="app-content"]/div/div/div/div[2]/div/button[2]'))).click()
        # time.sleep(2)


        #переходим
        driver.switch_to.window(general_handle)
        snap_url = 'https://snapshot.org/#/stgdao.eth/proposal/0x6c9437b45e8a88978bca68238048fca8c670ed356fa7d4ae9ab9e7e93788c538'
        driver.get(snap_url)
        # time.sleep(2)

        #коннектим метамаск
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="navbar"]/div/div/div/div[2]/button/span'))).click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal"]/div/div[2]/div[2]/div/div/div[1]/button'))).click()
        # print(driver.window_handles)
        # print(driver.current_window_handle)
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        # print(driver.window_handles)
        # print

        #ждем 5 сек чтобы точно сеть в ММ успела переключиться
        # time.sleep(5)

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]'))).click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]'))).click()
        time.sleep(3)
        driver.switch_to.window(general_handle)

        #голосуем
        choose = random.choice([1, 2, 3])
        # print(choose)
        driver.find_element(by=By.XPATH, value=f'//*[@id="content-left"]/div[3]/div[1]/div[2]/div/div/button[{choose}]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="content-left"]/div[3]/div[1]/div[2]/button').click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal"]/div/div[2]/div[2]/div[2]/button'))).click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-content"]/div/div/div/div[4]/div[1]/i'))).click()
        driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div/div/div[5]/footer/button[2]').click()
        driver.switch_to.window(general_handle)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal"]/div/div[2]/div[2]/div/button[4]'))).click()
        time.sleep(3)
    except Exception as err:
        with open('./error_wallets.txt', 'a') as file:
            file.write(pk)
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver.get_screenshot_as_file('./error.png')
        print(err)
    finally:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.close()
        driver.quit()

i = 1
with open('./wals.txt', 'r') as f:
    for string in f:
        snapshot_vote(string.strip())
        print(f'кошелек {i} успешно проголосовал')
        i += 1
