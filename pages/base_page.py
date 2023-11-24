class BasePage:
    def __init__(self,
                 driver):  # init is used to initialize a class, self represents instance of class, driver will control our browser
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()
        self.driver.find_element(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()

        self.find(*locator).send_keys(value)


    def get_title(self):
      return
