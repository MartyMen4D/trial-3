# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:25:51 2020

@author: martijn
"""
#%%
import numpy as np
from selenium import webdriver
from time import sleep
#import keyboard

class BumbleBot():
    def __init__(self):
        self.driver = webdriver.Chrome('C:/20 Thuisstudie/python 3/webdriver/chromedriver.exe')
#        sleep(5)
        
        
    def gotosite(self):
        self.driver.get('https://bumble.com/')
#        sleep(1)
        
        
    def login(self):
        fbbot = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
        fbbot.click()
        
        
    def facebooklogin(self):
#        facebookpath = '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div'
                       
        fb_elemnt = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div')
        fb_elemnt.click()
        
        basewindow = self.driver.window_handles[0]
        loginwindow = self.driver.window_handles[1]
        
        self.driver.switch_to_window(loginwindow)
        
        email_in_xpath = '//*[@id="email"]'
        email_in_element = self.driver.find_element_by_xpath(email_in_xpath)
        email_in_element.click()
        
        email_in_element.send_keys('martijn.mekkering@hotmail.com')
        
        
        pw_in_xpath = '//*[@id="pass"]'
        pw_in_element = self.driver.find_element_by_xpath(pw_in_xpath)
        pw_in_element.click()
        
        pw_in_element.send_keys('audia8')
        
        
        login_button_xpath = '//*[@id="u_0_0"]'
        login_button_element = self.driver.find_element_by_xpath(login_button_xpath)
        login_button_element.click()
        
        self.driver.switch_to_window(basewindow)
        
    def dislike(self):
        xpath='//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div'
        dislike_b = self.driver.find_element_by_xpath(xpath)    
        dislike_b.click()
        
    def like(self):
        xpath='//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div'
        like_b = self.driver.find_element_by_xpath(xpath)
        like_b.click()
        
        
    def autoswipe(self):
#        if keyboard.
        
        while True:
            random = np.random.random(1)[0]
            minimum = 0.5
            if random>minimum:
                waitvalue = random
            if minimum<random:
                waitvalue=minimum
            
            sleep(waitvalue)
            try:
                self.like()
            except:
                try:
                    self.close_popup()
                except:
                    self.close_match()
        
    def close_popup(self):
        closepopup = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div')
        closepopup.click()
        
    def close_match(self):
        closematch = self.driver.find_element_by_xpath('drop the stuff')
        closematch.click()
        
        
        
bot = BumbleBot()
bot.gotosite()
bot.login()
bot.facebooklogin()
bot.autoswipe()


#keyboard.wait('esc'):

    
#%%
print("HelloWorld")

print("Me")