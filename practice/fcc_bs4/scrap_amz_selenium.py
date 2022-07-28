import os
from selenium import webdriver

newpath = r'C:\SeleniumDrivers'
os.environ['PATH'] += os.pathsep + newpath
driver = webdriver.Chrome()