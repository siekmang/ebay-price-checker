from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

'''This script searches eBay for Nintendo Switch 2 listings and displays top results'''


def ebay_search():
    """Launch Firefox and perform eBay search for Nintendo Switch 2 Sealed in Box

    Print the top three results with title, price, and link."""
    search_query = 'Nintendo Switch 2 Sealed in Box'

    '''Initialize Firefox in headless mode'''
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    print("Launching Firefox and navigating to eBay...")
    selenium = webdriver.Firefox(options=options)

    '''Navigate to eBay and perform search'''
    selenium.get('https://www.ebay.com')
    search_bar = selenium.find_element(By.ID, 'gh-ac')
    if search_query:
        search_bar.send_keys(search_query)
    else:
        print("Search query is empty.")
        selenium.quit()
        return
    print(f"Performing search for {search_query}...")
    search_bar.submit()

    '''Introduce wait'''
    wait = WebDriverWait(selenium, 10)

    '''Click on Video Game Consoles'''
    video_game_console_locator = (By.XPATH, "//a[contains(., 'Video Game Consoles')]")
    video_game_console_element = wait.until(ec.element_to_be_clickable(video_game_console_locator))

    print("Filtering by Video Game Consoles...")
    video_game_console_element.click()

    '''Click on Buy It Now'''
    buy_it_now_locator = (By.XPATH, "//a[contains(., 'Buy It Now')]")
    buy_it_now_button = wait.until(ec.element_to_be_clickable(buy_it_now_locator))

    print("Filtering by Buy It Now...")
    buy_it_now_button.click()

    '''Click on Free Shipping'''
    free_shipping_locator = (By.XPATH, "//span[contains(., 'Free Shipping')]")
    free_shipping_element = wait.until(ec.presence_of_element_located(free_shipping_locator))

    print("Filtering by Free Shipping...")
    free_shipping_element.click()

    '''Click on New'''
    new_locator = (By.XPATH, "//span[contains(., 'New')]")
    new_element = wait.until(ec.presence_of_element_located(new_locator))

    print("Filtering by New...")
    new_element.click()

    '''Sort by Price'''
    sort_locator = (By.XPATH, "//span[contains(., 'Sort')]")
    sort_element = wait.until(ec.presence_of_element_located(sort_locator))

    print("Sorting by Price...")
    sort_element.click()

    sort_by_price_locator = (By.XPATH, "//a[contains(., 'Price + Shipping: lowest first')]")
    sort_by_price_element = wait.until(ec.presence_of_element_located(sort_by_price_locator))

    sort_by_price_element.click()

    '''Get and process search results'''
    results = selenium.find_elements(By.XPATH, "//li[contains(@class, 's-card--horizontal')]")

    for i in range(2, 5):
        wait.until(
            ec.presence_of_element_located((By.XPATH, ".//span[contains(@class, 'su-styled-text primary default')]")))
        title_element = results[i].find_element(By.XPATH, ".//span[contains(@class, 'su-styled-text primary default')]")

        price_elements = results[i].find_elements(By.XPATH,
                                                  ".//span[@class='su-styled-text primary bold large-1 s-card__price']")
        result_price_text = price_elements[0].text if price_elements else "Price not found"

        link_element = results[i].find_element(By.XPATH, ".//a[contains(@class, 's-card__link')]")
        link_url = link_element.get_attribute('href')
        max_len = 75
        truncated_link = (link_url[:max_len] + '...') if len(link_url) > max_len else link_url

        '''Print results'''
        print(f"Title: {title_element.text}")
        print(f"Price: {result_price_text}")
        print(f"Link: {truncated_link}")
        print("-" * 20)

    selenium.quit()


if __name__ == '__main__':
    try:
        ebay_search()
    except Exception as e:
        print(f"An error occurred: {e}")
