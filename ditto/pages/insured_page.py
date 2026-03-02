from playwright.sync_api import Page
from faker import Faker

class InsuredPage:
    def __init__(self, page: Page):
        self.page = page
        self.fake = Faker()

    def assert_loaded(self):
        assert self.page.is_visible("text=Who all do you want to buy health insurance for?")

    def fill_form(self):
        # Select only 'You' (Self) for the test
        self.page.get_by_text("Self").click()
        # Wait for the Next button to be enabled
        self.page.get_by_role("button", name="Next").wait_for(state="enabled", timeout=10000)

    def click_next(self):
        self.page.get_by_role("button", name="Next").click()
