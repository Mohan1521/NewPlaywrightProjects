from playwright.sync_api import Page, expect
import re

class LandingPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://app.joinditto.in/fq")

    def select_optima_secure(self):
        # Use the robust selector from user script
        expect(self.page.locator("div").filter(has_text=re.compile(r"^HDFCERGOOptima Secure")).nth(2)).to_be_visible(timeout=10000)
        self.page.locator("div").filter(has_text=re.compile(r"^HDFCERGOOptima Secure")).nth(2).click()

    def assert_main_benefits(self):
        expect(self.page.get_by_role("button", name="Main Benefits")).to_be_visible(timeout=10000)

    def next(self):
        self.page.get_by_role("button", name="Next").click()

    def assert_waiting_periods(self):
        expect(self.page.get_by_role("button", name="Waiting Periods")).to_be_visible(timeout=10000)

    def assert_whats_not_covered(self):
        expect(self.page.get_by_role("button", name="Whats Not Covered")).to_be_visible(timeout=10000)

    def assert_extra_benefits(self):
        expect(self.page.get_by_role("button", name="Extra Benefits")).to_be_visible(timeout=10000)

    def continue_button(self):
        self.page.get_by_role("button", name="Continue").click()
