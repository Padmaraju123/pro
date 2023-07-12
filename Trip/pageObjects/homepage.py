from selenium.webdriver.common.by import By

from pageObjects.secondpage import SecondPage


class HomePage:

    usr = (By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")
    psd = (By.XPATH, "//input[@placeholder='Enter your password']")
    hide_psd = (By.TAG_NAME, "small")
    butt1 = (By.XPATH, "//button[@type='submit']")
    scroll1 = ("window.scrollBy(0,50)","")
    scroll2 = ("window.scrollBy(50,100)", "")
    scroll3 = ("window.scrollBy(100,150)", "")
    scroll4 = ("window.scrollBy(150,200)", "")
    scroll5 = ("window.scrollBy(200,250)", "")
    scroll6 = ("window.scrollBy(250,300)", "")
    scroll7 = ("window.scrollBy(300,350)", "")
    scroll8 = ("window.scrollBy(350,400)", "")
    scroll9 = ("window.scrollBy(400,document.body.scrollHeight)", "")
    scroll_up = ("window.scrollTo(0, 0)", "")
    search1 = (By.XPATH, "//span[@class='nI-gNb-sb__placeholder']")

    designation = (By.XPATH, "//input[@placeholder='Enter keyword / designation / companies']")
    list_design = (By.XPATH, "//b[@class='pre-wrap']")

    experience = (By.XPATH, "//span[@class='ni-gnb-icn ni-gnb-icn-expand-more']")
    list_exp = (By.XPATH, "//li[@class=' ']/div/span")

    location = (By.CSS_SELECTOR,"input[placeholder='Enter location']")
    list_locations = (By.XPATH,"//b[@class='pre-wrap']")
    search2 = (By.XPATH,"//span[@class='ni-gnb-icn ni-gnb-icn-search']")

    def __init__(self, driver):
        self.driver = driver

    def meth_user(self):
        return self.driver.find_element(*HomePage.usr)

    def meth_pass(self):
        return self.driver.find_element(*HomePage.psd)

    def meth_hide(self):
        return self.driver.find_element(*HomePage.hide_psd)

    def meth_butt1(self):
        return self.driver.find_element(*HomePage.butt1)

    def meth_scroll1(self):
        return self.driver.execute_script(*HomePage.scroll1)

    def meth_scroll2(self):
        return self.driver.execute_script(*HomePage.scroll2)

    def meth_scroll3(self):
        return self.driver.execute_script(*HomePage.scroll3)

    def meth_scroll4(self):
        return self.driver.execute_script(*HomePage.scroll4)

    def meth_scroll5(self):
        return self.driver.execute_script(*HomePage.scroll5)

    def meth_scroll6(self):
        return self.driver.execute_script(*HomePage.scroll6)

    def meth_scroll7(self):
        return self.driver.execute_script(*HomePage.scroll7)

    def meth_scroll8(self):
        return self.driver.execute_script(*HomePage.scroll8)

    def meth_scroll9(self):
        return self.driver.execute_script(*HomePage.scroll9)

    def meth_scroll_up(self):
        return self.driver.execute_script(*HomePage.scroll_up)

    def meth_search1(self):
        return self.driver.find_element(*HomePage.search1)

    def meth_design(self):
        return self.driver.find_element(*HomePage.designation)

    def meth_list_design(self):
        return self.driver.find_elements(*HomePage.list_design)

    def meth_exp(self):
        return self.driver.find_element(*HomePage.experience)

    def meth_list_exp(self):
        return self.driver.find_elements(*HomePage.list_exp)

    def meth_location(self):
        return self.driver.find_element(*HomePage.location)

    def meth_list_locations(self):
        return self.driver.find_elements(*HomePage.list_locations)

    def meth_search2(self):
        self.driver.find_element(*HomePage.search2).click()
        second_obj = SecondPage(self.driver)
        return second_obj

