import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

#PATH = r"C:\Users\asus\Desktop\selenium_python\chromedriver.exe"
driver = webdriver.Chrome()
logging.basicConfig(level=logging.DEBUG)


def getLinks():
    link_list = []
    driver.get("https://www.mubawab.ma/fr/listing-promotion")
    lastPage = int(driver.find_element(By.ID, "lastPageSpan").text)
    for i in range(1, lastPage):
        link = "https://www.mubawab.ma/fr/listing-promotion:p:"+str(i)
        driver.get(link)
        time.sleep(0.5)
        li = driver.find_elements(By.CLASS_NAME, 'promotionListing.listingBox.w100')
        for l in li:
            link_item = l.get_attribute("linkref")
            link_list.append(link_item)
    return link_list

    
def scrap():
    data = 'data.csv'
    data = open(data, 'w', encoding='utf16', newline='')
    csv_writer = csv.writer(data, delimiter=';')
    csv_writer.writerow(
        ['Titre', 'Emplacememnt', 'Lat', 'Lon', 'Price', 'Badge', 'Livraison', 'Agence'])

    links = getLinks()
    #links = ["https://www.mubawab.ma/fr/p/2565/les-jardins-de-yanice"] #only for testing
    for link in links:
        print(link)
        driver.get(link)
        price = driver.find_element(By.CLASS_NAME, 'SpremiumH2.orangeText').text
        lat = driver.find_element(By.ID, 'mapOpen').get_attribute('lat')
        lon = driver.find_element(By.ID, 'mapOpen').get_attribute('lon')
        title = driver.find_element(By.CLASS_NAME, 'SpremiumH2').text
        emplacememnt = driver.find_element(By.CLASS_NAME, 'immoDetails.vAlignM.darkblue').text
        badge = driver.find_element(By.XPATH, '/html/body/div[13]/div[1]/div[2]/div[3]/p').text
        livraison = driver.find_element(By.XPATH, '/html/body/div[13]/div[1]/div[2]/div[4]/p').text
        agence = driver.find_element(By.CLASS_NAME, 'agencyBoxH2').text
        csv_writer.writerow(
                    [title, emplacememnt, lat, lon, price, badge, livraison, agence])
        


        

if __name__ == '__main__':
    scrap()

