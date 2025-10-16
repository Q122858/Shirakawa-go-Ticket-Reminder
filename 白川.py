
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import gc

while True:
    try:
        print(datetime.now())
        path = 'C:\Program Files\Google\Chrome\Application/chrome.exe'
        options = webdriver.ChromeOptions()
        prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
                }
            }
        options.add_experimental_option('prefs', prefs) 
        options.add_argument("disable-infobars")         
        
        driver = webdriver.Chrome(options=options)
        driver.get('https://secure.j-bus.co.jp/hon/Tour/SeatsAvailability?groupCode=210201&routeCode=0119&moveCode=0001&readOnly=false')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="tours"]/main/section/div/div[1]/div[2]/div[1]/a[2]').click()
        time.sleep(3)
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, "html.parser")
        price = soup.find_all("a", {"class": ["few","some","many"]})
        a=soup.find_all("p", {"id": "toursdateNumber"})[0].text
        print(a)
        for article in price:
                if int(article['data-yyyymmdd']) > 20240201 and int(article['data-yyyymmdd']) <20240230:
                    print(article['data-yyyymmdd'])
                    headers = {
                "Authorization": "Bearer " + "xj0DjDUh6ZJKdyjfKUfzuPfxUXGi5prfYfR7Ar9WjJW",
                "Content-Type": "application/x-www-form-urlencoded"
                    }
                params = {"message": f"Ｂコース 展望台シャトルチケット付き白川郷ライトアップバス\n https://secure.j-bus.co.jp/hon/Tour/SeatsAvailability?groupCode=210201&routeCode=0119&moveCode=0001&readOnly=false \n {article['data-yyyymmdd']} {a}有位置"}
                
                r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)


        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="tours"]/main/section/div/div[1]/div[1]/a[2]').click()
        time.sleep(3)
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, "html.parser")
        price = soup.find_all("a", {"class": ["few","some","many"]})
        a=soup.find_all("p", {"id": "toursdateNumber"})[0].text
        print(a)
        for article in price:
            if int(article['data-yyyymmdd']) > 20240201 and int(article['data-yyyymmdd']) <20240230:
                print(article['data-yyyymmdd'])
                headers = {
                "Authorization": "Bearer " + "xj0DjDUh6ZJKdyjfKUfzuPfxUXGi5prfYfR7Ar9WjJW",
                "Content-Type": "application/x-www-form-urlencoded"
                    }
                params = {"message": f"Ｂコース 展望台シャトルチケット付き白川郷ライトアップバス\n https://secure.j-bus.co.jp/hon/Tour/SeatsAvailability?groupCode=210201&routeCode=0119&moveCode=0001&readOnly=false \n {article['data-yyyymmdd']} {a}有位置"}
                
                r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
            
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="tours"]/main/section/div/div[1]/div[1]/a[2]').click()
        time.sleep(3)
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, "html.parser")
        price = soup.find_all("a", {"class": ["few","some","many"]})
        a=soup.find_all("p", {"id": "toursdateNumber"})[0].text
        print(a)
        for article in price:
            if int(article['data-yyyymmdd']) > 20240201 and int(article['data-yyyymmdd']) <20240230:
                print(article['data-yyyymmdd'])
                headers = {
                "Authorization": "Bearer " + "xj0DjDUh6ZJKdyjfKUfzuPfxUXGi5prfYfR7Ar9WjJW",
                "Content-Type": "application/x-www-form-urlencoded"
                    }
                params = {"message": f"Ｂコース 展望台シャトルチケット付き白川郷ライトアップバス\n https://secure.j-bus.co.jp/hon/Tour/SeatsAvailability?groupCode=210201&routeCode=0119&moveCode=0001&readOnly=false \n {article['data-yyyymmdd']} {a}有位置"}
                
                r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)    
        
        driver.refresh()
        driver = webdriver.Chrome(options=options)
        driver.get('https://secure.j-bus.co.jp/hon/Tour/SeatsAvailability?groupCode=180009&routeCode=0401&moveCode=0001&readOnly=false')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="tours"]/main/section/div/div[1]/div[2]/div[1]/a[2]').click()
        time.sleep(3)
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, "html.parser")
        price = soup.find_all("a", {"class": ["few","some","many"]})
        for article in price:
            if int(article['data-yyyymmdd']) > 20240201 and int(article['data-yyyymmdd']) <20240230:
                print(article['data-yyyymmdd'])
                headers = {
                    "Authorization": "Bearer " + "xj0DjDUh6ZJKdyjfKUfzuPfxUXGi5prfYfR7Ar9WjJW",
                    "Content-Type": "application/x-www-form-urlencoded"
                    }
                params = {"message": f"コースS　白川郷ライトアップバス（高岡発：展望台入場チケット付きコース）\n https://secure.j-bus.co.jp/hon/Tour/SeatsAvailability?groupCode=180009&routeCode=0401&moveCode=0001&readOnly=false \n {article['data-yyyymmdd']}有位置"}
                
                r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)    
                
        del pageSource,soup,price,driver,content,options
        gc.collect()
        driver.refresh()
        time.sleep(0)
        driver.quit()
    except:
        print()