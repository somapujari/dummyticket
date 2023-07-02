import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookTicket:
    buy_ticket_button_xpath = "//*[contains(text(),'BUY TICKET')]"
    radio_button_select_id = 'product_549'
    first_name_id = 'travname'
    last_name_id ='travlastname'
    date_id = 'dob'
    month_xpath = '//select[@class="ui-datepicker-month"]/option'
    year_xpath ='//select[@class="ui-datepicker-year"]/option'
    # table_rows_xpath = '//table[@class="ui-datepicker-calendar"]//tr'
    # table_cols_xpath = '//table[@class="ui-datepicker-calendar"]//tr[1]/td'
    table_date_xpath = '//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a'
    gender_male_id = 'sex_1'
    gender_female_id = 'sex_2'
    one_way_redio_id = 'traveltype_1'
    round_trip_id = 'traveltype_2'
    multi_city_radio_id = 'traveltype_3'
    fromcity_input_id = 'fromcity'
    to_city_id = 'tocity'
    phone_input_id = 'billing_phone'
    email_input_id = 'billing_email'
    country_input_id = 'select2-billing_country-container'
    country_drop_xpath = "//ul[@id='select2-billing_country-results']/li"
    street_xpath_input = '//span[@class="woocommerce-input-wrapper"]//input[@name="billing_address_1"]'
    city_input_xpath = "//input[@id='billing_city']"
    state_click_id = 'select2-billing_state-container'
    state_drop_Xpath = '//ul[@id="select2-billing_state-results"]/li'
    pincode_input_id= 'billing_postcode'
    place_order_button_xpath = "//button[@id='place_order']"
    departure_city_input_ID = 'departon'
    only_countries_Xpath = "//ul[@id='select2-billing_country-results']/li[contains(text(),'India')][2]"
    upi_text_xpath = '//ul[@class="pymtns-type-accordian"]//li/span[2]'
    phonepe_text_xpath = "//span[contains(text(),'PhonePe')]"
    phonenumber_input_id = 'upi2Id'
    verify_button_id = 'upi-verify-enabled'
    proceed_button_xpath= "//span[contains(text(),'PROCEED')]"
    card_option_xpath = '//ul[@class="pymtns-type-accordian"]//li[2]/span[2]'
    



    def __init__(self,driver):
        self.driver = driver

    def buy_ticket(self):
        self.driver.find_element(By.XPATH,self.buy_ticket_button_xpath).click()

    def ticket_for_visa(self):
        self.driver.find_element(By.ID, self.radio_button_select_id).click()

    def first_name_enter(self,first_name):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name)

    def last_name_enter(self,last_name):
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name)

    def date_textbox_click(self):
        self.driver.find_element(By.ID,self.date_id).click()

    def month_select(self,month):
        mon = self.driver.find_elements(By.XPATH, self.month_xpath)
        for mont in mon:
            if mont.text == month:
                mont.click()
                break

    def year_select(self, year):
        years = self.driver.find_elements(By.XPATH, self.year_xpath)
        for yea in years:
            if yea.text == year:
                yea.click()
                break

    def date_select(self, date):
        # rows = len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))
        # cols = len(self.driver.find_elements(By.XPATH, self.table_cols_xpath))
        # for r in range(1,rows+1):
        #     for c in range(1,cols+1):
        dat = self.driver.find_elements(By.XPATH, self.table_date_xpath)
        for da in dat:
            if da.text == date:
                da.click()
                break

    def gender_select(self, gender):
        male = self.driver.find_element(By.ID, self.gender_male_id)
        female = self.driver.find_element(By.ID, self.gender_female_id)
        if gender == 'male':
            male.click()
        else:
            female.click()

    def trip_select(self, trip_type):
        one_way = self.driver.find_element(By.ID, self.one_way_redio_id)
        round_trip = self.driver.find_element(By.ID, self.round_trip_id)
        multi_city = self.driver.find_element(By.ID, self.multi_city_radio_id)
        if trip_type == 'one_way':
            one_way.click()
        elif trip_type == 'round_trip':
            round_trip.click()
        elif trip_type == 'multi_city':
            multi_city.click()
        else:
            one_way.click()

    def fromcity_enter(self, start):
        self.driver.find_element(By.ID, self.fromcity_input_id).send_keys(start)

    def to_city_enter(self, end):
        self.driver.find_element(By.ID, self.to_city_id).send_keys(end)

    def departure_date_click(self):
        self.driver.find_element(By.ID, self.departure_city_input_ID).click()

    def dep_month_select(self, deptr_month):
        mon = self.driver.find_elements(By.XPATH, self.month_xpath)
        for mont in mon:
            if mont.text == deptr_month:
                mont.click()
                break

    def dep_year_select(self, deptr_year):
        years = self.driver.find_elements(By.XPATH, self.year_xpath)
        for yea in years:
            if yea.text == deptr_year:
                yea.click()
                break

    def dep_date_select(self, deptr_date):
        # rows = len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))
        # cols = len(self.driver.find_elements(By.XPATH, self.table_cols_xpath))
        # for r in range(1,rows+1):
        #     for c in range(1,cols+1):
        dat = self.driver.find_elements(By.XPATH, self.table_date_xpath)
        for da in dat:
            if da.text == deptr_date:
                da.click()
                break

    def phone_enter(self, phone):
        self.driver.find_element(By.ID,self.phone_input_id).send_keys(phone)

    def email_enter(self, email):
        self.driver.find_element(By.ID, self.email_input_id).send_keys(email)

    def country_select(self, country):
        self.driver.find_element(By.ID, self.country_input_id).click()
        countries = self.driver.find_elements(By.ID, self.country_drop_xpath)
        for cou in countries:
            if cou.text == country:
                cou.click()
                break

    def only_country_select(self):
        self.driver.find_element(By.ID, self.country_input_id).click()
        self.driver.find_element(By.XPATH, self.only_countries_Xpath).click()

    def street_address_ent(self, address):
        self.driver.find_element(By.XPATH, self.street_xpath_input).send_keys(address)

    def city_input_enter(self, city):
        self.driver.find_element(By.XPATH, self.city_input_xpath).send_keys(city)

    def state_select(self, state):
        self.driver.find_element(By.ID, self.state_click_id).click()
        states = self.driver.find_elements(By.XPATH, self.state_drop_Xpath)
        for stat in states:
            if stat.text == state:
                stat.click()
                break

    def postal_code_enter(self, pincode):
        self.driver.find_element(By.ID, self.pincode_input_id).send_keys(pincode)

    def place_order(self):
        # wait = WebDriverWait(self.driver, 10)
        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'place_order')))
        ele = self.driver.find_element(By.XPATH, self.place_order_button_xpath)
        self.driver.execute_script('arguments[0].click()', ele)

    def click_on_upi(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="pymtns-type-accordian"]//li/span[2]')))
        self.driver.find_element(By.XPATH, self.upi_text_xpath).click()

    def click_on_phonepe(self):
        self.driver.find_element(By.XPATH, self.phonepe_text_xpath).click()

    def phonepe_number_enter(self, phonepe_number):
        self.driver.find_element(By.ID, self.phonenumber_input_id).send_keys(phonepe_number)

    def verify_click(self):
        self.driver.find_element(By.ID, self.verify_button_id).click()

    def proceed_click(self):
        self.driver.find_element(By.XPATH, self.proceed_button_xpath).click()