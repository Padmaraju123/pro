import time
import pytest
from selenium.webdriver.common.by import By
from TestData.home_login_data import HomeLoginData
from pageObjects.homepage import HomePage
from utilities.basefile import Base


class TestTrip(Base):
    def test_home(self, get_data):
        log = self.get_logger()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        home_obj = HomePage(self.driver)
        home_obj.meth_user().send_keys(get_data["Username"])
        home_obj.meth_pass().send_keys(get_data["Password"])

        home_obj.meth_hide().click()
        home_obj.meth_butt1().click()

        time.sleep(1)
        home_obj.meth_scroll1()
        time.sleep(1)
        home_obj.meth_scroll2()
        time.sleep(1)
        home_obj.meth_scroll3()
        time.sleep(1)
        home_obj.meth_scroll4()
        time.sleep(1)
        home_obj.meth_scroll5()
        time.sleep(1)
        home_obj.meth_scroll6()
        time.sleep(1)
        home_obj.meth_scroll7()
        time.sleep(1)
        home_obj.meth_scroll8()
        time.sleep(1)
        home_obj.meth_scroll9()
        time.sleep(5)
        home_obj.meth_scroll_up()

        # searching the jobs
        home_obj.meth_search1().click()
        home_obj.meth_design().send_keys("Python Software Developer")
        # log.info("getting all the designations.")
        time.sleep(5)
        lists_design = home_obj.meth_list_design()
        for ll in lists_design:
            if ll.text == "Python Software Developer":
                ll.click()
                break

        home_obj.meth_exp().click()
        lists_exp = home_obj.meth_list_exp()
        for ex in lists_exp:
            txt = ex.text
            if txt == "2 years":
                ex.click()
                break

        home_obj.meth_location().send_keys("bangalore")
        list_places = home_obj.meth_list_locations()
        for place in list_places:
            tt = place.text
            if tt == "Bangalore":
                place.click()
                break

        # second page
        second_obj = home_obj.meth_search2()
        time.sleep(3)
        second_obj.meth_work_f_home().click()
        time.sleep(3)
        second_obj.meth_remote().click()
        time.sleep(3)

        # Department
        second_obj.meth_view().click()
        time.sleep(3)
        second_obj.meth_depart_input().send_keys("engineering")
        time.sleep(3)
        second_obj.meth_depart_name().click()
        time.sleep(3)
        second_obj.meth_depart_button().click()
        time.sleep(3)

        # salary
        second_obj.meth_salary_view().click()
        time.sleep(3)
        second_obj.meth_salary_option().click()
        time.sleep(3)
        second_obj.meth_salary_button().click()
        time.sleep(3)

        # company type
        second_obj.meth_company_choice().click()
        time.sleep(3)

        # role category
        second_obj.meth_role_cate().click()
        time.sleep(3)

        # education
        second_obj.meth_educ_view().click()
        time.sleep(3)
        second_obj.meth_educ_option().click()
        time.sleep(3)
        second_obj.meth_educ_button().click()

        # scrolling after all
        self.driver.execute_script("window.scrollBy(0,50)", "")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(50,100)", "")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(100,150)", "")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(150,200)", "")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(200,250)", "")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(250,document.body.scrollHeight)", "")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 0)", "")

        # logout section
        second_obj.meth_logout_option().click()
        second_obj.meth_logout_button().click()

    @pytest.fixture(params=HomeLoginData().get_data_xlsx())
    def get_data(self, request):
        return request.param









