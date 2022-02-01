from playwright.sync_api import sync_playwright

def new_cookie(url):
    cookie = None
    def set_cookie(req):
        nonlocal cookie
        if "cookie" in req.headers:
            cookie = req.headers["cookie"]

    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.on("request", set_cookie)
        page.goto(url)
        browser.close()

    return cookie

print(new_cookie("https://www.baidu.com/"))