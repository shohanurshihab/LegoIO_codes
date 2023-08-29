from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        start_url = "https://www.aiub.edu"
        page.goto(start_url)

        links = page.query_selector_all('a')

        for link in links:
            link_url = link.get_attribute('href')
            if link_url and '#' not in link_url:
                try:
                    page.goto(link_url)
                    print(f"Clicked and loaded: {link_url}")
                except:
                    print(f"Unable to click and load: {link_url}")

                page.goto(start_url)
        
        browser.close()

if __name__ == '__main__':
    main()
