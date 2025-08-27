import time

from helper.Page_Objects.Main_functions_poo import Main_functions_poo as main_functions
from behave import given, when, then

@given("Navigate to the website {url}")
def open_url(context, url):
    mf = main_functions(context.driver)
    mf.open_url(url)


@then("Click on the following button {button_name}")
def click_on_button(context, button_name = 'Create an Account'):
    mf = main_functions(context.driver)
    mf.click_on_button(button_name)


@then("Click on the following submit button {button_name}")
def click_on_submit_button(context, button_name = 'Create an Account'):
    mf = main_functions(context.driver)
    mf.click_on_button_submit(button_name)

@then("Fill the following fields")
def fill_the_form(context):
   mf = main_functions(context.driver)
   for i in context.table:
     mf.fill_form(i['field_name'], i['value'])

