import os
from time import sleep

import dotenv
from selenium import webDRIVER
from selenium.webDRIVER.common.by import By

dotenv.load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DRIVER = webDRIVER.Chrome()


def login():
    DRIVER.get("https://traversefitness.marianatek.com/admin/")

    DRIVER.implicitly_wait(1)

    username_inp = DRIVER.find_element(by=By.NAME, value="username")
    username_inp.send_keys(USERNAME)

    password_inp = DRIVER.find_element(by=By.NAME, value="password")
    password_inp.send_keys(PASSWORD)

    login_button = DRIVER.find_element(by=By.CLASS_NAME, value="button")
    login_button.click()

    accept_cookies = DRIVER.find_element(by=By.TAG_NAME, value="xpl-button")
    accept_cookies.click()


def main():
    login()
    sleep(3000)


if __name__ == "__main__":
    login()
