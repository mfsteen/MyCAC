from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = webdriver.Firefox(firefox_binary = FirefoxBinary(
    firefox_path='/home/msteen/Documents/Installations/FirefoxESR/firefox'))
browser.get('http://localhost:8000')

assert 'Django' in browser.title

