import time
from utility.loggenerate import LogGen
from selenium.webdriver.common.by import By

from pageobjects.dummyticket_book import BookTicket
from pageobjects.dummyticketpayment import Payment


class Test_BuyTicket:
    baseurl = 'https://www.dummyticket.com/'
    first_name = 'vishal'
    last_name = 'panchal'
    month = 'May'
    year = '1990'
    date = '12'
    gender = 'male'
    trip_type = 'one_way'
    start = 'pune'
    end = 'delhi'
    deptr_month = 'may'
    deptr_year = '2023'
    deptr_date = '10'
    phone = 8805633666
    email = 'somapujari0@gmail.com'
    country = 'Hungary'
    address = '108,bijapur Road'
    city = 'Pune 416414'
    state = 'Maharashtra'
    pincode = '406404'
    phonepe_number = '8888063221@ybl'
    upiid = '9999999999@barodampay'  # '9999999999@allbank'
    card_number = '5111010030175156'
    logger = LogGen.loggen()

    def test_ticket(self, setup):
        self.logger.info('test_ticket started ')
        self.driver = setup
        self.logger.info('opening url')
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(20)
        self.driver.delete_all_cookies()
        self.b = BookTicket(self.driver)
        self.logger.info('clicking on buy ticket button')
        self.b.buy_ticket()
        self.b.ticket_for_visa()
        self.logger.info('enter first_name')
        self.b.first_name_enter(self.first_name)
        self.logger.info('enter last_name')
        self.b.last_name_enter(self.last_name)
        self.b.date_textbox_click()
        self.logger.info('month selecting')
        self.b.month_select(self.month)
        self.logger.info('year selecting')
        self.b.year_select(self.year)
        self.logger.info('date selecting')
        self.b.date_select(self.date)
        self.logger.info('gender selecting ')
        self.b.gender_select(self.gender)
        self.logger.info('trip type selecting')
        self.b.trip_select(self.trip_type)
        self.logger.info('entering from city ')
        self.b.fromcity_enter(self.start)
        self.logger.info('entering to city ')
        self.b.to_city_enter(self.end)
        self.logger.info('entering dept date')
        self.b.departure_date_click()
        self.b.dep_month_select(self.deptr_month)
        self.b.dep_year_select(self.deptr_year)
        self.b.dep_date_select(self.deptr_date)
        self.logger.info('entering  phone number ')
        self.b.phone_enter(self.phone)
        self.logger.info('entering emaile')
        self.b.email_enter(self.email)
        # self.b.country_select(self.country)
        self.logger.info('country selecting')
        self.b.only_country_select()
        self.logger.info('entering address')
        self.b.street_address_ent(self.address)
        self.logger.info('entering city')
        self.b.city_input_enter(self.city)
        self.logger.info('selecting state')
        self.b.state_select(self.state)
        self.logger.info('entering pincode')
        self.b.postal_code_enter(self.pincode)
        self.logger.info('placing order')
        self.b.place_order()
        self.logger.info('opening payment page')
        self.py = Payment(self.driver)
        self.logger.info('entering card number')
        self.py.card_payment_select()
        for i in range(0, len(self.card_number), 4):
            chunk = self.card_number[i:i + 4]
            self.py.card_number_enter(chunk)
        self.logger.info('entering card expire date')
        self.py.card_exp_enter('0527')
        self.logger.info('entering cvv ')
        self.py.cvv_enter('456')
        self.logger.info('entering card owner name ')
        self.py.card_owner_name_enter('vishal panchal')
        self.logger.info('clicking on  proceed button ')
        self.py.click_proceed()
        self.logger.info('clicking on dont save card details button')
        try:
            self.driver.find_element(By.XPATH, '//div[@class="consent-modal-buttons"]').click()
        except Exception as e:
            print(e)
        time.sleep(2)
        self.logger.info('verifying test ')
        if self.driver.title == 'Thank You 6 - Dummy ticket':
            assert True
            self.logger.info('test is passed')
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\dummyticket\screenshots\ticketpass.png')
        else:
            self.logger.info('test failed')
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\dummyticket\screenshots\ticketfail.png')
            assert False
        self.logger.info('test_ticket  completed')
