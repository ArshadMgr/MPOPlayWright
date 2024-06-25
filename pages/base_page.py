class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, selector):
        if isinstance(selector, str):
            self.page.click(selector)
        else:
            selector.click()

    def fill(self, selector, text):
        if isinstance(selector, str):
            self.page.fill(selector, text)
        else:
            selector.fill(text)

    def get_text(self, selector):
        if isinstance(selector, str):
            return self.page.text_content(selector)
        else:
            return selector.text_content()

        self.page.click(selector)
