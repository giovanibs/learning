"""
this file will define the methods that will take the actions that we need done
"""

from selenium import webdriver
import os
import booking.constants as const
import time

# we want the Booking class to inherit the Chrome class
class Booking(webdriver.Chrome):
    
    # the __init__ method will run at the moment we create an instance of the booking class. AKA "CONSTRUCTOR"
    # the terardown argument will be used in the __exit__ magic method
    def __init__(self, driver_path=r'C:\SeleniumDrivers', teardown = True):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += os.pathsep + self.driver_path

        # why use the super() method? --> we want to instantiate the inherited class (webdriver.Chrome)
        # __init__ wil create the instance
        # after that, we have full access to the webdriver.Chrome's methods
        super(Booking, self).__init__()

        # wait for some ammount of time before until the element is ready at the website
        # proceeds before that time if the element is ready
        self.implicitly_wait(15)

        self.maximize_window()

    # this method will be called as soon as the context manager is finished running its main lines of code
    def __exit__(self, *args) -> None:
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency = 'USD'):
        currency_element = self.find_element_by_css_selector(
                                'button[data-tooltip-text="Escolha sua moeda"]'
                            )
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(
            # "*=" looks for a substring
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()
    
    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        #results_ul = self.find_element_by_css_selector('ul[class*=c-autocomplete__list sb-autocomplete__list')
        #first_result = results_ul.find_element_by_css_selector('li[data-i="0"]')
        first_result =self.find_element_by_css_selector(
            'li[data-i="0"]'
            )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        # to go to next calendar page: <div class="bui-calendar__control bui-calendar__control--next" data-bui-ref="calendar-next">
        check_in_elem = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
            )
        check_in_elem.click()
        check_out_elem = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
            )
        check_out_elem.click()

    def select_adults(self, count=1):
        selection_elem = self.find_element_by_id('xp__guests__toggle')
        selection_elem.click()

        adults_field =  self.find_element_by_css_selector('div[class*="sb-group__field-adults"]')
        add_button = adults_field.find_element_by_css_selector('button[data-bui-ref="input-stepper-add-button"]') 
        subtract_button = adults_field.find_element_by_css_selector('button[data-bui-ref="input-stepper-subtract-button"]')
        adults = int(self.find_element_by_id('group_adults').get_attribute('value'))
        
        while count != adults:
            print(f'Adultos: {adults}')
            if count < adults:
                subtract_button.click()
            elif count > adults:
                add_button.click()
            adults = int(self.find_element_by_id('group_adults').get_attribute('value'))

    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[class*="sb-searchbox__button"]'
        )
        search_button.click()
        
