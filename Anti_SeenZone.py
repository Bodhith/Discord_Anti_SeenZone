####################         BOT ACCOUNTS        ###############################

#
#

#
#

####################     END OF BOT ACCOUNTS        ############################

################################################################################
################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

import time
import random

################################################################################
################################################################################

def Login(driver, email, password):

    driver.get("https://www.discord.com/login")

    inputEmail = driver.find_elements_by_xpath("//input[@name='email']")[0]

    inputEmail.click()

    time.sleep(2)

    inputEmail.send_keys(email);

    inputPassword = driver.find_elements_by_xpath("//input[@name='password']")[0]

    inputPassword.click()

    time.sleep(2)

    inputPassword.send_keys(password);

    submitButton = driver.find_elements_by_xpath("//button[@type='submit']")[0]

    submitButton.click()


################################################################################


def FindLastWho(driver):

    lastWho = driver.execute_script('''

        var chat = document.getElementById("chat-messages").children;

        var who = "";

        var messageBox;

        for(i=chat.length-2; i>0; i--)
        {
            message = chat[i];

            try
            {
                if( message.children[0].children[1].children[0].children[0].innerHTML )
                {
                    who = message.children[0].children[1].children[0].children[0].innerHTML;

                    break;
                }
            }
            catch(e)
            {
                who = "Dunno";

                console.log("Chat Message Not Found...bruh");
            }
        }

        return who
    ''')

    return lastWho


################################################################################


def Bot():

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--incognito")

    global driver

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    ######################      LOGIN     ######################

    email = ""  #  Enter your Email

    password = ""  #  Enter your Password

    Login(driver, email, password)

    ######################      END OF LOGIN     ###############
    
    ######################      SETTINGS     ###################
    
    friendChannel = ""  #  Click on a friends chat, copy the url and paste it here, like '/channels/@me/12345..'

    you = "BetaS" #  Your Username without '#TagNumber'

    lastWho = ""  # The last person messaged , Advanced Settings (Optional), Auto Detects at later parts.

    messagesArray = [":)", ":(", ":D", ":O", ":|", ";(", ":,(", ">:(", ":P", ":,(", ":$"]  #  Array of messages that you could send
    
    ######################      END OF SETTINGS     ############
    
    selectFriend =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='"+friendChannel+"']")))

    selectFriend.click()

    time.sleep(2)

    lastWho = FindLastWho(driver)

    while True:

        if lastWho != you:

            messageBox = driver.find_elements_by_xpath("//span[@data-slate-object='text']")[0]

            messageBox.send_keys(random.choice(messagesArray))

            time.sleep(1)

            messageBox.send_keys(Keys.ENTER)

            lastWho = you

        else :

            try:

                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@class='unreadPill-2HyYtt']")))

                lastWho = ""

                continue

            except:

                print("Waiting for new Message")

            lastWho = FindLastWho(driver)

            print(lastWho)


################################################################################
################################################################################


if __name__ == "__main__":

    Bot()
