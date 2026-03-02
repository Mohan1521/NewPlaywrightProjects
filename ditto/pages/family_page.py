from playwright.sync_api import Page
from faker import Faker

class FamilyPage:
    def __init__(self, page: Page):
        self.page = page
        self.fake = Faker()

    def assert_loaded(self):
        assert self.page.is_visible("text=Tell us about your family")

    def fill_form(self):
        # Fill the 'Tell us about you' form using Faker
        self.page.get_by_label("Name").fill(self.fake.first_name())
        self.page.get_by_label("Age").fill(str(self.fake.random_int(min=18, max=60)))
        # Try to select gender if dropdown exists
        try:
            self.page.get_by_label("Gender").select_option("Male")
        except Exception:
            pass
        # Wait for Calculate Premium button to be enabled
        self.page.get_by_role("button", name="Calculate Premium").wait_for(state="enabled", timeout=10000)

    def click_calculate_premium(self):
        self.page.get_by_role("button", name="Calculate Premium").click()
