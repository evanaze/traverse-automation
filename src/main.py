import datetime as dt
import os
from time import sleep

import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

from src import dte_mapping

dotenv.load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DRIVER = webdriver.Chrome()
DTEMAP = dte_mapping.create_dtemap()
print(DTEMAP)


def login():
    DRIVER.get("https://traversefitness.marianatek.com/admin/")

    DRIVER.implicitly_wait(1)

    username_inp = DRIVER.find_element(by=By.NAME, value="username")
    username_inp.send_keys(USERNAME)

    password_inp = DRIVER.find_element(by=By.NAME, value="password")
    password_inp.send_keys(PASSWORD)

    login_button = DRIVER.find_element(by=By.CLASS_NAME, value="button")
    login_button.click()
    DRIVER.implicitly_wait(1)
    sleep(2)

    accept_cookies = DRIVER.find_element(
        by=By.XPATH, value="/html/body/div[5]/div/footer/xpl-button/button"
    )
    accept_cookies.click()
    DRIVER.implicitly_wait(1)
    sleep(2)


def logout():
    logout_button = DRIVER.find_element(
        by=By.XPATH,
        value="/html/body/xpl-application-shell/div[1]/xpl-main-nav/nav/footer/ul/xpl-nav-item[3]",
    )
    logout_button.click()
    DRIVER.implicitly_wait(1)
    sleep(2)


def nav_sched_today():
    # Select schedule and list view and today. Return today's date
    schedule_tab = DRIVER.find_element(
        by=By.XPATH,
        value="/html/body/xpl-application-shell/div[1]/xpl-main-nav/nav/div/div/xpl-nav-item[3]",
    )
    schedule_tab.click()
    DRIVER.implicitly_wait(1)
    sleep(2)

    list_view = DRIVER.find_element(
        by=By.XPATH,
        value="/html/body/xpl-application-shell/div[4]/xpl-content-area/main/div/div/div/section/div[1]/div[2]/label[1]",
    )
    list_view.click()
    DRIVER.implicitly_wait(1)
    sleep(1)

    today_btn = DRIVER.find_element(
        by=By.XPATH,
        value="/html/body/xpl-application-shell/div[4]/xpl-content-area/main/div/div/div/section/div[1]/div[1]/div/xpl-button[1]",
    )
    today_btn.click()
    DRIVER.implicitly_wait(1)
    sleep(1)


def sched_date() -> dt.date:
    sched_date = DRIVER.find_element(
        by=By.XPATH,
        value="/html/body/xpl-application-shell/div[4]/xpl-content-area/main/div/div/div/section/div[1]/div[1]/div/button",
    )
    unparsed_date = sched_date.text
    parsed_date = dte_mapping.parse_date(unparsed_date)
    return parsed_date


def get_program(dte: dt.date) -> str:
    pair = DTEMAP[dte]
    return " - ".join(pair)


def set_schedule(program: str):
    print(program)


def nav_tomorrow():
    pass


def main():
    login()
    nav_sched_today()
    today = sched_date()
    program = get_program(today)
    set_schedule(program)
    logout()
    DRIVER.close()


if __name__ == "__main__":
    main()
