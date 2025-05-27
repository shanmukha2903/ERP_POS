import string
from os import name

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
import random
import time
from faker import Faker
import  re

from pages.login_page import LoginPage
from utils.data_reader import DataReader
import math
import logging

from datetime import datetime
from datetime import datetime, timedelta
fake = Faker()
logger = logging.getLogger(__name__)

class POSPage(BasePage):
    def __init__(self, page, data_reader: DataReader):
        super().__init__(page)
        self.order_amounts = None
        self.data_reader = data_reader
        self.order_ids = []
        self.context = page.context

    def select_till(self, till_name):
        xpath_till = f"//span[text()='{till_name}']"
        self.click_element(xpath_till)
        self.click_element("//span[text()='Next']")
        logger.info(f"Selected till: {till_name}")

    def select_random_products(self):
        product_codes = self.data_reader.get_value("product_codes", [])
        selected = random.sample(product_codes, min(5, len(product_codes)))

        for code in selected:
            self.fill_text("//input[@id='sm-product-search']", code)
            self.page.keyboard.press("Enter")
            self.page.wait_for_timeout(500)
        logger.info(f"Selected products: {selected}")

    def press_plus_key(self,times:int = 3):
        for _ in range(times):
            self.page.keyboard.press("+")
        logger.info("products should be  added")


    def press_minus_key(self,times:int = 3):
        for _ in range(times):
            self.page.keyboard.press("-")
            logger.info("products should be delected")


    def refresh_page(self):
        self.page.reload()

    def delect_partial_amount_cash(self):
        self.click_element('//img[@style="height: 15px; width: 15px; cursor: pointer; margin-left: 1vw; position: absolute; right: 5px; top: 15%;"]')





    def product_drawer(self):
        self.click_element("//button[@id='sm-product-drawer']")
        self.click_element("(//span[contains(text(),'ADD')])[2]")
        self.click_element("//button[@id='sm-product-drawer']")
        self.click_element("(//span[contains(text(),'ADD')])[1]")
        self.click_element("//button[@id='sm-product-drawer']")
        self.click_element("(//span[contains(text(),'ADD')])[3]")
        logger.info("Added products from drawer")

    def delete_two_products(self):
        self.click_element('(//img[contains(@id,"sm-product-delete")])[2]')
        logger.info("Deleted two products")

    def cash_payment_full(self):
        self.click_element("//p[text()='Total Amount To Pay']")
        self.click_element("//span[text()='Cash']")
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info("Processed full cash payment")

    def upi_payment_full(self):
        self.click_element("//p[text()='Total Amount To Pay']")
        self.click_element("//span[text()='UPI']")
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info("Processed full UPI payment")

    def razor_payment_full(self):
        self.click_element("//p[text()='Total Amount To Pay']")
        self.click_element("//span[text()='Razor Pay']")
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info("Processed full Razor Pay payment")

    def card_payment_full(self):
        self.click_element("//p[text()='Total Amount To Pay']")
        self.click_element("//span[text()='Card']")
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info("Processed full card payment")

    def swiggy_payment(self):
        self.click_element("//p[text()='Total Amount To Pay']")
        self.click_element("(//span[contains(text(),'Swiggy')])[3]")
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info("Processed Swiggy payment")

    def zomato_payment(self):
        self.click_element("//p[text()='Total Amount To Pay']")
        self.click_element("(//span[contains(text(),'Zomato')])[3]")
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info("Processed Zomato payment")

    def online_payment(self):
        self.click_element("//p[text()='Total Amount To Pay']")
        self.click_element("(//span[contains(text(),'Online')])[2]")
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info("Processed Online payment")

    def cash_payment_partial_dynamic(self):
        total_amount_text = self.page.inner_text("//p[text()='Total Amount To Pay']/following-sibling::p")
        total_amount = float(total_amount_text.replace("₹", "").strip())

        if total_amount > 1:
            partial_amount = random.randint(1, math.floor(total_amount - 1))
        else:
            partial_amount = 1

        self.click_element("//p[text()='Total Amount To Pay']")
        self.click_element("//span[text()='Cash']")
        self.fill_text("//input[@placeholder='Enter Amount']", str(partial_amount))
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info(f"Processed partial cash payment: {partial_amount}")

    def card_remaining_partial(self):
        self.click_element("//span[text()='Card']")
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info("Processed remaining card payment")

    def upi_remaining_partial(self):
        self.click_element("//span[text()='UPI']")
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info("Processed remaining UPI payment")

    def razor_remaining_partial(self):
        self.click_element("//span[text()='Razor Pay']")
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info("Processed remaining Razor Pay payment")

    def sale_type_swiggy(self):
        self.click_element("//span[text()='Walkin']")
        self.click_element("//div[@style='background-color: rgb(142, 172, 205); margin-bottom: 1.5vh; height: 14vh; display: flex; justify-content: center; align-items: center; border-radius: 10px;']//span[text()='Swiggy']")
        logger.info("Set sale type to Swiggy")

    def sale_type_zomato(self):
        self.click_element("//span[text()='Walkin']")
        self.click_element(
            "//div[@style='background-color: rgb(222, 229, 212); margin-bottom: 1.5vh; height: 14vh; display: flex; justify-content: center; align-items: center; border-radius: 10px;']//span[text()='Zomato']")
        logger.info("Set sale type to Zomato")

    def sale_type_online(self):
        self.click_element("//span[text()='Walkin']")
        self.click_element("(//div[contains(@class, 'productName')])[4]")
        logger.info("Set sale type to Online")

    # def create_customer(self):
    #     name = fake.name()
    #     self.click_element("//input[@id='sm-customer-search']")
    #     self.click_element("//span[text()='Add Customer']")
    #     self.fill_text("//input[@placeholder='First Name']", name)
    #     self.click_element("//span[text()='Create new Customer']")
    #     logger.info(f"Created customer: {name}")

    def create_customer(self):
        name = fake.name()
        self.last_created_customer = name  # Store for later use

        self.click_element("//input[@id='sm-customer-search']")
        self.click_element("//span[text()='Add Customer']")
        self.fill_text("//input[@placeholder='First Name']", name)
        self.click_element("//span[text()='Create new Customer']")

        logger.info(f"Created customer: {name}")

    def select_existing_customer(self):
        name = getattr(self, "last_created_customer", None)
        if not name:
            raise ValueError("No customer name stored. Please create a customer first.")

        self.click_element("//input[@id='sm-customer-search']")
        self.click_element("(//input[contains(@id,'sm-product-search')])[2]")
        self.fill_text("(//input[contains(@id,'sm-product-search')])[2]", name)
        self.click_element('//p[@style="margin-bottom: 0px; color: rgb(15, 7, 24); font-size: 1.25em; font-weight: 500; position: relative; text-align: left;"]')
        # self.click_element(f"//span[contains(text(), '{name}')]")


        logger.info(f"Selected existing customer: {name}")

    def log_out(self):
        self.click_element('//img[@style="padding-left: 1rem; height: 2vw;"]')
        self.click_element("//span[text() = 'Logout']")
        self.click_element("//span[text() = 'Next']")
        self.click_element("//span[text() = 'Next']")
        self.click_element("//span[text() = 'Close Shift']")
        logger.info(f"log_out: {name}")

    def  menu_button(self):
        self.click_element("(//div[contains(@class ,'ant-col ant-col-1')])[1]")

    def full_sync(self):
        self.click_element("//span[text() = 'Full Sync']")
        logger.info("full_sync")

    def menu_delect(self):
        self.click_element('//img[@style="margin-left: auto; padding-top: 2vh; cursor: pointer; width: 1.5vw;"]')

    def product_sync(self):
        self.click_element("//span[text() = 'Product Sync']")
        logger.info("product_sync")

    def product_sync_with_product(self):
        self.click_element("//span[text() = 'Product Sync']")
        self.click_element("//span[text() =  'Yes']")
        logger.info("products_sync")

    def unlink(self):
        self.click_element("//span[text()  =  'Unlink Till']")
        self.click_element("//span[text() = 'Next']")
        self.click_element("//span[text() = 'Next']")
        self.click_element("//span[text() = 'Close Shift']")
        logger.info("Unlink")

    def hold_parked(self):
        self.click_element('//span[text()="Hold"]')
        self.click_element('//span[text()="Yes"]')
        logger.info(f"Clicked Hold")

    def cancel_product(self):
        self.click_element('//span[text()="Cancel"]')
        self.click_element('//span[text()="Yes"]')
        logger.info(f"Clicked Cancel Button: Cancel")

    def parked_bills(self):
        # Click on Parked Bills menu
        self.click_element('//span[text()="Parked Bills"]')

        # Fetch all parked bill arrows
        try:
            right_arrows = self.page.query_selector_all('//span[@style="color: rgb(146, 144, 152);"]')

            if right_arrows and len(right_arrows) >= 2:
                right_arrows[1].click()
                logger.info("Clicked on 2nd parked bill.")
            elif right_arrows and len(right_arrows) == 1:
                right_arrows[0].click()
                logger.info("Only 1 parked bill available. Clicked on the 1st one.")
            else:
                logger.warning("No parked bills found.")
                return

            # Click the retrieve button
            self.click_element('//p[@id="sm-parked-bill-retrieve"]')
            logger.info("Clicked on Retrieve Sale.")

        except Exception as e:
            logger.error(f"Error while retrieving parked bill: {e}")

    def parked_bills_discard(self):
        # Click on Parked Bills menu
        self.click_element('//span[text()="Parked Bills"]')

        # Fetch all parked bill arrows
        try:
            right_arrows = self.page.query_selector_all('//span[@style="color: rgb(146, 144, 152);"]')

            if right_arrows and len(right_arrows) >= 2:
                right_arrows[1].click()
                logger.info("Clicked on 2nd parked bill.")
            elif right_arrows and len(right_arrows) == 1:
                right_arrows[0].click()
                logger.info("Only 1 parked bill available. Clicked on the 1st one.")
            else:
                logger.warning("No parked bills found.")
                return

            # Click the retrieve button
            self.click_element('//p[@id="sm-parked-bill-discard"]')
            self.click_element("//span[text() ='OK']")
            self.click_element("//img[@id= 'sm-parked-bill-back']")
            logger.info("Clicked discard Sale.")



        except Exception as e:
            logger.error(f"Error while discard parked bill: {e}")

    def parked_bills_discard_all(self):
        # Click on Parked Bills menu
        self.click_element('//span[text()="Parked Bills"]')
        self.click_element("//span[@id= 'sm-parked-bill-expand']")
        self.click_element('//p[@id="sm-parked-bill-discard"]')
        self.click_element("//span[text()='OK']")
        self.click_element("//img[@id='sm-parked-bill-back']")
        logger.info("Discarded one parked bill.")

    def replace_parked_bills(self):
        # Click on Parked Bills menu
        self.click_element('//span[text()="Parked Bills"]')

        # Fetch all parked bill arrows
        try:
            right_arrows = self.page.query_selector_all('//span[@style="color: rgb(146, 144, 152);"]')

            if right_arrows and len(right_arrows) >= 2:
                right_arrows[1].click()
                logger.info("Clicked on 2nd parked bill.")
            elif right_arrows and len(right_arrows) == 1:
                right_arrows[0].click()
                logger.info("Only 1 parked bill available. Clicked on the 1st one.")
            else:
                logger.warning("No parked bills found.")
                return

            # Click the retrieve button
            self.click_element('//p[@id="sm-parked-bill-retrieve"]')
            self.click_element("//span[text() ='Yes']")
            logger.info("Clicked replace Sale.")

        except Exception as e:
            logger.error(f"Error while retrieving parked bill: {e}")


    def unlink_when_orders_in_PB(self):
        self.click_element("//span[text()  =  'Unlink Till']")
        self.click_element('//img[@style="margin-left: auto; padding-top: 2vh; cursor: pointer; width: 1.5vw;"]')
        self.click_element('//span[text()="Parked Bills"]')

        # Fetch all parked bill arrows
        try:
            right_arrows = self.page.query_selector_all('//span[@style="color: rgb(146, 144, 152);"]')

            if right_arrows and len(right_arrows) >= 2:
                right_arrows[1].click()
                logger.info("Clicked on 2nd parked bill.")
            elif right_arrows and len(right_arrows) == 1:
                right_arrows[0].click()
                logger.info("Only 1 parked bill available. Clicked on the 1st one.")
            else:
                logger.warning("No parked bills found.")
                return

            # Click the retrieve button
            self.click_element('//p[@id="sm-parked-bill-retrieve"]')
            logger.info("Clicked on Retrieve Sale.")

        except Exception as e:
            logger.error(f"Error while retrieving parked bill: {e}")

    def read_present_invoice_number(self):
        self.click_element('//span[text()="Invoice"]')
        self.click_element('//span[text()="Advance"]')

        invoice_locator = self.page.locator("//span[contains(text(),'Invoice No:')]")
        self.page.wait_for_selector("//span[contains(text(),'Invoice No:')]")
        full_text = invoice_locator.inner_text().strip()
        invoice_number = full_text.replace("Invoice No:", "").strip()
        print(f"Present Invoice Number: {invoice_number}")

        self.invoice_no = invoice_number

        return invoice_number

    def sales_history_two(self):

        invoice_number = self.invoice_no

        self.click_element('//span[text()="Sales History"]')
        self.page.wait_for_timeout(9000)

        search_input = self.page.locator('//input[@placeholder="Search for Customers/Document Number/Contact"]')
        search_input.fill(invoice_number)
        search_input.press("Enter")
        self.page.wait_for_timeout(2000)

    def search_invoice_in_sales_history(self):
        # This function becomes unnecessary if sales_history_two uses self.invoice_no
        self.sales_history_two()

    def sales_history_expand(self):
        self.click_element("//span[@id= 'sm-salesHistory-expand']")
        self.click_element("//p[text()='Retrieve Sale']")

    def extra_payment_methods(self):
        self.click_element('//span[text()="..."]')
        self.click_element('//span[text()="Complete Order"]')
        logger.info("Completed order: Done")

    def create_advance_click(self):
        self.click_element('//div[text()="Create Advance"]')
        logger.info("advance: clicked")

    def advance_order(self):
        self.click_element('//span[text()="Invoice"]')
        self.click_element('//span[text()="Advance"]')
        logger.info("Clicked on Invoice > Advance")

    def check_customer_alert(self) -> bool:
        """Handle 'Customer not selected' alert."""
        try:
            locator = self.page.locator('//div[@class="ant-message-custom-content ant-message-warning"]/span')
            locator.wait_for(timeout=3000)
            alert_text = locator.inner_text()
            print(f" ALERT DISPLAYED: {alert_text}")  # Printed to console
            logger.warning(f"Alert shown: {alert_text}")  # Logged
            return True
        except TimeoutError:
            logger.info(" No customer alert appeared.")
            return False

    def close_advance_order(self):
        self.click_element("//span[@class = 'anticon anticon-close ant-modal-close-icon']")

    def handle_product_alert(page: Page):
        try:
            # Wait for the alert message to appear (max 5 seconds)
            alert_locator = page.locator("div.ant-message-custom-content.ant-message-error span")
            alert_locator.wait_for(timeout=5000)

            # Extract and print the alert message text
            alert_text = alert_locator.text_content()
            print(f"[PRODUCT ALERT] {alert_text.strip()}")

        except Exception as e:
            print("[PRODUCT ALERT] No alert message appeared or timed out.")

    def only_one_product(self):
        self.click_element("//button[@id='sm-product-drawer']")
        self.click_element("(//span[contains(text(),'ADD')])[2]")

    def select_tomorrow_date(self):
        # Step 1: Click the calendar icon to open the picker
        self.click_element('//span[@aria-label="calendar"]')
        self.click_element('//input[@placeholder="Select date"]')

        # Step 2: Calculate tomorrow's day number
        tomorrow = datetime.today() + timedelta(days=1)
        tomorrow_day = str(tomorrow.day)

        # Step 3: Click the date (e.g., '6' for May 6)
        self.click_element(f"//div[contains(@class,'ant-picker-cell-inner') and text()='{tomorrow_day}']")

        # Step 4: Click "Ok" to confirm
        self.click_element("//span[text()='Ok']")

        print(f"[CALENDAR] Selected tomorrow's date: {tomorrow.strftime('%Y-%m-%d')}")


    def upi_payment_partial_dynamic(self):
        total_amount_text = self.page.inner_text("//p[text()='Total Amount To Pay']/following-sibling::p")
        total_amount = float(total_amount_text.replace("₹", "").strip())

        if total_amount > 1:
            partial_amount = random.randint(1, math.floor(total_amount - 1))
        else:
            partial_amount = 1

        self.click_element("//p[text()='Total Amount To Pay']")
        self.click_element("//span[text()='UPI']")
        self.fill_text("//input[@placeholder='Enter Amount']", str(partial_amount))
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info(f"Processed partial cash payment: {partial_amount}")

    def total_amount_click(self):
        self.click_element("//p[text()='Total Amount To Pay']")

    def  change_advance_order_to_sale_order(self):
        self.click_element('//span[text()="Advance"]')
        self.click_element('//span[text()="Invoice"]')

    def shift_close(self):
        logger.info("Starting login inside shift_close()")
        self.click_element('//div[@style="padding-top: 1em;"]')

        logger.info("Initiating login after shift close")
        login_page = LoginPage(self.page, self.data_reader)
        login_page.login_without_url()
        self.click_element('//span[text()="Next"]')
        logger.info("Shift close and login completed")

    def modify_the_order(self):
        self.click_element("(//tr[contains(@class, 'ant-table-row') and contains(@class, 'ant-table-row-level-0')])[1]")

    def modify_the_order2(self):
        self.click_element("(//tr[contains(@class, 'ant-table-row') and contains(@class, 'ant-table-row-level-0')])[2]")

    def lock_key(self):
        self.click_element('//img[@style="height: 3vh; cursor: pointer; margin-right: 0.7rem;"]')
        self.click_element('//span[text()="Log In"]')

        password = self.data_reader.get_value("password")
        self.fill_text('input[name="password"]', password)
        self.click_element("//button[@id='login']")
        logger.info("Completed login with password only")
        self.page.wait_for_timeout(4000)
        logger.info("POS page loaded successfully")

    def get_total_amount_to_pay(self) -> float:
        total_text = self.get_text(
            '//div[@id="sm-cart-total"]//p[contains(text(), "Total Amount To Pay")]/following-sibling::p')
        total_amount = float(re.findall(r'[\d.]+', total_text)[0])
        logger.info(f"Fetched 'Total Amount To Pay': ₹{total_amount}")
        return total_amount

    def apply_manual_discount_percentage(self):
        # Step 1: Click on Manual Discount
        self.click_element('//span[text()="Manual Discount"]')

        # Step 2: Select "Total Bill Discount %"
        self.click_element('//input[@id="discountName"]')
        self.click_element('//div[text()="Total Bill Discount %"]')
        logger.info("Selected 'Total Bill Discount %'")

        # Step 3: Get the Total Bill before discount
        total_bill_text = self.get_text('//p[contains(text(), "Total Bill")]')
        total_bill_amount = float(re.findall(r'[\d.]+', total_bill_text)[0])
        logger.info(f" Total Bill before discount: ₹{total_bill_amount}")

        # Step 4: Enter Random Discount % (1.00 - 9.99)
        self.page.wait_for_selector('//div[@id="discountValue"]//input[@placeholder="Enter Percentage"]',
                                    state="visible")
        discount_percent = round(random.uniform(1, 9.9), 2)
        self.fill_text('//div[@id="discountValue"]//input[@placeholder="Enter Percentage"]', str(discount_percent))
        logger.info(f"Entered Discount: {discount_percent}%")

        # Step 5: Capture After Discount Amount
        after_discount_text = self.get_text('//p[contains(text(), "After discount")]')
        after_discount_amount = float(re.findall(r'[\d.]+', after_discount_text)[0])
        logger.info(f" Displayed After Discount Amount: ₹{after_discount_amount}")

        # Step 6: Validate Calculation
        expected_discount = round(total_bill_amount * (discount_percent / 100), 2)
        expected_price = round(total_bill_amount - expected_discount, 2)

        if abs(expected_price - after_discount_amount) < 0.01:
            logger.info(" Discount percentage calculation is correct!")
        else:
            logger.error(" Discount validation failed!")
            logger.error(f"Expected After Discount: ₹{expected_price}, but got ₹{after_discount_amount}")
            assert False, "Discount calculation mismatch!"

        # Step 7: Apply Discount
        self.click_element('//span[text()="Apply"]')

        # Optional Step 8: Continue to Payment Flow
        self.click_element('//span[text()="cwsuite"]')
        self.click_element('//input[@id="pinInput"]')
        self.click_element('(//button[text()="1"])[4]')
        self.click_element('(//button[@id="sm-amount-button2"])[3]')
        self.click_element('(//button[text()="1"])[4]')
        self.click_element('(//button[@id="sm-amount-button2"])[3]')
        self.click_element('//span[text()="Approve"]')

        logger.info(f"🎉 Manual Percentage Discount of {discount_percent}% applied and validated successfully.")

    def manual_discount_amount(self):
        # Step 1: Click on Manual Discount
        self.click_element('//span[text()="Manual Discount"]')

        # Step 2: Select "Total Bill Discount Amount"
        self.click_element('//input[@id="discountName"]')
        self.click_element('//div[text()="Total Bill Discount Amount"]')
        logger.info("Selected 'Total Bill Discount Amount'")

        # Step 3: Extract Total Bill before discount
        total_bill_text = self.get_text('//p[contains(text(), "Total Bill")]')
        total_bill_amount = float(re.findall(r'[\d.]+', total_bill_text)[0])
        logger.info(f"Total Bill before discount: ₹{total_bill_amount}")

        # Step 4: Enter Random Discount (including decimals)
        self.page.wait_for_selector('//div[@id="discountValue"]//input[@placeholder="Enter Amount"]', state="visible")
        discount_amount = round(random.uniform(1, 99.99), 2)
        self.fill_text('//div[@id="discountValue"]//input[@placeholder="Enter Amount"]', str(discount_amount))
        logger.info(f"Entered Discount Amount: ₹{discount_amount}")

        # Step 5: Capture After Discount Amount
        after_discount_text = self.get_text('//p[contains(text(), "After discount")]')
        after_discount_amount = float(re.findall(r'[\d.]+', after_discount_text)[0])
        logger.info(f"Displayed After Discount Amount: ₹{after_discount_amount}")

        # Step 6: Validate Calculation
        expected_price = round(total_bill_amount - discount_amount, 2)
        if abs(expected_price - after_discount_amount) < 0.01:
            logger.info(" Discount amount calculation is correct!")
        else:
            logger.error(f" Discount mismatch! Expected ₹{expected_price}, but got ₹{after_discount_amount}")
            raise AssertionError("Manual discount amount validation failed!")

        # Step 7: Apply Discount
        self.click_element('//span[text()="Apply"]')

        # Step 8: Continue to Payment Flow
        self.click_element('//span[text()="cwsuite"]')
        self.click_element('//input[@id="pinInput"]')
        self.click_element('(//button[text()="1"])[4]')
        self.click_element('(//button[@id="sm-amount-button2"])[3]')
        self.click_element('(//button[text()="1"])[4]')
        self.click_element('(//button[@id="sm-amount-button2"])[3]')
        self.click_element('//span[text()="Approve"]')

        logger.info(f"Manual Discount: Applied and validated successfully with amount ₹{discount_amount}")

    def remove_and_validate_discount(self):
        # Get discounted total before removing
        discounted_amount = self.get_total_amount_to_pay()

        # Remove discount
        self.click_element('//span[text()="Manual Discount"]')
        self.click_element("//span[text()='Remove Discount']")
        logger.info("Clicked on Remove Discount")

        # Get total after removing discount
        self.page.wait_for_timeout(2000)  # wait for UI to reflect change
        amount_after_removal = self.get_total_amount_to_pay()

        assert amount_after_removal > discounted_amount, (
            f"Discount removal failed! Expected > ₹{discounted_amount}, got ₹{amount_after_removal}"
        )
        logger.info(f"Discount successfully removed. Amount reset to ₹{amount_after_removal}")

    def process_random_payment(self):
        methods = [
            ("Cash", "//span[text()='Cash']"),
            ("UPI", "//span[text()='UPI']"),
            ("Razor Pay", "//span[text()='Razor Pay']"),
            ("Card", "//span[text()='Card']")
        ]

        self.click_element("//p[text()='Total Amount To Pay']")

        visible = [m for m in methods if self.is_element_visible(m[1], timeout=2)]
        if not visible:
            raise Exception("No payment methods available")

        method, selector = random.choice(visible)
        self.click_element(selector)
        self.click_element("(//button[contains(text(), 'Enter')])[2]")
        logger.info(f"Payment done using {method}")

    def sales_history_for_advance(self):

        invoice_number = self.invoice_no

        self.click_element('//span[text()="Sales History"]')
        self.page.wait_for_timeout(8000)

        search_input = self.page.locator('//input[@placeholder="Search for Customers/Document Number/Contact"]')
        search_input.fill(invoice_number)
        search_input.press("Enter")
        self.page.wait_for_timeout(2000)



    def store_order_amount(self):
        """Store the order amount from the cart (right-side panel)."""
        total_text = self.get_text('//div[@id="sm-cart-total"]')  # e.g., 'Total Amount To Pay\n\n1279.97'
        print(f"[DEBUG] Raw total_text: {total_text}")

        # Extract numeric value using regex
        match = re.search(r"\d+(?:\.\d+)?", total_text)
        if not match:
            raise ValueError(f"❌ Could not find a valid number in total_text: {total_text}")

        total = float(match.group())
        print(f"[DEBUG] Extracted total amount: {total}")

        # Initialize or reuse the list
        if not hasattr(self, 'order_amounts') or self.order_amounts is None:
            self.order_amounts = []

        self.order_amounts.append(total)
        logger.info(f"Stored Order Amount: {total}")
        print(f"✅ Stored Order Amount: {total}")

    def validate_sales_amount(self):
        """Validate order total vs Close Till sales amount."""
        if not hasattr(self, 'order_amounts') or not self.order_amounts:
            raise ValueError("❌ No order amounts stored to validate.")

        expected_sum = round(sum(self.order_amounts), 2)

        # Locate the correct input field (adjust .nth(X) if needed)
        selector = '//input[contains(@class, "transactionAmtInputClose")]'
        locator = self.page.locator(selector).nth(4)  # Example: 5th input field

        locator.scroll_into_view_if_needed()
        sales_amount_str = locator.input_value()

        match = re.search(r"\d+(?:\.\d+)?", sales_amount_str)
        if not match:
            raise ValueError(f"❌ Could not extract a number: {sales_amount_str}")

        sales_amount = float(match.group())

        print(f"🧾 Expected Sum: {expected_sum}")
        print(f"🧾 Sales Amount: {sales_amount}")
        assert expected_sum == round(sales_amount, 2), \
            f"❌ Mismatch: Orders Total = {expected_sum} vs Sales Amount = {sales_amount}"
        print("✅ Sales Amount Validation Passed")

    def log_out_validation(self):
        self.click_element('//img[@style="padding-left: 1rem; height: 2vw;"]')
        self.click_element("//span[text() = 'Logout']")
        self.click_element("//span[text() = 'Next']")
        # self.click_element("//span[text() = 'Next']")
        # self.click_element("//span[text() = 'Close Shift']")
        logger.info(f"log_out: {name}")

    def nan_validation(self):
        self.click_element("//span[text() = 'Next']")
        self.click_element("//span[text() = 'Close Shift']")

    def store_order_id(self):
        """
        Extract the Order ID (e.g., Test 02/1045) and log/check for duplicates.
        """
        order_id_text = self.get_text('//span[contains(text(), "Invoice No:")]')
        print(f"[DEBUG] Raw Order ID Text: {order_id_text}")

        # Corrected regex to capture the full ID
        match = re.search(r'Invoice No:\s*(.+)', order_id_text)
        if not match:
            raise ValueError(f"❌ Could not extract a valid Order ID from: {order_id_text}")

        order_id = match.group(1).strip()
        print(f"[INFO] Extracted Order ID: {order_id}")

        # Duplicate check
        if order_id in self.order_ids:
            print(f"⚠️ Duplicate Order ID Detected: {order_id}")
            logger.warning(f"Duplicate Order ID Detected: {order_id}")
            # Optional: add exit logic or fail the test here
            raise Exception(f"Duplicate Order ID encountered: {order_id}")
        else:
            self.order_ids.append(order_id)
            print(f"✅ Stored Unique Order ID: {order_id}")
            logger.info(f"Stored Order ID: {order_id}")

    # pages/pos_page.py
    # def reopen_in_new_tab(self):
    #     """Copies current URL, opens new tab in same context, closes old tab, and navigates to URL"""
    #     try:
    #         # Get current URL
    #         current_url = self.page.url
    #         logger.info(f"Current URL: {current_url}")
    #
    #         # Create new page in same context
    #         new_page = self.context.new_page()
    #
    #         # Navigate to URL before closing original
    #         new_page.goto(current_url, wait_until="domcontentloaded")
    #
    #         # Close original page
    #         self.page.close()
    #
    #         # Update references
    #         self.page = new_page
    #         self.page.bring_to_front()
    #
    #         logger.info("Successfully transferred to new tab")
    #         return self.page
    #
    #     except Exception as e:
    #         logger.error(f"Failed to transfer to new tab: {str(e)}")
    #         raise

    def coupon_code_without_product(self):
        self.click_element('//span[text()="Coupon Code"]')
        try:

            popup_message = self.page.locator('.ant-message span:has-text("Coupon cant be applied for return items")')
            popup_message.wait_for(state="visible", timeout=5000)  # Wait up to 5 seconds for popup to appear
            expect(popup_message).to_be_visible()
            expect(popup_message).to_have_text("Coupon cant be applied for return items")
            logger.info("Coupon code popup verified successfully: 'Coupon cant be applied for return items'")

            self.page.wait_for_timeout(3000)
            logger.info("Paused for 3 seconds to observe the popup")

            if popup_message.is_visible():
                logger.info("Popup is still visible after 3 seconds")
            else:
                logger.info("Popup auto-dismissed within 3 seconds")

        except TimeoutError:
            logger.error("Coupon code popup did not appear within 5 seconds")
            self.page.screenshot(path="coupon_popup_error.png")
            raise
        except AssertionError as e:
            logger.error(f"Coupon code popup verification failed: {str(e)}")
            self.page.screenshot(path="coupon_popup_error.png")
            raise

    def coupon_code(self):
        try:
            # Extract total amount before coupon
            total_amount_locator = self.page.locator('//div[@id="sm-cart-total"]/p[2]')
            total_amount_locator.wait_for(state="visible", timeout=5000)
            total_amount_text = total_amount_locator.inner_text().strip()
            total_amount = float(total_amount_text)
            print(f"Total Amount To Pay: ₹{total_amount:.2f}")
            logger.info(f"Total Amount To Pay: ₹{total_amount:.2f}")

            # Click Coupon Code element
            self.click_element('//span[text()="Coupon Code"]')
            logger.info("Clicked Coupon Code element")

            # Apply coupon code
            self.click_element('//input[@placeholder="Type Code"]')
            self.page.keyboard.type("1234")
            self.click_element('//span[text()="Apply"]')
            logger.info("Typed 1234 into coupon code input field using keyboard")
            self.click_element('//span[@style="margin: 0.7rem 0px 0.7rem 10px; font-size: 1vw;"]')
            logger.info("clicked cwsuite")
            self.click_element('//input[@placeholder="Enter value"]')
            self.page.keyboard.type("1212")
            logger.info("Typed 1212 into coupon code input field using keyboard")
            self.click_element('//span[text()="Approve"]')
            logger.info("approved")

            # Extract total amount after coupon approval
            total_amount_locator = self.page.locator('//div[@id="sm-cart-total"]/p[2]')
            total_amount_locator.wait_for(state="visible", timeout=5000)
            total_amount_text = total_amount_locator.inner_text().strip()
            total_amount = float(total_amount_text)
            print(f"Total Amount To Pay After Coupon: ₹{total_amount:.2f}")
            logger.info(f"Total Amount To Pay After Coupon: ₹{total_amount:.2f}")

            return total_amount

        except TimeoutError:
            logger.error("Total amount element did not appear within 5 seconds")
            self.page.screenshot(path="total_amount_error.png")
            raise
        except ValueError:
            logger.error(f"Invalid total amount format: {total_amount_text}")
            self.page.screenshot(path="total_amount_error.png")
            raise
        except Exception as e:
            logger.error(f"Error in get_total_amount: {str(e)}")
            self.page.screenshot(path="total_amount_error.png")
            raise

    def coupon_removel(self):
        self.click_element("(//div[contains(@class ,'ant-col ant-col-1')])[1]")
        self.click_element('//span[text()="Coupon Code"]')
        self.click_element('//img[@style="height: 3.5vh; width: 1.5vw; cursor: pointer; position: absolute; right: 0.8vw;"]')
        self.click_element("//span[text()='Yes']")
        self.click_element('(//span[contains(text(),"Cancel")])[2]')


    def custom_box(self, data=None):
        # Open the product selection modal
        self.click_element('//span[@class="anticon anticon-code-sandbox"]')
        self.click_element('//span[text()="Add Products"]')

        # Wait for the product list to load
        product_rows_xpath = "//div[contains(@class, 'ant-row')]//button[contains(@class, 'ant-btn') and .//span[contains(@class, 'anticon-plus')]]/ancestor::div[contains(@class, 'ant-row')]"
        self.page.wait_for_selector(product_rows_xpath, timeout=10000)  # Wait up to 10 seconds for the product list

        # Find all product rows in the current page
        product_rows = self.page.locator(product_rows_xpath)
        total_products = product_rows.count()
        print(f"Found {total_products} products on the current page.")

        if total_products == 0:
            print("No products found in the list.")
            return

        # Determine how many products to select (max 5, or fewer if there aren't enough products)
        num_to_select = min(5, total_products)

        # Randomly select indices for the products
        selected_indices = random.sample(range(total_products), num_to_select)
        print(f"Selected indices: {selected_indices}")

        # Click the '+' button for each selected product
        for index in selected_indices:
            # XPath to locate the '+' button for the specific product row
            plus_button_xpath = f"({product_rows_xpath})[{index + 1}]//button[contains(@class, 'ant-btn') and .//span[contains(@class, 'anticon-plus')]]"
            print(f"Attempting to click '+' button for product at index {index} with XPath: {plus_button_xpath}")

            # Wait for the '+' button to be visible
            self.page.wait_for_selector(plus_button_xpath, timeout=2000)  # Wait up to 5 seconds for the button
            plus_button = self.page.locator(plus_button_xpath).first
            plus_button.click()
            self.page.wait_for_timeout(500)  # Small delay to ensure the UI updates

        # Click OK to close the modal
        self.click_element(
            '//button[@style="background-color: rgb(47, 56, 86); color: rgb(255, 255, 255); width: 8vw; height: 6.5vh; border-radius: 5px; margin-right: 1vw;"]')
        self.click_element('//span[text()="Submit"]')

    def custom_boxes(self):
        self.click_element('//span[@class="anticon anticon-code-sandbox"]')
        # self.click_element('//span[text()="Add Products"]')
        all_buttons_xpath = "//button[@class='ant-btn ant-btn-icon-only']"
        plus_buttons_xpath = "//button[@class='ant-btn ant-btn-icon-only' and .//span[contains(@class, 'anticon-plus')]]"
        self.page.wait_for_selector(all_buttons_xpath, timeout=3000)

        # Find all '+' buttons in the modal
        plus_buttons = self.page.locator(plus_buttons_xpath)
        total_plus_buttons = plus_buttons.count()
        print(f"Found {total_plus_buttons} '+' buttons in the modal.")

        if total_plus_buttons == 0:
            print("No '+' buttons found in the list.")
            return

        # Determine how many '+' buttons to click (max 5, or fewer if there aren't enough buttons)
        num_to_click = min(5, total_plus_buttons)

        # Randomly select indices for the '+' buttons
        selected_indices = random.sample(range(total_plus_buttons), num_to_click)
        print(f"Selected indices for '+' buttons: {selected_indices}")

        # Click each selected '+' button
        for index in selected_indices:
            # Use the exact XPath to locate the specific '+' button by index
            button_xpath = f"({plus_buttons_xpath})[{index + 1}]"
            print(f"Attempting to click '+' button at index {index} with XPath: {button_xpath}")

            # Wait for the button to be visible
            self.page.wait_for_selector(button_xpath, timeout=5000)  # Wait up to 5 seconds for the button
            button = self.page.locator(button_xpath).first
            button.click()
            self.page.wait_for_timeout(500)
            self.click_element('//span[text()="Add Products"]')

            # Wait for the product list to load
            product_rows_xpath = "//div[contains(@class, 'ant-row')]//button[contains(@class, 'ant-btn') and .//span[contains(@class, 'anticon-plus')]]/ancestor::div[contains(@class, 'ant-row')]"
            self.page.wait_for_selector(product_rows_xpath, timeout=10000)  # Wait up to 10 seconds for the product list

            # Find all product rows in the current page
            product_rows = self.page.locator(product_rows_xpath)
            total_products = product_rows.count()
            print(f"Found {total_products} products on the current page.")

            if total_products == 0:
                print("No products found in the list.")
                return

            # Determine how many products to select (max 5, or fewer if there aren't enough products)
            num_to_select = min(5, total_products)

            # Randomly select indices for the products
            selected_indices = random.sample(range(total_products), num_to_select)
            print(f"Selected indices: {selected_indices}")

            # Click the '+' button for each selected product
            for index in selected_indices:
                # XPath to locate the '+' button for the specific product row
                plus_button_xpath = f"({product_rows_xpath})[{index + 1}]//button[contains(@class, 'ant-btn') and .//span[contains(@class, 'anticon-plus')]]"
                print(f"Attempting to click '+' button for product at index {index} with XPath: {plus_button_xpath}")

                # Wait for the '+' button to be visible
                self.page.wait_for_selector(plus_button_xpath, timeout=2000)  # Wait up to 5 seconds for the button
                plus_button = self.page.locator(plus_button_xpath).first
                plus_button.click()
                self.page.wait_for_timeout(500)  # Small delay to ensure the UI updates

            # Click OK to close the modal
            self.click_element(
                '//button[@style="background-color: rgb(47, 56, 86); color: rgb(255, 255, 255); width: 8vw; height: 6.5vh; border-radius: 5px; margin-right: 1vw;"]')
            self.click_element('//span[text()="Submit"]')

    def custom_boxes_delect_product(self):
        self.click_element('//span[@class="anticon anticon-code-sandbox"]')
        delete_buttons = self.page.locator('//img[contains(@src, "delete1.eaf8a42c.svg")]')
        count = delete_buttons.count()
        if count >= 3:
            random_indices = random.sample(range(1, count), 2)
            for index in random_indices:
                delete_buttons.nth(index).click()
        elif count == 2:
            delete_buttons.nth(1).click()
        else:
            print("Less than 2 clickable products to delete.")

        self.click_element("//span[text() ='Submit']")




    def custom_mix_product_search(self):
        self.click_element('//span[text()="Add Products"]')
        self.click_element('//input[@placeholder="Search Item Code / Description"]')

    def custom_mix_add_five_products_by_description(self):
        product_descriptions = self.data_reader.get_value("product_descriptions", [])
        if not product_descriptions:
            logger.error("No product descriptions found in test_data")
            raise ValueError("No product descriptions found in test_data")

        selected_descriptions = random.choices(product_descriptions, k=5)

        self.click_element('//span[text()="Add Products"]')
        self.click_element('//input[@placeholder="Search Item Code / Description"]')
        for description in selected_descriptions:
            search_input = '//input[@placeholder="Search Item Code / Description"]'
            self.fill_text(search_input, description)
            self.press_enter(search_input)
            time.sleep(1)
            plus_button_xpath = f'//p[contains(text(), "{description}")]/following::button[@class="ant-btn ant-btn-icon-only"][2]'
            self.click_element(plus_button_xpath)
            time.sleep(1)

        # Click "Okay" and "Submit"
        self.click_element('//span[text()="Okay"]')
        self.click_element('//span[text()="Submit"]')

    def custom_mix_qty_change(self):
        self.click_element("(//button[contains(@type,'button')])[3]")
        product_index = random.randint(1,5)
        self.click_element(f"(//tr[contains(@class, 'ant-table-row-level-1')])[{product_index}]")
        self.page.keyboard.press('+')

































































