def test_amazon_login(page):
    page.goto("https://www.amazon.in/ap/signin")
    page.wait_for_timeout(3000)
    assert "signin" in page.url