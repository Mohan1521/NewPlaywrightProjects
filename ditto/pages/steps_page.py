from playwright.sync_api import Page, expect

class StepsPage:
    def __init__(self, page: Page):
        self.page = page

    def assert_title(self, expected: str):
        assert self.page.is_visible(f"text={expected}")

    def click_next_until_continue(self):
        while not self.page.is_visible("button:has-text('Continue')"):
            self.page.get_by_role("button", name="Next").click()
            self.page.wait_for_timeout(500)

    def click_continue(self):
        self.page.get_by_role("button", name="Continue").click()

    def select_gender(self, gender="Male"):
        expect(self.page.get_by_text(gender).first).to_be_visible(timeout=10000)
        self.page.get_by_text(gender).first.click()

    def assert_who_all(self):
        expect(self.page.get_by_role("heading", name="Who all do you want to buy")).to_be_visible(timeout=10000)

    def next_step(self):
        self.page.get_by_role("button", name="Next step").click()

    def fill_age_pincode(self, age, pincode):
        expect(self.page.get_by_role("textbox", name="Your age")).to_be_visible(timeout=10000)
        self.page.get_by_role("textbox", name="Your age").click()
        self.page.get_by_role("textbox", name="Your age").fill(str(age))
        expect(self.page.get_by_role("textbox", name="Proposer's Pincode")).to_be_visible(timeout=10000)
        self.page.get_by_role("textbox", name="Proposer's Pincode").click()
        self.page.get_by_role("textbox", name="Proposer's Pincode").fill(str(pincode))

    def calculate_premium(self):
        expect(self.page.get_by_role("button", name="Calculate Premium")).to_be_enabled(timeout=10000)
        self.page.get_by_role("button", name="Calculate Premium").click()
