import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib.request
import time


# Get the Selenium Remote URL from environment variable
selenium_url = os.environ.get("SELENIUM_REMOTE_URL", "http://chrome:4444/wd/hub")

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")

# Connect to the remote Chrome instance
#print(f"Connecting to Selenium at: {selenium_url}")

driver = webdriver.Remote(
    command_executor=selenium_url,
    options=chrome_options
)

# Open a webpage and perform some actions
driver.get("https://sccgov.iqm2.com/Citizens/Detail_Meeting.aspx?ID=16839")

# open window with video
element = driver.find_element(By.LINK_TEXT, "Video")
# TODO: error

element.click()

original_window = driver.current_window_handle
if len(driver.window_handles) > 1:
    # Switch to the new window
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
else:
    # error handling
    pass

# find video url
# For now, I am assuming that only one other window is opened
pg_src = driver.page_source

# TODO: check if no error
start = pg_src.find("MEDIA URL:")
end = pg_src[start:].find("-->")
media_url = pg_src[start + len("MEDIA URL:"):start + end].strip()

print(f"Media URL: {media_url}")
s = time.time()
urllib.request.urlretrieve(media_url, '/app/data/video_name.mp4') 
print(f"Video downloaded in {time.time() - s:.2f} seconds")

# Close the browser
driver.quit()