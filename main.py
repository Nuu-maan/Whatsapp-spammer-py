import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")  # Preserve login session
chrome_options.add_argument("--remote-debugging-port=9222")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Wait for the user to log in
input("Press Enter after logging in to your WhatsApp Web account...")

while True:
    phone_number = input("Enter the phone number: ")
    spam_message = input("Enter your spam message: ")
    try:
        frequency = int(input("How many times do you want to send the message: "))
    except ValueError:
        frequency = 5    
    response = input("Response accordingly to initiate spamming (y/n): ")

    try:
        # Use explicit wait to ensure the search bar is present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        search_box.clear()
        search_box.send_keys(phone_number)
        search_box.send_keys(Keys.ENTER)

        # Wait for the contact to appear and click
        user = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="row"][@tabindex="0"]'))
        )
        user.click()
    except Exception as e:
        print("User not found :(", e)
        break

    try:
        # Adjust the selector for the message input field
        msgfield = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
    except Exception as e:
        print("Message field not found :(", e)
        break

    if response.lower() == 'y':
        print("Spamming initiated...")
        for _ in range(frequency):
            try:
                msgfield.send_keys(spam_message)
                msgfield.send_keys(Keys.ENTER)
                time.sleep(0.1)  # Delay between messages
            except Exception as e:
                print("An error occurred while sending the message :(", e)
                break
        else:
            print("Spamming completed successfully")
    else:
        print("Meet you next time :)")
        break

    ask = input("Do you want to exit (y/n): ")
    if ask.lower() == 'y':
        print("Thank you for using our spammer")
        break

# Close the WebDriver
driver.quit()
