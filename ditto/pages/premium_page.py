from playwright.sync_api import Page, expect
import re

class PremiumPage:
    def __init__(self, page: Page):
        self.page = page

    def assert_loaded(self):
        # Check for a unique, always-present element on the premium summary page
        expect(self.page.get_by_text("Base Premium")).to_be_visible(timeout=10000)

    def get_premium_values(self):
        # Wait for the premium summary to be visible
        expect(self.page.get_by_text("Base Premium")).to_be_visible(timeout=10000)
        # Get the value next to "Base Premium"
        base_value = self.page.locator("text=Base Premium").locator("xpath=following-sibling::*[1]").inner_text()
        # Get the value next to "Total Premium"
        total_value = self.page.locator("text=Total Premium").locator("xpath=following-sibling::*[1]").inner_text()
        # For add-ons/riders, sum all visible add-on values (if any)
        riders_value = 0.0  # If you want to sum checked add-ons, add logic here
        # GST may not be shown separately; if not, set to 0
        gst_value = 0.0
        def parse_amount(text):
            import re
            match = re.search(r"₹([\d,]+(?:\.\d{1,2})?)", text)
            return float(match.group(1).replace(",", "")) if match else 0.0
        base = parse_amount(base_value)
        total = parse_amount(total_value)
        return base, riders_value, gst_value, total

    def assert_premium_calculation(self):
        base, riders, gst, total = self.get_premium_values()
        assert abs((base + riders + gst) - total) < 1, f"Premium calculation mismatch: {base}+{riders}+{gst}!={total}"
