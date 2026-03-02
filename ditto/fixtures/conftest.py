"""
Pytest fixtures for Playwright browser and page setup.
"""
import os
from datetime import datetime
import pytest
from playwright.sync_api import sync_playwright
from ditto.config.config import BASE_URL, BROWSER_HEADLESS
import traceback

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=BROWSER_HEADLESS)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context, request):
    page = context.new_page()
    page.goto(BASE_URL)
    # Take screenshot immediately after loading the page
    screenshots_dir = os.path.join(os.path.dirname(__file__), "..", "reports", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    test_name = request.node.name.replace("/", "_")
    filename = f"{test_name}_immediate_{timestamp}.png"
    filepath = os.path.join(screenshots_dir, filename)
    print(f"[DEBUG] Attempting immediate screenshot to: {filepath}")
    try:
        page.screenshot(path=filepath, full_page=True)
        print(f"[DEBUG] Immediate screenshot saved: {filepath}")
    except Exception as e:
        print(f"[DEBUG] Immediate screenshot failed: {e}")
        traceback.print_exc()
    yield page
    # Take screenshot before closing the page
    screenshots_dir = os.path.join(os.path.dirname(__file__), "..", "reports", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    test_name = request.node.name.replace("/", "_")
    filename = f"{test_name}_finalizer_{timestamp}.png"
    filepath = os.path.join(screenshots_dir, filename)
    print(f"[DEBUG] Attempting to save screenshot to: {filepath}")
    try:
        if page:
            page.screenshot(path=filepath, full_page=True)
            print(f"[DEBUG] Screenshot saved in finalizer: {filepath}")
        else:
            print("[DEBUG] Page object is None at screenshot time.")
    except Exception as e:
        print(f"[DEBUG] Screenshot failed in finalizer: {e}")
        traceback.print_exc()
    page.close()
