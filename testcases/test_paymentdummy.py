from pageobjects.dummyticketpayment import Payment


class Test_Payment:
    url = ''
    card_number = '5111010030175156'


    


    def test_payment_ticket(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.py = Payment(self.driver)
        self.py.card_payment_select()
        for i in range(0, len(self.card_number), 4):
            chunk = self.card_number[i:i + 4]
            self.py.card_number_enter(chunk)
        self.py.card_exp_enter('05/27')
        self.py.cvv_enter('456')
        self.py.card_owner_name_enter('vishal panchal')
        self.py.click_proceed()

