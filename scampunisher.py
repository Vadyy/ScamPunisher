# Copyright Vady 2018 All Rights Reserved
# Using Selenium v3.1.1 and Geckodriver v0.21.0 
print('Loading ScamPunisher v0.1')
from selenium import webdriver
#from selenium.webdriver.common.proxy import Proxy, ProxyType
import random
import json
import string
import time

def randomize(email=False):
    words = json.loads(open('words.json').read())
    word = random.choice(words)
    optionalnumbers = ""
    randomizer = [0, 1]
    if not email:
        if random.choice(randomizer) == 1:
            optionalnumbers = str(random.randint(1, 3))
    extraword = random.choice(words)
    if email:
        word.capitalize()
        extraword.capitalize()
    optionalLetters = ""
    if random.choice(randomizer) == 1:
        if not email:
            amount = random.randint(1, 6)
            counter = 0
            while counter < amount:
                optionalLetters += random.choice(string.ascii_letters)
                counter += 1
                if counter == amount:
                    break
        else:
            optionalLetters = str(random.randint(0,101))
    randomized = word + optionalnumbers + extraword + optionalLetters

    if email:
        emails = ['gmail', 'yahoo', 'outlook', 'hotmail']
        randomized += '@' + random.choice(emails) + '.com'

    return randomized

scammer = "https://free-fortnite-v-buck.weebly.com/"

print('Opening Firefox...')

# PROXY = "118.97.140.195:8080"
# prox = Proxy()
# prox.proxy_type = ProxyType.MANUAL
# prox.http_proxy = PROXY
# prox.socks_proxy = PROXY
# prox.ssl_proxy = PROXY
#
# capabilities = webdriver.DesiredCapabilities.FIREFOX
# prox.add_to_capabilities(capabilities)

driver = webdriver.Firefox() #desired_capabilities=capabilities
print('Opening the scammer website...')
driver.get(scammer)
print('Initializing the ScamPunisher')
while True:
    #Amount
    driver.find_element_by_id('input-124470319696886790').send_keys(str(random.randint(1000, 12400)))

    #Password
    password = randomize()
    driver.find_element_by_id('input-879792283493594752').send_keys(password)

    #Email
    email = randomize(email=True)
    driver.find_element_by_id('input-965882991678103459').send_keys(email)

    #Send
    driver.find_elements_by_class_name('wsite-button-inner')[0].click()
    print('Sent! Email [{}] Password [{}]'.format(email, password))
    time.sleep(1)

    #Refresh
    driver.refresh()
