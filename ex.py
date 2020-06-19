from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pynput.mouse import Button,Controller
import sys
import time
from datetime import date
import datetime
x=datetime.date.today()
y=x.weekday()
print(y)

def numOfDays(date1, date2):
    return (date2-date1).days

# Driver program
date1 = date(2020, 1, 1)
date2 = x
date3=numOfDays(date1, date2)

print(date3)


def search(list,n):

    l=0
    u=len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            return True
        else :
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

list = [160,196,211,226,233,274,298,316,317,358]
n = date3

if search(list,n):
    sys.exit()
elif y==6:
    print("today is sunday")
elif y==5:
    print("today is saturday")
elif y== 0 or 1 or 2 or 3 or 4:
    browser = webdriver.Chrome('D:\\work\\cnsi\\chromedriver')

    browser.maximize_window()
    browser.get("https://app1.factohr.com/apposite/Security/Login")


    username = browser.find_element_by_id("txtUsername")
    password = browser.find_element_by_id("txtPassword")
    submit   = browser.find_element_by_id("btnLogin")
    username.send_keys("INHYD-1907")
    password.send_keys("rgysa302")

    submit.click()
    time.sleep(5)
    mouse=Controller()
    mouse.position

    mouse.position=(382, 211)
    mouse.click(Button.left,1)
    time.sleep(5)
    mouse.position=(624, 447)
    mouse.click(Button.left,1)
    time.sleep(5)
    mouse.position=(950, 164)
    mouse.click(Button.left,1)



#196
#211
#226
#233
#274
#298
#316
#317
#358
