from selenium.webdriver.common.by import By


class Payment:
    card_option_xpath = (By.XPATH, '//ul[@class="pymtns-type-accordian"]//li[2]/span[2]')
    card_num_input_ID = (By.ID, 'cardNumber')
    card_exp_inp_id = (By.ID, 'cardExpiry')
    card_cvv_inp_id = (By.ID, 'cardCvv')
    card_owner_inp_id = (By.ID, 'cardOwnerName')
    proceed_btn_xpath = "//span[contains(text(),'PROCEED')]"
    verify_xpath = (By.XPATH, '//h3')

    def __init__(self, driver):
        self.driver = driver

    def card_payment_select(self):
        self.driver.find_element(*Payment.card_option_xpath).click()

    def card_number_enter(self, card_number):
        self.driver.find_element(*Payment.card_num_input_ID).send_keys(card_number)

    def card_exp_enter(self, exp_date):
        self.driver.find_element(*Payment.card_exp_inp_id).send_keys(exp_date)

    def cvv_enter(self, cvv):
        self.driver.find_element(*Payment.card_cvv_inp_id).send_keys(cvv)

    def card_owner_name_enter(self, card_owner_name):
        self.driver.find_element(*Payment.card_owner_inp_id).send_keys(card_owner_name)

    def click_proceed(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'PROCEED')]").click()
