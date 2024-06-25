from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options for headless mode and other configurations
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Grant microphone permission
prefs = {
    "profile.default_content_setting_values.media_stream_mic": 1,  # Allow microphone access
    "profile.default_content_setting_values.media_stream_camera": 1  # Allow camera access (if needed)
}
chrome_options.add_experimental_option("prefs", prefs)

# Set up WebDriver with Chrome options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def start_vapi():
    try:
    # Step 1: Visit the website
        driver.get('https://vapi.ai/')
    
    # Optionally, wait for the page to load
        time.sleep(5)  # Adjust the sleep time as needed
    
    # Step 2: Click on the button using the provided XPath
        button = driver.find_element(By.XPATH, '//*[@id="circle"]/div/div/div/div/div[1]')
        button.click()

    # Optionally, wait to observe the result
        time.sleep(5)  # Adjust as needed

    # Keep the script running
        print("Script execution completed. WebDriver remains open.")
        print("Press Ctrl+C to terminate the script.")

    # Infinite loop to keep the script running
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Closing the WebDriver.")

    finally:
    # Close the WebDriver when you're ready to exit
        driver.quit()
        print("WebDriver closed.")
