from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib2
import csv
import re
from bs4 import BeautifulSoup

PATH = "C:\ProgramData\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://itdashboard.gov/")

link = driver.find_element_by_partial_link_text("Dive in")
link.click()

url = 'https://itdashboard.gov/'
request = urllib2.Request(url)
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')
 
rows= soup.find('div', class_={'h4 w200'}).find_all('div', recursive=False)
 
file = open('agencies.csv', 'wb')
writer = csv.writer(file)
 
# write title row
writer.writerow(['Agencie', 'Total FY2021 Spending'])
 
for row in rows:

    Agencie = row.find('div', class_={'h4 w200'}).find_all('div', recursive=False).a.text.strip()
    TotalFY2021 = row.find('div', class_={'h1 w900'}).find_all('div', recursive=False).span.text.strip()
    
 
    print Agencie + ' ' + TotalFY2021 
    writer.writerow([Agencie.encode('utf-8'), TotalFY2021.encode('utf-8')])


file.close() 

PATH = "C:\ProgramData\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://itdashboard.gov/")

link = driver.find_element_by_partial_link_text("Dive in")
link.click()

link = driver.find_element_by_partial_link_text("view")
link.click()

url = 'https://itdashboard.gov/'
request = urllib2.Request(url)
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')
 
rows= soup.find('div', class_={'w200 maertop-0 w300'}).find_all('div', recursive=False)
 
file = open('individualinvest.csv', 'wb')
writer = csv.writer(file)
 
# write title row
writer.writerow(['Bureau', 'Total FY2021 Spending'])
 
for row in rows:

    Bureau= row.find('div', class_={'left select-filter'}).find_all('div', recursive=False).a.text.strip()
    TotalF2021 = row.find('td', class_={'right'}).find_all('div', recursive=False).span.text.strip()
    
 
    print Bureau + ' ' + TotalF2021 
    writer.writerow([Agencie.encode('utf-8'), TotalFY2021.encode('utf-8')])

 file.close() 
