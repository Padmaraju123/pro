from selenium.webdriver.common.by import By


class SecondPage:
    work_f_home = (By.XPATH, "(//i[@class='fleft naukicon naukicon-checkbox'])[1]")
    remote = (By.XPATH, "(//i[@class='fleft naukicon naukicon-checkbox'])[3]")

    view_more = (By.LINK_TEXT, "View More")
    depart_input = (By.XPATH, "//input[@class='search-input']")
    depart_name = (By.XPATH, "(//div[@class='swiper-slide swiper-slide-active']/div/label/i)[1]")
    depart_button = (By.XPATH, "//div[@class='filter-apply-btn ']")

    salary_view = (By.XPATH, "(//span[@class='fleft'])[2]")
    salary_choice = (By.XPATH, "(//div[@class='swiper-slide swiper-slide-active']"
                               "/div[@class='chckBoxCont mt-8']/label[@class='chkLbl']/i)[2]")
    salary_button = (By.XPATH, "//div[@class='filter-apply-btn ']")

    company_choice = (By.XPATH, "((//div[@class='filterOptns'])[5]/div[@class='chckBoxCont mt-8'])[1]")

    role_cate = (By.XPATH, "(//div[@data-filter-id='glbl_RoleCat']/div)[1]")

    education_view = (By.XPATH, "(//span[@class='fleft'])[2]")
    education_option = (By.XPATH, "(//div[@class='swiper-slide swiper-slide-active']/div)[5]")
    education_button = (By.XPATH, "//div[@class='filter-apply-btn ']")

    logout_option = (By.XPATH, "//div[@class='nI-gNb-drawer__bars']")
    logout_button = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def meth_work_f_home(self):
        return self.driver.find_element(*SecondPage.work_f_home)

    def meth_remote(self):
        return self.driver.find_element(*SecondPage.remote)

    def meth_view(self):
        return self.driver.find_element(*SecondPage.view_more)

    def meth_depart_input(self):
        return self.driver.find_element(*SecondPage.depart_input)

    def meth_depart_name(self):
        return self.driver.find_element(*SecondPage.depart_name)

    def meth_depart_button(self):
        return self.driver.find_element(*SecondPage.depart_button)

    # salary methods
    def meth_salary_view(self):
        return self.driver.find_element(*SecondPage.salary_view)

    def meth_salary_option(self):
        return self.driver.find_element(*SecondPage.salary_choice)

    def meth_salary_button(self):
        return self.driver.find_element(*SecondPage.salary_button)

    def meth_company_choice(self):
        return self.driver.find_element(*SecondPage.company_choice)

    def meth_role_cate(self):
        return self.driver.find_element(*SecondPage.role_cate)

    def meth_educ_view(self):
        return self.driver.find_element(*SecondPage.education_view)

    def meth_educ_option(self):
        return self.driver.find_element(*SecondPage.education_option)

    def meth_educ_button(self):
        return self.driver.find_element(*SecondPage.education_button)

    def meth_logout_option(self):
        return self.driver.find_element(*SecondPage.logout_option)

    def meth_logout_button(self):
        return self.driver.find_element(*SecondPage.logout_button)


