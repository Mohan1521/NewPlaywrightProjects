def test_login(page):
    page.goto("http://www.amazon.com")
    page.wait_for_timeout(5000)
    assert "flipkart" in page.url