import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Create a ChromeOptions object to configure the Chrome WebDriver.
options = Options()

# To prevent the browser from closing and keep it open after the script execution.
options.add_experimental_option("detach", True)

# To bypass SSL errors by ignoring SSL certificate errors.
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')


# Initialize a Chrome WebDriver with the specified options.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the specified URL.
driver.get('https://www.neuralnine.com/')

# Maximize the browser window to ensure full visibility.
driver.maximize_window()

# Find all links on the web page that have an 'href' attribute.
links = driver.find_elements("xpath", "//a[@href]")

# Loop through the links and find the one with "Books" in its inner HTML.
for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        # Click on the link with "Books" in its inner HTML.
        link.click()
        break

# Locate book links on the page based on specific criteria.
book_links = driver.find_elements("xpath", "//div[contains(@class, 'elementor-widget-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a")

# Click on the first book link found.
book_links[0].click()

# for book_link in book_links:
#     print(book_link.get_attribute("href"))

# Switch to the newly opened tab or window (second window handle).
driver.switch_to.window(driver.window_handles[1])
    
# Pause the script execution for 3 seconds.
time.sleep(3)

# Find and print the inner HTML of elements with specific criteria (buttons for paperback books with prices).
buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(., '$')]]")

for button in buttons:
    print(button.get_attribute("innerHTML"))








