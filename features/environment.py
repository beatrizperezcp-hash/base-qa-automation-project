from selenium import webdriver
import os

def before_all(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()


def before_step(context, step):
    context.driver.save_screenshot(f"{os.getcwd()}/reports/{step.name}.png")