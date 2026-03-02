import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# """
# End-to-end test for Ditto.
# """
from ditto.pages.landing_page import LandingPage
from ditto.pages.steps_page import StepsPage
from ditto.pages.premium_page import PremiumPage
from ditto.utilities.utils import get_fake_user

def test_ditto_e2e(page):
    user = get_fake_user()
    landing = LandingPage(page)
    landing.goto()
    landing.select_optima_secure()
    landing.assert_main_benefits()
    landing.next()
    landing.assert_waiting_periods()
    landing.next()
    landing.assert_whats_not_covered()
    landing.next()
    landing.assert_extra_benefits()
    landing.continue_button()

    steps = StepsPage(page)
    steps.select_gender(user["gender"])
    steps.assert_who_all()
    steps.next_step()
    # Use a valid Bangalore pincode (e.g., 560001)
    steps.fill_age_pincode(age=user["age"], pincode="560001")
    steps.calculate_premium()

    premium = PremiumPage(page)
    premium.assert_loaded()
    base, riders, gst, total = premium.get_premium_values()
    print(f"Base: {base}, Riders: {riders}, GST: {gst}, Total: {total}")
    assert abs((base + riders + gst) - total) < 1, f"Premium calculation mismatch: {base}+{riders}+{gst}!={total}"
