import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('./chromedriver')
driver.get('https://web.whatsapp.com/')

input("Press any key after logging in your whatsapp web account")


while True:
    name=input("Enter the user name:")
    spam_message=input("Enter your spam message:")
    try:
        frequency=int(input("How many times do you want to send the message:"))
    except ValueError:
        frequency=5    
    response=input("Response accordingly to initiate spamming (y/n):")
    try:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    except:
        print("User not found :(")
        break
    user.click()
    time.sleep(2)
    msgfield = driver.find_element_by_class_name("_3uMse")
    c=0
    flag=0
    if response=='y':
        print("Spamming initiated...")
        for c in range(1,frequency+1):
            try:
                msgfield.send_keys(spam_message)
                time.sleep(0.5)
                msgfield.send_keys(Keys.ENTER)
            except:
                print("Some error occured :(") 
                flag=1
                break
        if flag==0:
            print("Spamming completed successfully")
    else:
        print("Meet you next time :)")
        break
    ask=input("Do you want to exit (y/n):")
    if ask=='y':
        print("Thank you for using our spammer")
        break
    else:
        continue